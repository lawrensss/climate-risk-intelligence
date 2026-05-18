<div align="center">

# 🌍 Climate Risk Intelligence System

### End-to-end data pipeline connecting NASA climate science with World Bank economics

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com)
[![Google Colab](https://img.shields.io/badge/Google_Colab-Analysis-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com)

> **Which regions of the world face the highest climate-driven economic risk?**
> This project answers that question with a fully automated pipeline — from raw API calls to an interactive Power BI dashboard.

---

### 🌡️ 2024 was the hottest year ever recorded at **1.29°C** above baseline &nbsp;|&nbsp; 5 years have now crossed the **1.0°C danger threshold** &nbsp;|&nbsp; The most agriculture-dependent regions have the **lowest GDP**

---

</div>

## 📊 Dashboard Preview

### Page 1 — Climate Overview
![Climate Overview](climate%20overview%20screenshot.png)

### Page 2 — Economic Risk
![Economic Risk](economic%20risk%20screenshot.png)

### Page 3 — Climate vs Economy
![Climate vs Economy](climate%20vs%20economy%20screenshot.png)

---

## ✅ Project Status

| Deliverable | Status |
|-------------|--------|
| Python ingestion pipeline | ✅ Complete |
| SQLite star schema database | ✅ Complete |
| Google Colab analysis notebook | ✅ Complete |
| Power BI 3-page interactive dashboard | ✅ Complete |
| GitHub repository | ✅ Complete |

---

## 📌 What This Project Does

This system automatically:
- **Downloads** real climate and economic data from NASA and World Bank APIs
- **Cleans and transforms** the raw data into analysis-ready tables
- **Loads** everything into a structured SQLite database
- **Analyses** trends and patterns in Google Colab with visualisations
- **Presents** findings in a 3-page interactive Power BI dashboard

---

## 🗂️ Project Structure

```
climate-risk-intelligence/
│
├── 📁 config/
│   └── sources.yaml                     # API endpoints and parameters
│
├── 📁 pipeline/
│   ├── ingest.py                        # Pulls data from NASA + World Bank APIs
│   ├── transform.py                     # Cleans, fills gaps, engineers features
│   ├── db.py                            # Loads star schema into SQLite
│   └── export_for_colab.py              # Exports CSVs for notebook analysis
│
├── 📁 notebooks/
│   └── Climate_Risk_Analysis.ipynb      # Full Colab analysis notebook
│
├── 📁 dashboard/
│   └── climate_risk_dashboard.pbix      # Power BI dashboard file
│
├── 📁 images/
│   ├── climate_overview_screenshot.png
│   ├── economic_risk_screenshot.png
│   └── climate_vs_economy_screenshot.png
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Tool | Why |
|-------|------|-----|
| **Ingestion** | Python `requests` | Retry logic, rate limiting, API handling |
| **Storage (raw)** | Apache Parquet | 10x smaller than CSV, faster reads |
| **Transformation** | `pandas` + `numpy` | Interpolation, feature engineering |
| **Database** | SQLite (star schema) | Zero infrastructure, direct Power BI connection |
| **Analysis** | Google Colab | Reproducible notebooks, free GPU |
| **Visualisation** | Power BI Desktop | Interactive slicers, executive-ready dashboards |

---

## 📊 Data Sources

| Source | What We Get | Coverage |
|--------|-------------|----------|
| [NASA GISTEMP v4](https://data.giss.nasa.gov/gistemp/) | Global surface temperature anomaly vs 1951–1980 baseline | 1880–2025 |
| [World Bank API](https://data.worldbank.org/indicator) | GDP, population, agriculture % of GDP | 1970–2025 |

---

## 🚀 How To Run

### Prerequisites
- Python 3.8+
- Power BI Desktop (free from Microsoft)
- Google account (for Colab)

### Step 1 — Clone and set up

```bash
git clone https://github.com/yourusername/climate-risk-intelligence.git
cd climate-risk-intelligence

python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Mac/Linux

pip install -r requirements.txt
```

### Step 2 — Run the pipeline

```bash
# Download raw data from APIs
python pipeline/ingest.py

# Clean and engineer features
python pipeline/transform.py

# Load into SQLite database
python pipeline/db.py

# Export CSVs for Colab
python pipeline/export_for_colab.py
```

### Step 3 — Explore in Google Colab

Open `notebooks/Climate_Risk_Analysis.ipynb` in Google Colab and run all cells.

### Step 4 — Open the dashboard

Connect Power BI Desktop to `data/climate_risk.db` via ODBC and open `dashboard/climate_risk_dashboard.pbix`.

---

## 📈 Dashboard Pages

| Page | Visuals | Slicer |
|------|---------|--------|
| **Climate Overview** | Temperature trend line, hottest years table, GDP by region bar chart | Anomaly tier |
| **Economic Risk** | GDP over time, population donut, agriculture dependence ranking | Decade |
| **Climate vs Economy** | Temperature by decade, anomaly tier pie, bars + rolling average combo | Anomaly tier |

---

## 🔍 Key Findings

```
🌡️  Hottest year on record  →  2024 at 1.29°C above the 1951–1980 baseline
📈  Years above 1.0°C       →  5 years, ALL between 2016 and 2025
🌾  Most vulnerable regions →  Heavily indebted poor countries (HIPC)
                               highest agriculture dependence, lowest GDP
💰  Wealthiest region       →  Euro area at $46,945 GDP per capita
📉  10yr rolling average    →  Unbroken upward trend since late 1970s
```

---

## 🏗️ Pipeline Architecture

```
                    ┌─────────────────┐
                    │   sources.yaml  │
                    │  (config file)  │
                    └────────┬────────┘
                             │
              ┌──────────────▼──────────────┐
              │         ingest.py           │
              │  NASA GISTEMP + World Bank  │
              │     → data/raw/*.parquet    │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │        transform.py         │
              │  Clean · Fill · Engineer    │
              │  → data/processed/*.parquet │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │           db.py             │
              │   SQLite Star Schema        │
              │   → data/climate_risk.db    │
              └──────┬───────────┬──────────┘
                     │           │
          ┌──────────▼──┐   ┌───▼──────────┐
          │  Power BI   │   │ Google Colab │
          │  Dashboard  │   │   Notebook   │
          └─────────────┘   └─────────────┘
```

---

## 🗄️ Database Schema

```
dim_country          dim_year
───────────          ────────
country_code PK      year PK
country_name         decade
                     is_post_paris

fact_economic                    fact_climate
─────────────                    ────────────
country_code FK                  year PK
year FK                          temp_anomaly_c
gdp_current_usd                  temp_anomaly_rolling10y
gdp_per_capita_usd               anomaly_tier
agriculture_pct_gdp
population
co2_per_capita
```

---

## 💡 Design Decisions

<details>
<summary><b>Why SQLite instead of PostgreSQL?</b></summary>

SQLite is zero-infrastructure — a single `.db` file that connects directly to Power BI via ODBC with no server needed. For this dataset size (under 10MB) it's the right tool. At scale, swapping to PostgreSQL requires changing exactly one connection string in `db.py`.

</details>

<details>
<summary><b>Why separate ingest and transform scripts?</b></summary>

Raw data is saved to `data/raw/` and never modified. Any bug in the transform logic can be fixed and rerun instantly without hitting the APIs again. This is a core data engineering principle — raw data is sacred.

</details>

<details>
<summary><b>Why Parquet instead of CSV for intermediate files?</b></summary>

Parquet is a columnar format — significantly more compressed than CSV and much faster for pandas to read. It also preserves data types exactly, so a float saved as float comes back as float — no type inference surprises.

</details>

<details>
<summary><b>Why a 10-year rolling average for temperature?</b></summary>

Single year anomalies contain natural variation (El Niño, volcanic eruptions). The 10-year rolling average cuts through the noise to show the true long-term warming signal — which is what matters for economic risk assessment.

</details>

<details>
<summary><b>Why regional groups instead of individual countries?</b></summary>

The free World Bank API returns clean, complete data for regional aggregates. Individual country data has significant gaps (some countries missing 10–20 years) that would require imputation strategies — a planned Phase 2 enhancement.

</details>

---

## 🔮 Phase 2 — Coming Next

This project is actively being expanded. Phase 2 will add:

### 🌪️ New Data Source — EM-DAT Disaster Database
Connecting real disaster event records (floods, droughts, storms)
to economic loss figures — quantifying exactly how much each
disaster type costs each region in USD.

### 🤖 Machine Learning — Climate Risk Score
Building a country-level risk score (0–100) using XGBoost
with SHAP explainability — so every score can be broken down
into exactly which factors drove it up or down.

### 🗺️ Geospatial Maps — GeoPandas + Folium
Choropleth world maps showing risk scores and economic
vulnerability visually by geography — not just by region name.

### ⚙️ Automation — Windows Task Scheduler
The pipeline currently runs manually. Phase 2 will schedule
it to run every night automatically and refresh the
Power BI dashboard without any human input.

### 🌍 Individual Countries — Gap Filling Strategy
Currently using World Bank regional aggregates. Phase 2
expands to 190 individual countries using linear interpolation
and forward-fill to handle missing data years cleanly.

---

> Phase 2 is in active development. Watch this repo for updates.

## 👤 Author

**Lawrence**
Data Analyst | Portfolio Project | 2026

---

<div align="center">

*Built with real data from NASA and the World Bank*
*Pipeline → Analysis → Dashboard — fully end to end*

</div>
