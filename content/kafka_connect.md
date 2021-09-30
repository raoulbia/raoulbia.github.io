Title: Kafka Connect Cheatsheet
Date: 2017-11-23
Category: Kafka
Slug: kafka_connect
Summary: Kafka Connect Cheatsheet


### Connectors

In this demonstration we're going to make use of the Kafka Connect API.

[See the documentation for more information on any of these actions](https://docs.confluent.io/current/connect/references/restapi.html).


To get a list of connectors that are loaded in to the Kafka Connect cluster

```
curl http://localhost:8083/connector-plugins | python -m json.tool
```



#### Viewing Connectors

First, we can view connector-plugins:

```bash
curl http://localhost:8083/connector-plugins | python -m json.tool
```

#### Create a Connector

Lets create a connector. We'll dive into more details on how this works later.

```bash
curl -X POST -H 'Content-Type: application/json' -d '{
    "name": "first-connector",
    "config": {
        "connector.class": "FileStreamSource",
        "tasks.max": 1,
        "file": "/var/log/journal/confluent-kafka-connect.service.log",
        "topic": "kafka-connect-logs"
    }
  }' \
  http://localhost:8083/connectors
```

#### List connectors

We can list all configured connectors with:

```bash
curl http://localhost:8083/connectors | python -m json.tool
```

You can see our connector in the list.

#### Detailing connectors

Let's list details on our connector:

```bash
curl http://localhost:8083/connectors/first-connector | python -m json.tool
```

#### Pausing connectors

Sometimes its desirable to pause or restart connectors:

To view status:

```bash
curl http://localhost:8083/connectors/first-connector/status | python -m json.tool
```

To pause:

```bash
curl -X PUT http://localhost:8083/connectors/first-connector/pause 
```

To restart (note this is a POST command!):

```bash
curl -X POST http://localhost:8083/connectors/first-connector/restart
```

#### Deleting connectors

Finally, to delete your connector:

```bash
curl -X DELETE http://localhost:8083/connectors/first-connector
```
