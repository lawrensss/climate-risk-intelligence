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
│   └── sources.yaml              # API endpoints and parameters
│
├── 📁 data/
│   ├── raw/                      # Untouched API responses (parquet)
│   ├── processed/                # Cleaned, enriched data (parquet)
│   └── colab/                    # Exported CSVs for Colab analysis
│
├── 📁 pipeline/
│   ├── ingest.py                 # Pulls data from NASA + World Bank APIs
│   ├── transform.py              # Cleans, fills gaps, engineers features
│   ├── db.py                     # Loads star schema into SQLite
│   └── export_for_colab.py       # Exports CSVs for notebook analysis
│
├── 📁 logs/
│   └── pipeline.log              # Full run history with timestamps
│
├── fix_config.py                 # Config file generator
├── check_db.py                   # Database verification script
├── export_for_colab.py           # Colab export utility
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
| [World Bank API](https://data.worldbank.org/indicator) | GDP, population, agriculture % of GDP, CO2 per capita | 1970–2025 |

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

pip install requests pandas pyarrow pyyaml numpy openpyxl
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
python export_for_colab.py
```

### Step 3 — Explore in Google Colab

Upload the 4 CSV files from `data/colab/` to a new Colab notebook and run the analysis.

### Step 4 — Open the dashboard

Connect Power BI Desktop to `data/climate_risk.db` via ODBC and open `climate_risk_dashboard.pbix`.

---

## 📈 Dashboard Pages

<table>
<tr>
<td width="33%">

**Page 1 — Climate Overview**
- 📉 Temperature anomaly trend 1970–2025
- 🔥 Hottest years table
- 💰 GDP by region bar chart
- 🎛️ Anomaly tier slicer

</td>
<td width="33%">

**Page 2 — Economic Risk**
- 📈 GDP per capita over time
- 🌍 Population donut by region
- 🌾 Agriculture dependence ranking
- 🎛️ Decade slicer

</td>
<td width="33%">

**Page 3 — Climate vs Economy**
- 🌡️ Temperature anomaly by decade
- 🥧 Anomaly tier pie chart
- 📊 Bars + rolling average combo
- 🎛️ Anomaly tier slicer

</td>
</tr>
</table>

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
          │  Dashboard  │   │   Analysis   │
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

## 🔮 What's Next (Phase 2)

- [ ] Add EM-DAT natural disaster database to quantify economic losses per event
- [ ] Build a country-level climate risk score (0–100) using XGBoost + SHAP
- [ ] Add geospatial choropleth maps using GeoPandas and Folium
- [ ] Automate daily pipeline refresh with Windows Task Scheduler
- [ ] Expand to individual country level with gap-filling strategy

---

## 👤 Author

**Lawrence**
Data Analyst | Portfolio Project | 2026

---

<div align="center">

*Built with real data from NASA and the World Bank*
*Pipeline → Analysis → Dashboard — fully end to end*

</div>
