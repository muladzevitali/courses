from pyspark.sql import SparkSession

from lib.logger import Log4j

spark = SparkSession \
    .builder \
    .appName("Streaming word count") \
    .master("local[3]") \
    .config("spark.streaming.stopGracefullyOnShutdown", "true") \
    .config("spark.sql.shuffle.partitions", 3) \
    .config("spark.sql.streaming.schemInference", "true") \
    .getOrCreate()

logger = Log4j(spark)

raw_df = spark \
    .readStream \
    .format("json") \
    .option("path", "input") \
    .option("maxFilesPerTrigger", "10") \
    .option("cleanSource", "delete") \
    .load()

# raw_df.printSchema()
explode_df = raw_df.selectExpr("1", "2")

invoice_writer_query = explode_df.writeStream \
    .format("json") \
    .option("checkpointLocation", "checkpoint-dir") \
    .outputMode("append") \
    .queryName("Flattened Invoice writer") \
    .trigger(processingTime="1 minute") \
    .start()

invoice_writer_query.awaitTermination()
