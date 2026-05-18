import sqlite3
import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
log = logging.getLogger("db")

DB_PATH = "data/climate_risk.db"


def load_all():
    print("Loading data into SQLite database...")

    # Read cleaned files
    wb = pd.read_parquet("data/processed/world_bank_clean.parquet")
    gs = pd.read_parquet("data/processed/gistemp_clean.parquet")

    # Connect to database (creates file if it doesn't exist)
    con = sqlite3.connect(DB_PATH)

    # Create tables
    con.executescript("""
        CREATE TABLE IF NOT EXISTS dim_country (
            country_code TEXT PRIMARY KEY,
            country_name TEXT
        );

        CREATE TABLE IF NOT EXISTS dim_year (
            year         INTEGER PRIMARY KEY,
            decade       INTEGER,
            is_post_paris INTEGER
        );

        CREATE TABLE IF NOT EXISTS fact_economic (
            country_code        TEXT,
            year                INTEGER,
            gdp_current_usd     REAL,
            gdp_per_capita_usd  REAL,
            agriculture_pct_gdp REAL,
            population          REAL,
            co2_per_capita      REAL,
            PRIMARY KEY (country_code, year)
        );

        CREATE TABLE IF NOT EXISTS fact_climate (
            year                    INTEGER PRIMARY KEY,
            temp_anomaly_c          REAL,
            temp_anomaly_rolling10y REAL,
            anomaly_tier            TEXT
        );
    """)

    # Load dim_country
    countries = wb[["country_code", "country_name"]].drop_duplicates()
    countries.to_sql("dim_country", con, if_exists="replace", index=False)
    print(f"  ✓ dim_country — {len(countries)} countries")

    # Load dim_year
    years = pd.DataFrame({"year": range(1970, 2031)})
    years["decade"] = (years["year"] // 10) * 10
    years["is_post_paris"] = (years["year"] >= 2016).astype(int)
    years.to_sql("dim_year", con, if_exists="replace", index=False)
    print(f"  ✓ dim_year — {len(years)} years")

    # Load fact_economic
    econ_cols = ["country_code", "year", "gdp_current_usd", "gdp_per_capita_usd",
                 "agriculture_pct_gdp", "population", "co2_per_capita"]
    econ = wb[[c for c in econ_cols if c in wb.columns]]
    econ.to_sql("fact_economic", con, if_exists="replace", index=False)
    print(f"  ✓ fact_economic — {len(econ)} rows")

    # Load fact_climate
    gs.to_sql("fact_climate", con, if_exists="replace", index=False)
    print(f"  ✓ fact_climate — {len(gs)} rows")

    con.close()
    print(f"\nDatabase saved → {DB_PATH}")
    log.info(f"Database loaded successfully → {DB_PATH}")


if __name__ == "__main__":
    load_all()