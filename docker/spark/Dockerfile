FROM apache/spark:3.5.2-python3

USER root

# ============================================================
# System dependencies
# ============================================================

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        wget \
        python3-pip \
        procps \
        && \
    rm -rf /var/lib/apt/lists/*


# ============================================================
# Python dependencies
# ============================================================

RUN pip3 install --no-cache-dir \
    pandas \
    numpy \
    scikit-learn \
    xgboost \
    lightgbm \
    shap \
    optuna \
    ortools \
    mlflow \
    boto3 \
    s3fs \
    requests \
    python-dotenv


# ============================================================
# Spark / Hudi / S3A dependencies
# ============================================================

RUN mkdir -p /opt/spark/jars

RUN wget -q \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
    -O /opt/spark/jars/hadoop-aws-3.3.4.jar

RUN wget -q \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar \
    -O /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar

RUN wget -q \
    https://repo1.maven.org/maven2/org/apache/hudi/hudi-spark3.5-bundle_2.12/0.15.0/hudi-spark3.5-bundle_2.12-0.15.0.jar \
    -O /opt/spark/jars/hudi-spark3.5-bundle_2.12-0.15.0.jar


# ============================================================
# SmartSupply directories
# ============================================================

RUN mkdir -p \
    /opt/spark/src \
    /opt/spark/data \
    /opt/spark/notebooks \
    /opt/spark/jobs

WORKDIR /opt/spark

# ============================================================
# Python path
# ============================================================

ENV PYTHONPATH=/opt/spark:/opt/spark/src

ENV PYSPARK_PYTHON=python3

ENV PYSPARK_DRIVER_PYTHON=python3

# ============================================================
# Permissions
# ============================================================

RUN chmod -R 755 /opt/spark

USER 185