from pyspark.sql import SparkSession
spark = SparkSession.builder \
  .appName('1.1. BigQuery Storage & Spark DataFrames - Python')\
  .config('spark.jars', 'gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar') \
  .getOrCreate()
project="data-engineering-383515"
df = spark.read \
  .format("bigquery") \
  .option('table', 'data-engineering-383515.test.student') \
  .load()
