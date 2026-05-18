import sqlite3
import pandas as pd
from pathlib import Path

Path("data/colab").mkdir(exist_ok=True)

con = sqlite3.connect("data/climate_risk.db")

# Export each table as CSV
tables = ["dim_country", "dim_year", "fact_economic", "fact_climate"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", con)
    out = f"data/colab/{table}.csv"
    df.to_csv(out, index=False)
    print(f"  ✓ {table} — {len(df)} rows → {out}")

con.close()
print("\nAll files ready for Colab!")