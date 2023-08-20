package io.conductor.demos.kafka;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.CooperativeStickyAssignor;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.errors.WakeupException;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.time.Duration;
import java.util.Arrays;
import java.util.Properties;

public class ConsumerDemoWithShutdown {
    private static final Logger log = LoggerFactory.getLogger(ConsumerDemoWithShutdown.class.getSimpleName());

    public static void main(String[] args) {
        log.info("I am a Kafka consumer");
        String groupID = "my-java-application";
        String topic = "demo_java";
        //create producer properties
        Properties properties = new Properties();

        properties.setProperty("bootstrap.servers", "cluster.playground.cdkt.io:9092");
        properties.setProperty("security.protocol", "SASL_SSL");
        properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"6B0y336cf6jOs7YP2ZvADB\" password=\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29uZHVrdG9yLmlvIiwic291cmNlQXBwbGljYXRpb24iOiJhZG1pbiIsInVzZXJNYWlsIjpudWxsLCJwYXlsb2FkIjp7InZhbGlkRm9yVXNlcm5hbWUiOiI2QjB5MzM2Y2Y2ak9zN1lQMlp2QURCIiwib3JnYW5pemF0aW9uSWQiOjc0NzI4LCJ1c2VySWQiOjg2OTQ4LCJmb3JFeHBpcmF0aW9uQ2hlY2siOiI4ZWFhNmFmYi0wODIyLTQxNDAtYjMxNi0wYjk3MTUwNWU3ZGUifX0.FMs5w7F5AySGH-p5ieJ-sWqNmaXWZ_8rkpvTbSu0as4\";");
        properties.setProperty("sasl.mechanism", "PLAIN");

        // create consumer configs
        properties.setProperty("key.deserializer", StringDeserializer.class.getName());
        properties.setProperty("value.deserializer", StringDeserializer.class.getName());

        properties.setProperty("group.id", groupID);
        properties.setProperty("auto.offset.reset", "earliest");
        properties.setProperty("partition.assignment.strategy", CooperativeStickyAssignor.class.getName());

        // create consumer
        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(properties);

        // get a reference to the main thread
        final Thread mainThread = Thread.currentThread();
        Runtime.getRuntime().addShutdownHook(new Thread() {
            public void run() {
                log.info("detected a shutdown, let's exist by caling consumer.wakeup()");
                consumer.wakeup();
                try {
                    mainThread.join();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        try {
            // subscribe to a topic
            consumer.subscribe(Arrays.asList(topic));
            // poll for data

            while (true) {
                ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(1000));
                for (ConsumerRecord<String, String> record : records) {
                    log.info(String.format("Key: %s, Value: %s, Partition: %s, Offset: %s", record.key(), record.value(), record.partition(), record.offset()));
                }
            }
        } catch (WakeupException e) {
            log.info("consumer is starting to shut down");
        } catch (Exception e) {
            log.info("unexpected exception");
        } finally {
            consumer.close();
            log.info("the consumer is now gracefully shutdown");
        }


    }
}
