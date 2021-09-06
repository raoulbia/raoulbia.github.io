Title: Kafka Cheatsheet
Date: 2017-11-24
Category: Kafka
Slug: kafka
Summary: Kafka 


#### Start Zookeeper and Kafka

```
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```

#### Topics

* `kafka-topics.sh --create --topic "my-first-topic" --partitions 1 --replication-factor 1 --zookeeper localhost:2181`
* `kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list`


#### Producers

* `kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092 --topic first_topic`


#### Consumers

* `kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic first_topic --from-beginning`
