Title: Databricks PySpark
Date: 2023-01-24
Category: Databricks
Slug: databricks_pyspark
Summary: Databricks PySpark


#### Exporting as CSV from Data Factory

```
-- save as CSV 

-- step 1 create parquet file

df.coalesce(1).write
.format("parquet")
.option("header", "true")
.mode("overwrite")
.save(f'{OUTPATH}/{today_nodash}_FDA_Drug_Shortages_Exclusions')

-- step 2 create ADF copy data activity

- requires two datasets
     a) for the source : New dataset > select File System > parquet
     b) for the sink: New dataset > select File System > delimited text
        - note: in the sink dataset
          - tick the box "First row as header"    
          - use custom filename in file path e.g. @concat(formatDateTime(utcnow(),'yyyy'), formatDateTime(utcnow(),'MM'), formatDateTime(utcnow(),'dd'), '_FDA_Drug_Shortages_Exclusions.csv')
   - in the copy data activity "source" settings > select wildcard file path
   - in the copy data activity "sink" settings 
        > select "Copy Behaviour" as "Merge"
        > type ".csv" in File type extension
```
<br>

#### Snippets
```
df = spark.read.format("parquet").load(file)
df = (spark.read.format('csv').option('header', 'true').load(file))
df.write.format("delta").mode("overwrite").saveAsTable("team_data.DXD_OFSH_000_RATIONAL_LIMITS")
spark.createDataFrame(res, StringType()).write.format("delta").mode("overwrite").saveAsTable("team_data.DXQ_DEFAULT_CEILINGS")
```
<br>

#### Create Delta Table from DataFrame
```
df.write.format("delta").mode("overwrite").saveAsTable("schema_name.table_name")
```

<br>


#### Create Temp View
```
df.createOrReplaceTempView("my_temp_view")
```

<br>

#### Create Empty Table 
```
spark.sql("CREATE OR REPLACE TABLE team_data.bob_tbl(COL1 STRING, 
                                                     COL2 INT, 
                                                     COL3 Decimal(10,3)")
```

<br>

#### Save Dataframe as XLS
```python
(spark.createDataFrame(df).write
 .mode("overwrite")
 .format("com.crealytics.spark.excel")
 .option("header", "true")
 .option("dataAddress", "'Sheet Name'!A1")
 .save("/mnt/userspace/custom_dataset/path-to-dir/filename.xlsx"))
```

<br>

#### Save DataFrame as CSV

To save a DataFrame as CSV requires three steps. 

1. Use `coalesce()` to create a parquet file, Note, here the path points to a directory, NOT a file.
2. Read the parquet file into a Pandas DataFrame: `pd.read_parquet()`
3. save the Pandas DataFrame e.g. `df.to_csv('...', index=False)`

```python
(res
 .coalesce(1)
 .write
 .save("/mnt/userspace/custom_dataset/path-to-dir/"))
```

<br>

#### Load CSV Then Save As Parquet
```
from pyspark.sql.types import *

# Define Schema
schema = StructType([StructField('COL1', LongType(), True) \
                    ,StructField('COL2',StringType(), True) \
                    ,StructField('COL3', TimestampType(), True) ])

# File location and type
file_location = "/mnt/userspace/custom_dataset/username/file.csv"
file_type = "csv"

# Make DF from CSV file
df = spark.read.format(file_type) \
  .schema(schema) \
  .option("header", "true") \
  .option("sep", ",") \
  .load(file_location)
  
# Save DF as Parquet
(df.write
 .mode("overwrite")
 .format("parquet")
 .option("header", "true")
 .save("/mnt/userspace/custom_dataset/username/file.parquet"))
```

<br>

#### Create Spark DF from Pandas DF then Save As Excel or Parquet

Note we Save As Parquet if we want to export it as CSV file via ADF Copy data activity

```
df_spark = spark.createDataFrame(df, schema=schema)
df_spark.write.format("delta").mode("overwrite").saveAsTable("team_data.MYTABLE")
OUTPATH = '/mnt/userspace/custom_dataset/...'
df = spark.sql('select * from team_data.MYTABLE')
df.write.format("com.crealytics.spark.excel").option("header", "true").mode("overwrite").save(f'{OUTPATH}/shortages_api_{today}.xlsx')
df.write.format("parquet").option("header", "true").mode("overwrite").save(f'{OUTPATH}/{today_nodash}_FDA_Drug_Shortages_RxMac')
```

<br>

#### Persist Dataframe in Delta Lake

About overwriteSchema: if any new column is added the command will not fail but overwrite the delta table with new schema. 
[Read More](https://mungingdata.com/delta-lake/schema-enforcement-evolution-mergeschema-overwriteschema/)

```python
def persist_dataframe(dataframe: object, path: str, schema_name: str, table: str, evolution: bool = False) -> None :
    """
    function to persist the dataframe to parquet and/or delta lake
    return: success/error message

    Evolution = True will mergeSchema - This is for  incremental schema changes.
    Evolution = False will OverwriteSchema - This is for wiping out old schema for new schema
    """

    # Check if table exists
    _, table_exist = validate_table_source(path=path, schema_name=schema_name, table=table)

    target = "{0}.{1}".format(schema_name, table)

    if table_exist is True :
        # if schema evolution is set merge the schemas
        if evolution is True :
            dataframe.write.format("delta").option("mergeSchema", "true").mode("overwrite").saveAsTable(target)
            print("Data overwritten and Schema evolved for table {0} in database".format(target))
        else :
            dataframe.write.format("delta").option("overwriteSchema", "true").mode("overwrite").saveAsTable(target)
            print("Data and Schema overwritten. New Schema in place for table {0} in database".format(target))
    else :
        dataframe.write.format("delta").saveAsTable(target)
        print("Table {0} added to database".format(target))


    # Do we want to partition? if so parse the partition key from the config
    print("\n- Dataframe successfully persisted in Delta Lake\n")
```
<br>

#### Parameterised Query

```python
SCHEMA_A = dbutils.widgets.get("<Azure Data Factory Base parameter name 1>")
SCHEMA_B = dbutils.widgets.get("<Azure Data Factory Base parameter name 2>")

df = spark.sql("""SELECT c.claim_nbr 
                  FROM {0}.TABLE1 c
                  LEFT JOIN {1}.TABLE2 p
                         ON (c.claim_nbr = p.claim_nbr 
               """.format(SCHEMA_A, SCHEMA_B))
```

<br>

#### Misc.
```
spark.sql("""desc formatted <table name>""").show(100, truncate=False)
```

#### Useful Links
* [Spark-Pandas](https://learn.microsoft.com/en-us/azure/databricks/spark/latest/spark-sql/spark-pandas)
* [PySpark withColumn](https://www.educba.com/pyspark-withcolumn/)
