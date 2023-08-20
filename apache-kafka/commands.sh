# 7_36  Kafka topics
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --create --topic firstTopic;
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --create --topic secondTopic --partitions 5;
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --create --topic thirdTopic --replication-factor 2;
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic thirdTopic --describe;
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic first_topic --delete;

# 7_37 Kafka producer
kafka-console-producer.sh --producer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstTopic
> Hello world
> My name is vitali
> I love kafka;
kafka-console-producer.sh --producer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstTopic --producer-property acks=all;
kafka-console-producer.sh --producer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic newTopic;
kafka-console-producer.sh --producer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstTopic --property parse.key=true --property key.separator=:;

# 7_38 Kafka consumer
kafka-topics.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --create --partitions 3;
kafka-console-consumer.sh -consumer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic demo_java;
kafka-console-producer.sh --producer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --producer-property partitioner.class=org.apache.kafka.clients.producer.RoundRobinPartitioner;
kafka-console-consumer.sh -consumer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --from-beginning;
kafka-console-consumer.sh -consumer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --from-beginning --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --property print.partition=true;

# 7_39 Kafka consumer group
kafka-console-consumer.sh -consumer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --group myFirstApplication;
kafka-console-consumer.sh -consumer.config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --topic firstConsumerTopic --group myFirstApplication;

# 7_40 Kafka consumer groups cli
kafka-consumer-groups.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --list;
kafka-consumer-groups.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --describe --group myFirstApplication;

# 7_41 Kafka consumer groups reset offset
kafka-consumer-groups.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --describe --group myFirstApplication;
kafka-consumer-groups.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --group myFirstApplication --reset-offsets --to-earliest --topic firstConsumerTopic --dry-run;
kafka-consumer-groups.sh --command-config 7_playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --group myFirstApplication --reset-offsets --to-earliest --topic firstConsumerTopic --execute;
