Title: Kafka Cheatsheet
Date: 2017-11-24
Category: Kafka
Slug: kafka
Summary: Kafka 

### Terminology 

* A Kafka cluster is a group of Kafka brokers.
* A Kafka broker allows consumers to fetch messages by topic, partition and offset.
* Kafka brokers can create a Kafka cluster by sharing information between each other directly or indirectly using Zookeeper.

### Installation

* Download and Setup Java 8 JDK: `sudo apt install openjdk-8-jdk`

* Download & Extract the Kafka binaries from https://kafka.apache.org/downloads

* Try Kafka commands using bin/kafka-topics.sh (for example)

* add to `~/.bashrc`:  `export PATH=/home/vagrant/kafka_2.12-2.8.0/bin:$PATH`

* Edit Zookeeper & Kafka configs in `kafka_2.12-2.8.0/config`

	* zookeeper.properties: `dataDir=/home/vagrant/kafka_2.12-2.8.0/data/zookeeper`

	* server.properties: `log.dirs=/home/vagrant/kafka_2.12-2.8.0/data/kafka`


### Start Zookeeper, Kafka Server and Kafka Connect

* Pre-requisite: Kafka aded to PATH
* Only when Zookeeper is up and running you can start a Kafka server (that will connect to Zookeeper).

```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
connect-distributed.sh config/connect-distributed.properties
```

### Topics

```
kafka-topics.sh --zookeeper localhost:2181 --create --topic "gtfs" --partitions 1 --replication-factor 1
kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list
kafka-topics.sh --zookeeper localhost:2181 --delete --topic 'g.*'
kafka-topics.sh --zookeeper localhost:2181 --delete --topic '.*ksql.*'
```



### Producers

```
kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092 --topic topic_name
```

Piping a JSON file into a Topic:

```
file_name.json | kafka-console-producer.sh --bootstrap-server 127.0.0.1:9092 --topic topic_name
```



### Consumers

This tool helps to read data from Kafka topics and outputs it to standard output.

```
kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic first_topic --from-beginning --property print.key=true --property key.separator="-" --property print.timestamp=true
```

### Faust

Note: append -p 6067 to the line below to use a different port.

```bash
$ python script.py worker 
```

### Other Useful Commands

* ```kafka-topics.sh --bootstrap-server 127.0.0.1:9092 --list```
* ``` kafka-consumer-groups.sh  --list --bootstrap-server localhost:9092```
* ```zookeeper-shell.sh localhost:2181 ls /brokers/ids``` to list active brokers. 
