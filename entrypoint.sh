FROM python:3.11-slim

# Install Java (PySpark needs a JVM)
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Workdir inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code (including src/)
COPY src ./src

# No entrypoint.sh, just call Python directly
ENTRYPOINT ["python", "src/process_data.py"]
