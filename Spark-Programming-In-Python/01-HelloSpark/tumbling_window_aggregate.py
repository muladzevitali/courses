from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_timestamp, expr, window, sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from lib.logger import Log4j

spark = SparkSession \
    .builder \
    .appName("Streaming word count") \
    .master("local[3]") \
    .config("spark.streaming.stopGracefullyOnShutdown", "true") \
    .getOrCreate()

logger = Log4j(spark)

stock_schema = StructType([
    StructField("CreatedTime", StringType()),
    StructField("Type", StringType()),
    StructField("Amount", IntegerType()),
    StructField("BrokerCode", StringType())
]
)

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "trades") \
    .option("startingOffsets", "earliest") \
    .load()

value_df = kafka_df.select(from_json(col("value").cast("string"), stock_schema).alias("value"))
trade_df = value_df.select("value.*") \
    .withColumn("CreatedTime", to_timestamp(col("CreatedTime"), "yyyy:MM:dd HH:mm:ss")) \
    .withColumn("Buy", expr("case when type == 'BUY' then Amount else 0 end")) \
    .withColumn("Sell", expr("case when type == 'Sell' then Amount else 0 end"))

window_agg_df = trade_df \
    .groupBy(window(col("CreatedTime"), "15 minute")) \
    .agg(sum("Buy").alias("TotalBuy"), sum("Sell").alias("TotalSell"))

query = window_agg_df.writeStream \
    .format("console") \
    .outputMode("update") \
    .option("checkpointLocation", "checkpoint-dir") \
    .trigger(processingTime="1 minute") \
    .start()

logger.info("Waiting for query")
query.awaitTermination()
