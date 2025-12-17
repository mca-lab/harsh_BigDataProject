# Big Data Project: Distributed Console War Analytics

## Project Overview

This project analyzes video game sales and market trends using a Big Data pipeline built with **Python**, **PySpark**, and **Docker**. The analysis compares PlayStation performance against global market trends to answer key research questions about the gaming industry.

**Research Questions:**
- How can we use predictive analytics to analyze PlayStation sales and identify market winners?
- What are the performance differences between PlayStation and the overall gaming market in terms of genres and regional sales?

---

## Project Workflow

### Module 1: Data Collection & Ingestion

Automate downloading datasets and store them for processing.

**Tasks:**
- Choosed 2 public dataset from kaggle
  -PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv from gvidalguiresse/playstation-sales-and-metadata-ps3ps4ps5
  -video_game_reviews.csv from jahnavipaliwal/video-game-reviews-and-ratings
- Wrote a Python script to fetch datasets dynamically via Kaggle API
- Stored raw datasets in `data/raw/`
- Docker container ensures uniform data collection environment
### 2. Build and Run with Docker

```bash
# Build the Docker image
docker build -t bigdata-project .

# Run the container
docker run --rm -v "$(pwd)/data:/app/data" bigdata-project
```
---

### Module 2: Data Cleaning & Integration

Prepare raw data for analysis using PySpark.

**Tasks performed:**
- Loaded raw datasets into PySpark
- Handled missing values, inconsistent formats, duplicates
- Merge, join or aggregate datasets as required
- Store processed data in `data/processed/`
- Docker container ensures reproducible cleaning pipeline
---

### Module 3: Data Analysis & Visualization

Explored and analyzed cleaned datasets to answer research questions.

**Tasks:**
- Loaded processed data in Jupyter Notebook
- Performed descriptive statistics, correlations, aggregations
- Visualized using Matplotlib, Seaborn, or Plotly
- Documented findings and interpretations in notebook cells


---

## Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Primary programming language for scripting and analysis |
| **PySpark** | Distributed computing for large-scale data processing |
| **Docker** | Reproducible environment for data collection and processing |
| **Pandas & NumPy** | Data manipulation and array operations |
| **KaggleHub** | Fetching datasets from Kaggle |
| **Matplotlib, Seaborn, Plotly** | Data visualization |

---

## To Run project

### 1. Clone the Repository

```bash
git clone https://github.com/mca-lab/harsh_BigDataProject.git
cd harsh_BigDataProject
```


### 2. To Run Analysis Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Start Jupyter Notebook
jupyter notebook notebooks/analyze.ipynb
```

---

## Project Structure

```
harsh_BigDataProject/
├── src/
│   ├── fetch_data.py          # Data ingestion script
│   ├── process_data.py        # Data cleaning and processing
│   └── analyze.ipynb          # Analysis and visualization
├── data/
│   ├── raw/                   # Raw datasets
│   └── processed/             # Processed datasets
├── notebooks/                 # Jupyter notebooks
├── dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies
├── entrypoint.sh             # Container entry script
└── README.md                 # This file
```





