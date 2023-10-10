Title: Interview Prep
Date: 1900-04-26
Category: None
Slug: interview_prep2
Summary: Interview Prep

#### Data Modelling

•	longitudinal data model
  o	track the same subjects over multiple time points
  o	useful for identifying trends, patterns, or impacts of interventions over time
•	Relational data model
  o	Designed for transactional operations, it uses tables to represent entities and their relationships. It's optimized for data integrity and complex queries.
•	Dimensional data model
  o	Designed for analytical processing, it uses facts and dimensions to represent data. It's optimized for fast query performance and ease of use in data analysis.
•	Columnar databases
  o	collect statistics about the data stored in each column, which can further enhance query performance. These statistics can include information like minimum and maximum values …


Databases
•	Handling large volumes of data
  o	Partitioning rows by e,g, Prescription Date to more effectively retrieve data from last 30 days 
  o	Indexing: create a lookup table on e.g. email address
  o	Batch processing: data load every Monday at 5 AM
  o	Sharding (distributed databases) distribute data across multiple clusters
  o	Archiving old data
•	Security
  o	access control: roles 
  o	data masking: row or column level (Optum onshore offshore example)
  o	backups
  o	hardware: regular updates and batches

<br>

#### ETL
•	pipeline key elements: 
  o	sources: CSV files
  o	ingestion: ADF
  o	processing: Databricks notebooks
  o	output: optimised drug prices
•	robust, reliable and efficient pipeline
  o	Error Handling: automated email alerts if pipeline fails
  o	Data validation: schema validation through ADF e.g. helps check date format is consistent
  o	Monitoring time to execute
  o	Scalability i.e. ability to handle increasing volume: azure cloud and ADF take care of this by design
•	CI/CD: only high quality code ends up in PROD
  o	Automated testing every time code is committed
  o	Version control to make roll back easier
  o	Better work flow management by integrating with Jira
  o	Consistency of environment e.g. python library version
  o	Monitoring (alerts)
  o	Audit of changes made
•	Moving data between layers: Prefect with Jinja and SQL templates
  o	Bronze to Silver:		
    * raw data from various sources is ingested into the Bronze layer. 
    * cleans, deduplicates, and validates 
  o	Silver to Gold: 
    *	transformed to make fit for purpose for analytics. 
    *	transformations, aggregations, and enrichments 
  o	Gold Layer: 
    *	optimized for fast querying and analysis. 
    *	ETL process may create indexed views, materialized views, or summary tables to facilitate quick data retrieval.
  o	Each stage would have its own set of validation checks, error-handling mechanisms, and monitoring to ensure data integrity and pipeline robustness."

<br>

#### Documentation
•	Confluence: stakeholders, engagement scope, AS IS process, testing plan & results, hand-over
•	Code 
  o	docstring inputs outputs of functions incl. data type, descriptions 
  o	PEP8 style guide, linter, pycharm
  o	Adopt Strongly typed coding style although not enforced as such


