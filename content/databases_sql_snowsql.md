Title: SnowSQL Cheatsheet
Date: 2017-11-23
Category: Databases
Slug: snowsql
Summary: SnowSQL 


#### config file

config file is located here: `/home/<user>/.snowsql`

In your config file you need to modify this line:

`log_file = ../snowsql_rt.log`

to this:

`log_file = ~/.snowsql/snowsql_rt.log`


#### Useful commands

```
snowsql --accountname 123.north-europe.azure --username <username>
snowsql -c my_connection


```
