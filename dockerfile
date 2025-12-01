# Use bookworm so we can install Java 17
FROM python:3.11-slim-bookworm

# Install Java (required by PySpark / Spark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre-headless && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Workdir inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code and entrypoint
COPY src/ ./src
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Default entrypoint: runs fetch_data.py (if exists) then process_data.py
ENTRYPOINT ["/entrypoint.sh"]
