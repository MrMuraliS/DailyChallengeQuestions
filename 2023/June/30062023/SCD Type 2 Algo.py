from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, when, col, row_number
from pyspark.sql.window import Window

# Define the source file path
source_file = "new.csv"

# Define the target table name
target_table = "Address.csv"

# Define the audit column names
EffectiveStartDate = "EffectiveStartDate"
EffectiveEndDate = "EffectiveEndDate"
CurrentFlag = "CurrentFlag"

# Create a Spark session
spark = SparkSession.builder.getOrCreate()

# Read data from different source formats
data = spark.read.format("csv").option("header", "true").load(source_file)

# Add the audit columns
data = data.withColumn(EffectiveStartDate, current_timestamp())
data = data.withColumn(EffectiveEndDate, lit("9999-12-31"))
data = data.withColumn(CurrentFlag, lit("Y"))

# Define the window specification for the SCD2 logic
window_spec = Window.partitionBy("CustomerID").orderBy(col(EffectiveStartDate).desc())

# Determine the end_date and is_current values for each record
data = data.withColumn("rank", row_number().over(window_spec))
data = data.withColumn(
    EffectiveEndDate,
    when(col("rank") == 1, lit("9999-12-31")).otherwise(current_timestamp()),
)
data = data.withColumn(
    CurrentFlag, when(col("rank") == 1, lit("Y")).otherwise(lit("N"))
)
data = data.drop("rank")

data.show(truncate=False)
