Title: Databricks Spark SQL
Date: 2023-01-24
Category: Databricks
Slug: databricks_sparksql
Summary: Databricks SparkSQL

#### Pandas to Spark
```
df_spark = spark.createDataFrame(df_pandas)
```

#### Pandas to Spark with Schema
```python
# create schema for your dataframe
schema = StructType([StructField("CONTRACT_ID", StringType(), True) \
                    ,StructField("CONTRACT_NAME", StringType(), True) \
                    ,StructField("ACCOUNT", StringType(), True) \
                    ,StructField("LINE_OF_BUSINESS", StringType(), True) \
                    ,StructField("CLIENT_SHAREPOINT", StringType(), True)])
 
# Convert Pandas DataFrame to Spark DataFrame
df = spark.createDataFrame(pandas_df, schema=schema)
```

#### Create temp View
```python
df.createOrReplaceTempView("tmp_vw")
```

#### Pandas to Spark to Table
```python
(spark.createDataFrame(df, StringType())
 .write
 .format("delta")
 .mode("overwrite")
 .saveAsTable("schema_name.table_name"))
```

#### Read CSV File
```python
fpath = """/mnt/userspace/custom_dataset/path-to-file/filename.csv"""
`df = (spark.read.format('csv').option('header', 'true').load(fpath))`
```

#### Read Parquet File
```python
fpath = """/mnt/userspace/custom_dataset/path-to-file/filename.parquet"""
df = spark.read.format("parquet").load(fpath)
```

#### Create Table from CSV File
```python
DROP TABLE IF EXISTS schema_name.table_name ;
CREATE TABLE schema_name.table_name
USING csv
LOCATION "/mnt/userspace/custom_dataset/bboggava/outbound_data/MACTOOLS/mac_config.csv"
OPTIONS(header=True, inferSchema=True)
```

#### Subsetting DataFrame

* Spark DataFrame: `df.where(df.GPI_NO == '12345').display()`
* Pandas DataFrame: `df[df.GPI_NO == '12345'].sort_values(by='DAY_SPLY', ascending=False)`


#### Misc.
```python
SHOW COLUMNS IN schema_name.table_name
```

```python
DESCRIBE TABLE EXTENDED schema_name.table_name
```

Only for tables, NOT views:
```python
DESCRIBE DETAIL schema_name.table_name` 
```
