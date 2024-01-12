from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr

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
    .load()

# kafka_df.printSchema()
value_df = kafka_df.select(from_json(col("value").cast("string"), schema=_))
notification_df = value_df.select("value.InvoiceNumber", "value.CustomerCardNo", "value.TotalAmount") \
    .withColumn("EarnedPoints", expr("TotalAmount * 0.2"))

kafka_target_df = notification_df.selectExpr("InvoiceNumber as key",
                                             """
                                             to_json(
                                                named_struct(
                                                    'CustomerCardNo', CustomerCardNo
                                                )
                                             ) as value
                                             """)

invoice_writer_query = kafka_target_df.writeStream \
    .queryName("Notification writer") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "notifications") \
    .outputMode("append") \
    .option("checkpointLocation", "checkpoint-dir") \
    .start()
