import sys
import boto3
import json
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, count, when
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue and Spark
spark = SparkSession.builder.appName("DataQualityETL").getOrCreate()
glueContext = GlueContext(spark)
s3_client = boto3.client("s3")

# Parameters
SOURCE_BUCKET = "source-data-bucket"
FAILED_BUCKET = "failed-data-bucket"
PROCESSED_BUCKET = "processed-data-bucket"
DATA_KEY = "input_data.csv"

# Read data
input_df = spark.read.option("header", "true").csv(f"s3://{SOURCE_BUCKET}/{DATA_KEY}")

# Data Quality Checks
unique_check = input_df.select(countDistinct("id")).collect()[0][0] == input_df.count()
completeness_check = input_df.select([count(when(col(c).isNull(), c)).alias(c) for c in input_df.columns])
freshness_check = input_df.filter(col("timestamp") > '2024-01-01').count() > 0

# Classify data
if unique_check and freshness_check and completeness_check.rdd.flatMap(lambda x: x).sum() == 0:
    input_df.write.mode("overwrite").csv(f"s3://{PROCESSED_BUCKET}/processed_data.csv")
else:
    input_df.write.mode("overwrite").csv(f"s3://{FAILED_BUCKET}/failed_data.csv")

# Notify
sns_client = boto3.client("sns")
sns_client.publish(TopicArn='arn:aws:sns:region:account-id:topic-name',
                   Message='Data Quality Check Completed.',
                   Subject='AWS Glue Data Quality Report')

print("ETL Process Completed.")
