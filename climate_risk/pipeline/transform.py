import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
log = logging.getLogger("transform")

# Create processed folder
Path("data/processed").mkdir(parents=True, exist_ok=True)


def latest_file(pattern):
    files = sorted(Path("data/raw").glob(pattern))
    if not files:
        raise FileNotFoundError(f"No file found for pattern: {pattern}")
    return files[-1]


def transform_world_bank():
    print("Cleaning World Bank data...")
    df = pd.read_parquet(latest_file("world_bank_*.parquet"))

    # Remove regional aggregates — keep only real countries
    aggregates = ["WLD","LIC","MIC","HIC","EAS","SAS","SSA","LCN","MEA","ECS","NAC"]
    df = df[~df["country_code"].isin(aggregates)]
    df = df[df["country_code"].str.len() == 3]
    df = df[df["country_code"].str.strip() != ""]

    # Keep only from 1970 onwards
    df = df[df["year"] >= 1970]

    # Fill gaps within each country using interpolation
    numeric_cols = ["gdp_current_usd", "agriculture_pct_gdp", "population", "co2_per_capita"]
    df = df.sort_values(["country_code", "year"])
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df.groupby("country_code")[col].transform(
                lambda x: x.interpolate(method="linear").ffill().bfill()
            )

    # Add GDP per capita column
    if "gdp_current_usd" in df.columns and "population" in df.columns:
        df["gdp_per_capita_usd"] = (df["gdp_current_usd"] / df["population"]).round(2)

    df = df.reset_index(drop=True)
    out = Path("data/processed/world_bank_clean.parquet")
    df.to_parquet(out, index=False)
    print(f"  ✓ Saved {len(df)} rows → {out}")
    log.info(f"transform_world_bank: {len(df)} rows saved")
    return df


def transform_gistemp():
    print("Cleaning NASA temperature data...")
    df = pd.read_parquet(latest_file("gistemp_*.parquet"))

    # Keep only from 1970
    df = df[df["year"] >= 1970].copy()
    df = df.sort_values("year")

    # Add 10 year rolling average — key feature for analysis
    df["temp_anomaly_rolling10y"] = (
        df["temp_anomaly_c"].rolling(10, min_periods=5).mean().round(4)
    )

    # Classify severity — useful as a slicer in Power BI
    conditions = [
        df["temp_anomaly_c"] >= 1.0,
        df["temp_anomaly_c"] >= 0.5,
        df["temp_anomaly_c"] >= 0.0,
    ]
    choices = ["High", "Moderate", "Low"]
    df["anomaly_tier"] = np.select(conditions, choices, default="Negative")

    df = df.reset_index(drop=True)
    out = Path("data/processed/gistemp_clean.parquet")
    df.to_parquet(out, index=False)
    print(f"  ✓ Saved {len(df)} rows → {out}")
    log.info(f"transform_gistemp: {len(df)} rows saved")
    return df


if __name__ == "__main__":
    transform_world_bank()
    transform_gistemp()
    print("\nAll data cleaned and saved!")