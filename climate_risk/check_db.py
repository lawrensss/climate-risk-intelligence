import sqlite3

con = sqlite3.connect("data/climate_risk.db")
cur = con.cursor()

print("=== Tables in database ===")
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
for t in tables:
    print(f"  {t[0]}")

print("\n=== Sample climate data ===")
cur.execute("SELECT * FROM fact_climate ORDER BY year DESC LIMIT 5")
rows = cur.fetchall()
for r in rows:
    print(f"  {r}")

print("\n=== Sample economic data ===")
cur.execute("SELECT * FROM fact_economic LIMIT 5")
rows = cur.fetchall()
for r in rows:
    print(f"  {r}")

con.close()