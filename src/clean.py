import pandas as pd
from pathlib import Path

# Read loaded parquet file
df = pd.read_parquet("data/interim/01_loaded.parquet")

# Missing value report
print("Null values before cleaning:")
print(df.isna().sum())

# Valid ranges for polyhouse data
valid = (
    df["humidity_pct"].between(50, 100)
    & df["temperature_c"].between(10, 35)
    & df["co2_ppm"].between(400, 2000)
    & df["yield_kg"].notna()
)

# Keep only valid rows
df = df[valid].copy()

# Fill small missing sensor gaps
cols = ["temperature_c", "humidity_pct", "co2_ppm"]
df[cols] = df[cols].ffill(limit=2)

# Remove rows with missing yield
df = df.dropna(subset=["yield_kg"])

# Remove duplicate timestamps
df = df.drop_duplicates(subset=["timestamp"], keep="last")

# Null values after cleaning
print("\nNull values after cleaning:")
print(df.isna().sum())

# Create processed folder
PROCESSED = Path("data/processed")
PROCESSED.mkdir(parents=True, exist_ok=True)

# Save cleaned dataset
df.to_parquet(PROCESSED / "02_cleaned.parquet", index=False)

# Print final row count
print(f"\nClean rows: {len(df)}")
print("Cleaned file saved successfully!")