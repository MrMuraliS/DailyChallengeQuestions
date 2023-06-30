from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, when, col
from pyspark.sql.window import Window

# Define the source file path
source_file = "path/to/source/file.csv"

# Define the target table name
target_table = "your_target_table"

# Define the audit column names
effective_date_column = "effective_date"
end_date_column = "end_date"
is_current_column = "is_current"

# Create a Spark session
spark = SparkSession.builder.getOrCreate()

# Read data from different source formats
data = spark.read.format("csv").option("header", "true").load(source_file)

# Add the audit columns
data = data.withColumn(effective_date_column, current_timestamp())
data = data.withColumn(end_date_column, lit("9999-12-31"))
data = data.withColumn(is_current_column, lit(True))

# Define the window specification for the SCD2 logic
window_spec = Window.partitionBy("id").orderBy(col(effective_date_column).desc())

# Determine the end_date and is_current values for each record
data = data.withColumn(
    end_date_column,
    when(col(end_date_column).isNull(), current_timestamp()).otherwise(
        col(end_date_column)
    ),
)
data = data.withColumn(
    is_current_column,
    when(col(end_date_column) == "9999-12-31", lit(True)).otherwise(lit(False)),
)

# Create a temporary view for the existing data
existing_data = (
    spark.read.format("jdbc")
    .option("url", "jdbc:postgresql://your_database_url")
    .option("dbtable", target_table)
    .option("user", "your_username")
    .option("password", "your_password")
    .load()
)
existing_data.createOrReplaceTempView("existing_data")

# Update the end_date for existing records
update_query = """
    UPDATE {target_table}
    SET {end_date_column} = CURRENT_TIMESTAMP, {is_current_column} = FALSE
    WHERE {target_table}.id IN (
        SELECT e.id
        FROM existing_data e
        LEFT JOIN {target_table} t ON e.id = t.id
        WHERE t.id IS NOT NULL
    )
""".format(
    target_table=target_table,
    end_date_column=end_date_column,
    is_current_column=is_current_column,
)

spark.sql(update_query)

# Insert the new data into the table
data.write.format("jdbc").option("url", "jdbc:postgresql://your_database_url").option(
    "dbtable", target_table
).option("user", "your_username").option("password", "your_password").mode(
    "append"
).save()

print("Data processed successfully.")
