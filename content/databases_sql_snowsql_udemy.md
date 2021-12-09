Title: SnowSQL Cheatsheet
Date: 2017-11-23
Category: Databases
Slug: snowsql_udemy
Summary: SnowSQL Udemy
Status: draft

```
-- Create the Employee table
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

```
-- Some Employee queries
select * From Public.Employee
drop table Employee
truncate table Employee
```

```
-- Create a File Format Object
create or replace file format employee_csv
  type = 'CSV'
  field_delimiter = ','
  skip_header = 1;
```

```
-- Create an internal Stage object
create or replace stage employee_stage
  file_format = employee_csv;
```

```
-- Display the stages we have created
show stages
```

```
-- See what's in the employee_stage
list @employee_stage;
```

```
-- Move the data in employee_stage to the employee table. Skip the entire file on any errors
copy into employee
  from @employee_stage
  on_error = 'skip_file';
```


```
-- Move the data in employee_stage to the employee table. Skip just the rows causing any errors
copy into employee
  from @employee_stage
  on_error = 'continue';

```
-- Remove file from stage
remove @employee_stage pattern='.*.csv.gz';
```

```
-- Create a table to hold all errors during ingestion (VIDEO 21 8:00)
create or replace table employee_errors as 
select * from table(validate(employee, job_id => '019b04c4-0c52-f649-0001-3d6e0002d14e'));
select * from employee_errors
```

```
describe file format employee_csv
```

