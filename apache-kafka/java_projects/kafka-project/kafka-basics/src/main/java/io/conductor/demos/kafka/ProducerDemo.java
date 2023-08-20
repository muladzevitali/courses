package io.conductor.demos.kafka;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemo {
    private static final Logger log = LoggerFactory.getLogger(ProducerDemo.class.getSimpleName());

    public static void main(String[] args) {
        log.info("I am a Kafka producer");
        //create producer properties
        Properties properties = new Properties();

        properties.setProperty("bootstrap.servers", "cluster.playground.cdkt.io:9092");
        properties.setProperty("security.protocol", "SASL_SSL");
        properties.setProperty("sasl.jaas.config", "org.apache.kafka.common.security.plain.PlainLoginModule required username=\"6B0y336cf6jOs7YP2ZvADB\" password=\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29uZHVrdG9yLmlvIiwic291cmNlQXBwbGljYXRpb24iOiJhZG1pbiIsInVzZXJNYWlsIjpudWxsLCJwYXlsb2FkIjp7InZhbGlkRm9yVXNlcm5hbWUiOiI2QjB5MzM2Y2Y2ak9zN1lQMlp2QURCIiwib3JnYW5pemF0aW9uSWQiOjc0NzI4LCJ1c2VySWQiOjg2OTQ4LCJmb3JFeHBpcmF0aW9uQ2hlY2siOiI4ZWFhNmFmYi0wODIyLTQxNDAtYjMxNi0wYjk3MTUwNWU3ZGUifX0.FMs5w7F5AySGH-p5ieJ-sWqNmaXWZ_8rkpvTbSu0as4\";");
        properties.setProperty("sasl.mechanism", "PLAIN");

        properties.setProperty("key.serializer", StringSerializer.class.getName());
        properties.setProperty("value.serializer", StringSerializer.class.getName());

        // create producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        // create producer record
        ProducerRecord<String, String> producerRecord = new ProducerRecord<>("demo_java", "key", "hello world");
        //send data
        producer.send(producerRecord);
        producer.flush();
        producer.close();
    }
}
