from pathlib import Path

content = "sources:\n"
content += "  world_bank:\n"
content += "    base_url: \"https://api.worldbank.org/v2\"\n"
content += "    indicators:\n"
content += "      NY.GDP.MKTP.CD: \"gdp_current_usd\"\n"
content += "      NV.AGR.TOTL.ZS: \"agriculture_pct_gdp\"\n"
content += "      SP.POP.TOTL: \"population\"\n"
content += "      EN.ATM.CO2E.PC: \"co2_per_capita\"\n"
content += "    start_year: 1970\n"
content += "    format: \"json\"\n"
content += "    per_page: 1000\n"
content += "  nasa_gistemp:\n"
content += "    url: \"https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv\"\n"
content += "    description: \"Global surface temperature anomaly\"\n"

Path("config/sources.yaml").write_text(content)
print("Config file created successfully!")