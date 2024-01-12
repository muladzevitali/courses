from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col

from lib.logger import Log4j

spark = SparkSession \
    .builder \
    .appName("Streaming word count") \
    .master("local[3]") \
    .config("spark.streaming.stopGracefullyOnShutdown", "true") \
    .getOrCreate()

logger = Log4j(spark)

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "invoices") \
    .option("startingOffsets", "earliest") \
    .load()

# kafka_df.printSchema()
value_df = kafka_df.select(from_json(col("value").cast("string"), schema=""))
explode_df = value_df.selectExpr("value.InvoiceNumber", "explode(value.InvoiceLineItems) as LineItem")

invoice_writer_query = explode_df.writeStream \
    .format("json") \
    .option("checkpointLocation", "checkpoint-dir") \
    .outputMode("append") \
    .queryName("Flattened Invoice writer") \
    .trigger(processingTime="1 minute") \
    .start()

invoice_writer_query.awaitTermination()
