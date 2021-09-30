Title: KSql Cheatsheet
Date: 2017-11-23
Category: KSql
Slug: ksql
Summary: KSql 


### Installation

* Download and Setup Java 8 JDK: `sudo apt install openjdk-8-jdk`
* wget https://packages.confluent.io/archive/6.2/confluent-6.2.0.tar.gz
* tar -xvf confluent-6.2.0
* `sudo ln -s confluent-6.2.0/ confluent`
* add to `~/.bashrc`:
  * `export  export PATH=/opt/confluent/bin:$PATH` (or where ever the tar has been unzipped to.
  * `export CONFLUENT_HOME=/opt/confluent`


### Start KSql

```bash
confluent local services ksql-server start
confluent local services ksql-server status
```

#### Topics


Note: By default KSql will show only new arriving data.

Use `FROM BEGINNING` to see all existing data AND keep listening for new data.

Also useful for checking that topic has a KEY!!

* `print 'topic_name' FROM BEGINNING LIMIT 1;`



#### auto.offset.reset

By default KSql `select` only shows new incoming data aka `current offset`. 

Must run command below (Only valid for current KSql session! Must re-issue each tme entering KSql prompt).

```
SET 'auto.offset.reset'='earliest' ;
``` 

to reset this setting:

```
UNSET 'auto.offset.reset';
```

#### KSql CREATE TABLE ([KSQL Syntax Reference](https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/create-table/) )

```
create table GTFS_DELAYS_TABLE (id VARCHAR PRMARY KEY, delay INT, timestamp INT) WITH (KAFKA_TOPIC='gtfs-delays', VALUE_FORMAT='JSON') ;
show tables ;
describe GTFS_DELAYS_TABLE ;
```

```bash
create table GTFS_TABLE ( \
id VARCHAR PRIMARY KEY, \
trip_update_trip_trip_id VARCHAR, \
trip_update_trip_start_time VARCHAR, \
trip_update_trip_start_date VARCHAR,\
trip_update_trip_schedule_relationship VARCHAR, \
trip_update_trip_route_id VARCHAR, \
trip_update_stop_time_update_stop_sequence INT, \
trip_update_stop_time_update_departure_delay INT, \
trip_update_stop_time_update_stop_id VARCHAR, \
trip_update_stop_time_update_schedule_relationship VARCHAR, \
trip_update_stop_time_update_arrival_delay INT \
) WITH (KAFKA_TOPIC='GTFS_TOPIC', VALUE_FORMAT='JSON') ;
```

To persist the above table see below. 

```
create table GTFS_TABLE2 AS select * from GTFS_TABLE ;
```

Before terminating a persistent table we must first terminate that query!

```
show queries ;
terminate <query_name> ;
drop table <table_name> ;
```

#### KSql SELECT 

```
select trip_update_trip_trip_id, trip_update_stop_time_update_stop_sequence, trip_update_stop_time_update_departure_delay from GTFS_TABLE emit changes ;
```

```
select trip_update_trip_trip_id, trip_update_stop_time_update_stop_sequence, sum(trip_update_stop_time_update_departure_delay) from GTFS_TABLE group by trip_update_trip_trip_id, trip_update_stop_time_update_stop_sequence emit changes ;
```

#### KSql streams

KSql streams are used to interrogate the underlying data.


```
create stream users_stream (name VARCHAR, countrycode VARCHAR) WITH (KAFKA_TOPIC='USERS', VALUE_FORMAT='DELIMITED') ;
list streams ;
select name, countrycode from users_stream emit changes;
select name, countrycode from users_stream emit changes limit 5;
select countrycode, count(*) from users_stream group by countrycode;
drop stream if exists users_stream ;
drop stream if exists users_stream delete topic ;
```

```
create stream gtfs_delays_stream (id VARCHAR, delay INT, timestamp INT) WITH (KAFKA_TOPIC='gtfs-delays', VALUE_FORMAT='JSON') ;
describe gtfs_delays_stream ;
select TIMESTAMPTOSTRING(rowtime, 'dd/MMM HH:mm') as createtime, * from gtfs_delays_stream emit changes limit 5;
```

```
create stream GTFS_STREAM ( \
id VARCHAR, \
trip_update STRUCT \
	< trip STRUCT \
		< trip_id VARCHAR, start_time VARCHAR, start_date VARCHAR, schedule_relationship VARCHAR, route_id VARCHAR> \
	>,  \
stop_time_update STRUCT < stop_sequence INT, arrival STRUCT < delay INT >, stop_id VARCHAR, schedule_relationship VARCHAR >
) WITH (KAFKA_TOPIC='GTFS_TOPIC', VALUE_FORMAT='JSON') ;

select * from GTFS_STREAM emit changes ;

```



### Other Useful Commands

* ``` kafka-consumer-groups.sh  --list --bootstrap-server localhost:9092```
* ```zookeeper-shell.sh localhost:2181 ls /brokers/ids``` to list active brokers. 
