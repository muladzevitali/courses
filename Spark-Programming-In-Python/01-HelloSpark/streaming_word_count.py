from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

from lib.logger import Log4j

spark = SparkSession \
    .builder \
    .appName("Streaming word count") \
    .master("local[3]") \
    .config("spark.streaming.stopGracefullyOnShutdown", "true") \
    .config("spark.sql.shuffle.partitions", 3) \
    .getOrCreate()

logger = Log4j(spark)

lines_df = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", "9999") \
    .load()

# lines_df.printSchema()
words_df = lines_df.select(expr("explode(split(value, ' ')) as word"))
counts_df = words_df.groupBy("word").count()

word_count_query = counts_df.writeStream \
    .format("console") \
    .option("checkpointLocation", "checkpoint-dir") \
    .outputMode("complete") \
    .start()

logger.info("Listening to localhost:9999")
word_count_query.awaitTermination()
