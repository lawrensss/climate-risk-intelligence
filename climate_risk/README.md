\# Global Climate Risk \& Economic Impact Intelligence System



A complete end-to-end data analytics pipeline that connects

NASA climate data with World Bank economic indicators to

reveal which regions face the highest climate-driven economic risk.



\---



\## Project Structure

climate\_risk/

├── config/          # Data source configuration

├── data/

│   ├── raw/         # Downloaded API data

│   ├── processed/   # Cleaned data

│   └── colab/       # Exported CSVs for analysis

├── pipeline/

│   ├── ingest.py    # Downloads data from APIs

│   ├── transform.py # Cleans and enriches data

│   ├── db.py        # Loads into SQLite database

│   └── run\_pipeline.py # Runs all stages in order

└── logs/            # Pipeline logs



\---



\## Tools Used



| Tool | Purpose |

|------|---------|

| Python | Data pipeline and automation |

| SQLite | Local data warehouse |

| Google Colab | Exploratory analysis and charts |

| Power BI | Interactive executive dashboard |



\---



\## Data Sources



| Source | Data | Years |

|--------|------|-------|

| NASA GISTEMP | Global temperature anomalies | 1880–2025 |

| World Bank API | GDP, population, agriculture | 1970–2025 |



\---



\## How To Run



\*\*1. Clone the repo\*\*

git clone https://github.com/yourusername/climate\_risk.git

cd climate\_risk



\*\*2. Create virtual environment\*\*

python -m venv .venv

.venv\\Scripts\\activate



\*\*3. Install dependencies\*\*

pip install requests pandas pyarrow pyyaml numpy openpyxl



\*\*4. Run the full pipeline\*\*

python pipeline/run\_pipeline.py



\*\*5. Open the dashboard\*\*

Open climate\_risk\_dashboard.pbix in Power BI Desktop



\---



\## Key Findings



\- 2024 was the hottest year on record at 1.29°C above baseline

\- Only 5 years have crossed the dangerous 1.0°C threshold

&#x20; and all are between 2016 and 2025

\- The most agriculture dependent regions have the lowest GDP

&#x20; making them most vulnerable to climate shocks

\- The 10 year rolling average shows an unbroken warming trend

&#x20; since the late 1970s



\---



\## Pipeline Architecture

NASA API ──────┐

├──► ingest.py ──► transform.py ──► db.py ──► Power BI

World Bank API ┘                                      │

└──► Colab



\---



\## Interview Design Decisions



\*\*Why SQLite?\*\*

Zero infrastructure, single file database that connects

directly to Power BI without a server. At scale this

would swap to PostgreSQL by changing one connection string.



\*\*Why separate ingest and transform?\*\*

Keeps raw data untouched so any transform bug can be

fixed and rerun without hitting the API again.



\*\*Why parquet for intermediate files?\*\*

Parquet is columnar and compressed — 10x smaller than

CSV and much faster to read in pandas.



\*\*Why a rolling 10 year average?\*\*

Single year anomalies are noisy. The rolling average

reveals the true long term trend clearly in Power BI.



\---



\## Author



Lawrence

Data Analyst Portfolio Project

2026

