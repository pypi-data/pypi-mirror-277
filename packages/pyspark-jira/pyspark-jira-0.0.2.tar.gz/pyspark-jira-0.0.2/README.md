# PySpark JIRA Data Source

`pyspark-jira` is a simple yet powerful Python package designed to integrate JIRA with Apache Spark.
This package allows users to seamlessly read JIRA tickets and create Spark DataFrames, enabling
efficient data processing and analysis within the Spark ecosystem. Whether you are managing agile
workflows or performing detailed project analytics, `pyspark-jira` makes it easy to leverage
the power of PySpark for your JIRA data.

## Getting Started

### Installation

```bash
pip install pyspark-jira
```

### Usage

```python
jira_username = "Your full email address that you used for logging in"
jira_api_token = "See https://id.atlassian.com/manage-profile/security"
jql_query = "project = 'ES'"
df = (
    spark.read.format("jira")
        .option("JIRA_USERNAME", jira_username)
        .option("JIRA_API_TOKEN", jira_api_token)
        .load(jql_query)
)
df.show()
```

