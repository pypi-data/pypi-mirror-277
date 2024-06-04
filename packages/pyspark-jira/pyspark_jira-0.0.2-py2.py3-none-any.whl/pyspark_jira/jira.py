#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests
from requests.auth import HTTPBasicAuth

from pyspark.sql.datasource import DataSource, DataSourceReader


class JIRAReader(DataSourceReader):
    def __init__(self, schema, options):
        self.schema = schema
        self.options = options

    def read(self, partition=None):
        base_url = "https://databricks.atlassian.net"
        search_api_endpoint = "/rest/api/3/search"
        jql_query = self.options.get("path")
        headers = {
            "Accept": "application/json"
        }
        username = self.options.get("jira_username")
        api_token = self.options.get("jira_api_token")
        auth = HTTPBasicAuth(username, api_token)
        params = {
            "jql": jql_query,
            "maxResults": "100"  # This can be configurable
        }
        response = requests.request(
            "GET",
            base_url + search_api_endpoint,
            headers=headers,
            params=params,
            auth=auth
        )
        response.raise_for_status()
        data = response.json()
        for issue in data["issues"]:
            key = issue["key"]
            summary = issue["fields"]["summary"]
            created = issue["fields"]["created"]
            assignee = issue["fields"]["assignee"]["displayName"] if issue["fields"]["assignee"] else "Unassigned"
            reporter = issue["fields"]["reporter"]["displayName"]
            components = [component["name"] for component in issue["fields"]["components"]]
            yield (
                key, summary, assignee, reporter, components, created
            )


class DefaultSource(DataSource):

    @classmethod
    def name(cls):
        return "jira"

    def schema(self):
        return "key string, summary string, assignee string, reporter string, components array<string>, created string"

    def reader(self, schema):
        return JIRAReader(schema, self.options)
