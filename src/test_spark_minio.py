from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SmartSupply-MinIO-Test")
    .config(
        "spark.hadoop.fs.s3a.endpoint",
        "http://minio:9000"
    )
    .config(
        "spark.hadoop.fs.s3a.access.key",
        "minioadmin"
    )
    .config(
        "spark.hadoop.fs.s3a.secret.key",
        "minioadmin_password"
    )
    .config(
        "spark.hadoop.fs.s3a.path.style.access",
        "true"
    )
    .config(
        "spark.hadoop.fs.s3a.connection.ssl.enabled",
        "false"
    )
    .config(
        "spark.hadoop.fs.s3a.impl",
        "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    .getOrCreate()
)

print("======================================")
print(" SmartSupply - Spark + MinIO Test")
print("======================================")

data = [
    ("P001", "Laptop", 10, 999.99),
    ("P002", "Keyboard", 25, 49.99),
    ("P003", "Mouse", 50, 19.99),
]

df = spark.createDataFrame(
    data,
    ["product_id", "product_name", "quantity", "unit_price"]
)

print("\n--- DataFrame ---")
df.show()

print("\n--- Writing to MinIO ---")

output_path = "s3a://smartsupply-bronze/test/products"

df.write.mode("overwrite").parquet(output_path)

print(f"Data written to: {output_path}")

print("\n--- Reading from MinIO ---")

df_read = spark.read.parquet(output_path)

df_read.show()

print("\nNumber of rows:", df_read.count())

print("\n======================================")
print(" SPARK + MINIO TEST SUCCESS")
print("======================================")

spark.stop()