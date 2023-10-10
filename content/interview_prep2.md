Title: Interview Prep
Date: 1900-04-26
Category: None
Slug: interview_prep2
Summary: Interview Prep

#### Data Modelling

* longitudinal data model
  + track the same subjects over multiple time points
  + useful for identifying trends, patterns, or impacts of interventions over time
* Relational data model
  + Designed for transactional operations, it uses tables to represent entities and their relationships. It's optimized for data integrity and complex queries.
* Dimensional data model
  + Designed for analytical processing, it uses facts and dimensions to represent data. It's optimized for fast query performance and ease of use in data analysis.
* Columnar databases
  + collect statistics about the data stored in each column, which can further enhance query performance. These statistics can include information like minimum and maximum values …

<br>

#### Databases

* Handling large volumes of data
  + Partitioning rows by e,g, Prescription Date to more effectively retrieve data from last 30 days 
  + Indexing: create a lookup table on e.g. email address
  + Batch processing: data load every Monday at 5 AM
  + Sharding (distributed databases) distribute data across multiple clusters
  + Archiving old data
* Security
  + access control: roles 
  + data masking: row or column level (Optum onshore offshore example)
  + backups
  + hardware: regular updates and batches

<br>

#### ETL

* pipeline key elements: 
  + sources: CSV files
  + ingestion: ADF
  + processing: Databricks notebooks
  + output: optimised drug prices
* robust, reliable and efficient pipeline
  + Error Handling: automated email alerts if pipeline fails
  + Data validation: schema validation through ADF e.g. helps check date format is consistent
  + Monitoring time to execute
  + Scalability i.e. ability to handle increasing volume: azure cloud and ADF take care of this by design
* CI/CD: only high quality code ends up in PROD
  + Automated testing every time code is committed
  + Version control to make roll back easier
  + Better work flow management by integrating with Jira
  + Consistency of environment e.g. python library version
  + Monitoring (alerts)
  + Audit of changes made

* Moving data between layers: Prefect with Jinja and SQL templates
  - Bronze to Silver:		
    + raw data from various sources is ingested into the Bronze layer. 
    + cleans, deduplicates, and validates
  - Silver to Gold: 
    + transformed to make fit for purpose for analytics
    + transformations, aggregations, and enrichments
  - Gold Layer: 
    + optimized for fast querying and analysis. 
    + ETL process may create indexed views, materialized views, or summary tables to facilitate quick data retrieval.
  - Note: Each stage would have its own set of validation checks, error-handling mechanisms, and monitoring to ensure data integrity and pipeline robustness.

#### Documentation

* Confluence: stakeholders, engagement scope, AS IS process, testing plan & results, hand-over
* Code: 
  + docstring inputs outputs of functions incl. data type, descriptions 
  + PEP8 style guide, linter, pycharm
  + Adopt Strongly typed coding style although not enforced as such


