import requests
import pandas as pd
import yaml
import time
import logging
from pathlib import Path
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
log = logging.getLogger("ingest")

# Create folders if they don't exist
Path("data/raw").mkdir(parents=True, exist_ok=True)

# Load config
with open("config/sources.yaml") as f:
    CONFIG = yaml.safe_load(f)


def fetch_world_bank():
    print("Downloading World Bank data...")
    cfg = CONFIG["sources"]["world_bank"]
    frames = []

    for indicator_code, col_name in cfg["indicators"].items():
        print(f"  → {col_name}")
        url = f"{cfg['base_url']}/country/all/indicator/{indicator_code}"
        params = {
            "format": "json",
            "per_page": cfg["per_page"],
            "date": f"{cfg['start_year']}:{datetime.now().year}"
        }
        try:
            r = requests.get(url, params=params, timeout=30)
            r.raise_for_status()
            raw = r.json()
            if not raw or len(raw) < 2:
                continue
            rows = []
            for rec in raw[1] or []:
                if rec.get("value") is not None:
                    rows.append({
                        "country_code": rec["countryiso3code"],
                        "country_name": rec["country"]["value"],
                        "year": int(rec["date"]),
                        col_name: rec["value"]
                    })
            frames.append(pd.DataFrame(rows))
            time.sleep(0.5)
        except Exception as e:
            log.error(f"World Bank {col_name} failed: {e}")

    if not frames:
        raise RuntimeError("No World Bank data fetched")

    df = frames[0]
    for f in frames[1:]:
        df = df.merge(f, on=["country_code", "country_name", "year"], how="outer")

    df = df.sort_values(["country_code", "year"]).reset_index(drop=True)
    today = datetime.now().strftime("%Y%m%d")
    df.to_parquet(f"data/raw/world_bank_{today}.parquet", index=False)
    print(f"  ✓ Saved {len(df)} rows")
    log.info(f"World Bank: saved {len(df)} rows")
    return df


def fetch_gistemp():
    print("Downloading NASA temperature data...")
    cfg = CONFIG["sources"]["nasa_gistemp"]
    try:
        r = requests.get(cfg["url"], timeout=30)
        r.raise_for_status()
        from io import StringIO
        lines = r.text.split("\n")
        data_start = next(i for i, l in enumerate(lines) if l.startswith("Year"))
        df = pd.read_csv(StringIO("\n".join(lines[data_start:])))
        df.columns = [c.strip() for c in df.columns]
        df = df[["Year", "J-D"]].rename(columns={"Year": "year", "J-D": "temp_anomaly_c"})
        df = df[~df["temp_anomaly_c"].astype(str).str.contains("\\*")].copy()
        df["temp_anomaly_c"] = pd.to_numeric(df["temp_anomaly_c"])
        df["year"] = pd.to_numeric(df["year"])
        df = df.dropna().reset_index(drop=True)
        today = datetime.now().strftime("%Y%m%d")
        df.to_parquet(f"data/raw/gistemp_{today}.parquet", index=False)
        print(f"  ✓ Saved {len(df)} rows")
        log.info(f"GISTEMP: saved {len(df)} rows")
        return df
    except Exception as e:
        log.error(f"GISTEMP failed: {e}")
        raise


if __name__ == "__main__":
    fetch_world_bank()
    fetch_gistemp()
    print("\nAll data downloaded successfully!")