# Big Data Project: Distributed Console War Analytics

## Project Overview

This project analyzes video game sales and market trends using a Big Data pipeline built with **Python**, **PySpark**, and **Docker**. The analysis compares PlayStation performance against global market trends to answer key research questions about the gaming industry.

**Research Questions:**
- How can we use predictive analytics to forecast PlayStation sales and identify market winners?
- What are the performance differences between PlayStation and the overall gaming market in terms of genres and regional sales?

---

## Project Workflow

### Module 1: Data Collection & Ingestion

Automate downloading datasets and store them for processing.

**Tasks:**
- Choose 2+ public datasets (Kaggle, Data.gov, WHO, World Bank, UCI, etc.)
- Write Python script to fetch datasets dynamically (URLs, APIs, Kaggle datasets)
- Store raw datasets in `data/raw/`
- Optional: convert datasets to Parquet for efficient storage
- Docker container ensures uniform data collection environment

**Deliverables:**
- `Dockerfile` + `requirements.txt`
- Scripts in `src/` (e.g., `fetch_data.py`)
- `data/raw/` populated when container runs

---

### Module 2: Data Cleaning & Integration

Prepare raw data for analysis using PySpark.

**Tasks:**
- Load raw datasets into PySpark
- Handle missing values, inconsistent formats, duplicates
- Merge, join or aggregate datasets as required
- Store processed data in `data/processed/`
- Docker container ensures reproducible cleaning pipeline

**Deliverables:**
- `Dockerfile` + `requirements.txt` for cleaning
- Scripts in `src/` (e.g., `clean_data.py`)
- `data/processed/` ready for analysis

---

### Module 3: Data Analysis & Visualization

Explore and analyze cleaned datasets to answer research questions.

**Tasks:**
- Load processed data in Jupyter Notebook
- Perform descriptive statistics, correlations, aggregations
- Apply regression or other appropriate analysis methods
- Visualize using Matplotlib, Seaborn, or Plotly
- Document findings and interpretations in notebook cells

**Deliverables:**
- Jupyter Notebook(s) in `/notebooks/`
- Plots and charts illustrating key insights
- Problem statement, explanation and conclusion in README.md

---

## Technologies

| Technology | Purpose |
| :--- | :--- |
| **Python** | Primary programming language for scripting and analysis |
| **PySpark** | Distributed computing for large-scale data processing |
| **Docker** | Reproducible environment for data collection and processing |
| **Pandas & NumPy** | Data manipulation and array operations |
| **KaggleHub** | Fetching datasets from Kaggle |
| **Matplotlib, Seaborn, Plotly** | Data visualization |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mca-lab/harsh_BigDataProject.git
cd harsh_BigDataProject
```

### 2. Build and Run with Docker

```bash
# Build the Docker image
docker build -t bigdata-project .

# Run the container
docker run --rm -v "$(pwd)/data:/app/data" bigdata-project
```

### 3. Run Analysis Locally

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

---

## Git Configuration

To maintain a clean repository:

- Use `.gitignore` to exclude large files, cache, and unnecessary folders
- **DO NOT** commit raw or processed datasets (`data/raw/`, `data/processed/`)
- **DO NOT** commit Python cache (`__pycache__`), notebook checkpoints (`.ipynb_checkpoints`), or virtual environments
- **ONLY** commit scripts, notebooks, Docker setup, and README.md

---

## Notes

- Modules 1 and 2 require Docker for reproducibility
- Module 3 is executed in Jupyter Notebook (no Docker required)
- End goal: automated pipeline from data fetching → cleaning → analysis → insights


