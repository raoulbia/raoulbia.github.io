Title: Databricks PySpark
Date: 2023-01-24
Category: Databricks
Slug: databricks_pyspark
Summary: Databricks PySpark


#### Create Table from DataFrame
```
df.write.format("delta").mode("overwrite").saveAsTable("schema_name.table_name")
```

#### Create Empty Table 
```
spark.sql("CREATE OR REPLACE TABLE team_data.bob_tbl(GPI_NO STRING, 
                                                     DAY_SPLY STRING, 
                                                     RX INT, 
                                                     QTY Decimal(10,3), 
                                                     IC Decimal(10,2), 
                                                     AWP Decimal(15,8), 
                                                     MBR INT)")
```

#### Create Table from DataFrame with overwriteSchema

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


#### Save DataFrame as XLS
```python
(df.write
 .mode("overwrite")
 .format("com.crealytics.spark.excel")
 .option("header", "true")
 .save("/mnt/userspace/custom_dataset/path-to-dir/filename.xlsx"))
 ```

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

#### Misc.
```
spark.sql("""desc formatted <table name>""").show(100, truncate=False)
```

#### Useful Links
* https://learn.microsoft.com/en-us/azure/databricks/spark/latest/spark-sql/spark-pandas
* https://www.educba.com/pyspark-withcolumn/
