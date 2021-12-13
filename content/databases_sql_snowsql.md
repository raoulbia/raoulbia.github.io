Title: SnowSQL Cheatsheet
Date: 2017-11-23
Category: Databases
Slug: snowsql
Summary: SnowSQL  Cheatsheet

#### SnowSQL CLI Config file

The onfig file is located here: `/home/<user>/.snowsql`. This is where you configure custom connection parameters.

In your config file you need to modify this line:

`log_file = ../snowsql_rt.log` to this `log_file = ~/.snowsql/snowsql_rt.log`


#### Connect to Snowflake account with SnowSQL CLI

`snowsql --accountname 123.north-europe.azure --username <username>`

`snowsql -c my_connection`


#### Bulk Loading from Local Source

Create the Employee table

```
create or replace table Employee (
    row_id integer,
    first_name varchar(50),
    last_name varchar(50),
    city varchar(50),
    state varchar(50),
    hire_date date,
    salary integer
)

```

Some Employee queries

```
select * From Public.Employee
drop table Employee
truncate table Employee
```

Create a File Format Object
```
create or replace file format employee_csv
  type = 'CSV'
  field_delimiter = ','
  skip_header = 1;
```

Create an internal Stage object
```
create or replace stage employee_stage
  file_format = employee_csv;
```

Display the stages we have created
```
show stages
```

See what's in the employee_stage
```
list @employee_stage;
```

Move the data in employee_stage to the employee table. Skip the entire file on any errors
```
copy into employee
  from @employee_stage
  on_error = 'skip_file';
```


Move the data in employee_stage to the employee table. Skip just the rows causing any errors
```
copy into employee
  from @employee_stage
  on_error = 'continue';

```

Remove file from stage
```
remove @employee_stage pattern='.*.csv.gz';
```

Create a table to hold all errors during ingestion (VIDEO 21 8:00)
```
create or replace table employee_errors as 
select * from table(validate(employee, job_id => '019b04c4-0c52-f649-0001-3d6e0002d14e'));
select * from employee_errors
```

Describe file format
```
describe file format employee_csv
```

#### Storage Integration: Bulk Loading from External Source

Notes:

* to verify STORAGE INTEGRATION made it to Azure, go to Azure AAD > Entreprise applications > you should see Snowflake 

* after creating STORAGE INTEGRATION, must authorize Snowflake in Access Control (IAM)
  go to Storage Account > Access Control (IAM) > Add a role assignment > "Storage Blob Data Contributor"
  click +Select Members and search for Snowflake principal described above > Select > Review+Assign

```
SHOW FILE FORMATS
SHOW TABLES
SHOW STAGES

// CLEAN UP
USE ROLE ACCOUNTADMIN ;
DROP INTEGRATION IF EXISTS AZURE_STORAGE ;
DROP FILE FORMAT IF EXISTS CSV_FORMAT ;
DROP STAGE IF EXISTS GTFS ;

```

Step 1: Create Table
```
create or replace table agency(
  agency_id varchar(50), 
  agency_name varchar(50),  
  agency_url varchar(50), 
  agency_timezone varchar(50)
);
```

Step 2: Setup Storage Integration
```
USE ROLE ACCOUNTADMIN ;
CREATE OR REPLACE STORAGE INTEGRATION AZURE_STORAGE
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = AZURE
  ENABLED = TRUE
  AZURE_TENANT_ID = < tenant id >
  STORAGE_ALLOWED_LOCATIONS = ('*') ;
  
GRANT USAGE ON INTEGRATION AZURE_STORAGE TO SYSADMIN ;
  
DESCRIBE STORAGE INTEGRATION AZURE_STORAGE ;
  
USE ROLE SYSADMIN ; -- De-esclate the role
```

Step 3: Setup File Format

```
create or replace file format csv_format
  type = 'CSV'
  field_delimiter = ','
  skip_header = 1
  null_if = ('NULL', 'null')
  empty_field_as_null = TRUE
  compression = gzip ;
```  

Step 4: Set up Stage
```
create or replace stage gtfs
  storage_integration = AZURE_STORAGE
  url = 'azure://<container_name>.blob.core.windows.net/gtfs '
  file_format = CSV_FORMAT ;
```
  
Note: it can take an hour or two for Azure to create objects necessary for the integration
```
list @gtfs ;
```


