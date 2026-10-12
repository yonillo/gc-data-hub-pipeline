# ⛽ Gran Canaria Fuel Data Pipeline (ETL)

[![GC Fuel Data Pipeline](https://github.com/yonillo/gc-data-hub-pipeline/actions/workflows/main.yml/badge.svg)](https://github.com/yonillo/gc-data-hub-pipeline/actions/workflows/main.yml)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Storage Format](https://img.shields.io/badge/Storage-Apache%20Parquet-orange.svg)](https://parquet.apache.org/)
[![Automation](https://img.shields.io/badge/Orchestration-GitHub%20Actions-2088FF.svg)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)

Automated production Data Engineering (ETL) pipeline that ingests, cleans, analyzes, and persists daily fuel station prices across the province of Las Palmas (Gran Canaria, Spain), with micro-regional price differential analytics focused on **Agaete**.

---

## 🏗️ Architecture & Data Flow

```mermaid
flowchart LR
    A["Government REST API\n(Minetur / MITECO)"] -->|Extract| B["Extraction Module\n(Resilient HTTP & Session)"]
    B -->|Transform| C["Pandas & PyArrow Engine\n(Clean, Cast, Filter Prov 35)"]
    C -->|Analytics| D["Price Metrics\n(Agaete vs Regional Mean)"]
    D -->|Load| E["Columnar Storage\n(/data/*.parquet)"]
    F["GitHub Actions Cron\n(Daily @ 08:00 UTC)"] -.->|Trigger| B
    E -.->|Auto-Commit| G["Versioned Data Lake"]
```

1. **Extract (`src/extract.py`):** Ingests live data from Spain's Ministry of Industry and Energy REST API. Features connection resilience with automated retries and exponential backoff.
2. **Transform (`src/transform.py`):** Cleans decimal encodings, normalizes numeric datatypes, filters geographic records for Las Palmas (`IDProvincia: 35`), and computes comparative variance metrics.
3. **Load (`src/load.py`):** Serializes clean data into **Apache Parquet** columnar format, creating daily snapshots and updating the `latest` pointer.

---

## 💡 Engineering & Business Impact

- **Storage Efficiency:** Migrating from CSV to **Apache Parquet** achieves an **~80% reduction in storage footprint**, maintaining strict columnar schemas and high compression ratios.
- **Zero-Cost Serverless Orchestration:** Daily ingestion scheduled via GitHub Actions cron runners with automated CI/CD push to storage.
- **Fast Analytics:** Downstream query latency reduced by columnar projections and typed schema preservation.

---

## 📂 Repository Structure

```
gc-data-hub-pipeline/
├── .github/workflows/
│   └── main.yml           # Automated daily cron workflow (08:00 UTC)
├── config/
│   └── settings.py        # Pipeline parameters & paths
├── data/
│   ├── fuel_prices_latest.parquet
│   └── fuel_prices_gc_*.parquet
├── src/
│   ├── extract.py         # REST API ingestion & error handling
│   ├── transform.py       # Data cleansing & price transformations
│   ├── load.py            # Apache Parquet serialization
│   ├── main.py            # ETL orchestrator
│   └── utils/
│       └── logger.py      # Structured UTF-8 logging
├── Dockerfile             # Multi-platform container definition
├── requirements.txt       # Pinned production dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Local Setup

```bash
# Clone the repository
git clone https://github.com/yonillo/gc-data-hub-pipeline.git
cd gc-data-hub-pipeline

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python src/main.py
```

### 2. Run with Docker

```bash
# Build the container
docker build -t gc-fuel-pipeline .

# Execute ETL inside container
docker run --rm -v $(pwd)/data:/app/data gc-fuel-pipeline
```

---

## 👨‍💻 Author

**Yone Suárez Viera**  
Data Science & Engineering Student @ ULPGC | Gran Canaria 🏝️  
- **LinkedIn:** [yone-suarez](https://linkedin.com/in/yone-suarez)
- **Portfolio:** [yonesuarez.es](https://yonesuarez.es)
