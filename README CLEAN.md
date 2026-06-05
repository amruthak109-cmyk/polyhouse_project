# Cleaning Log

* Checked missing values using df.isna().sum()
* Removed invalid humidity values outside 50–100
* Removed invalid temperature values outside 10–35
* Removed invalid CO₂ values outside 400–2000
* Forward-filled small missing sensor gaps
* Removed rows with missing yield values
* Removed duplicate timestamps
* Saved cleaned dataset as 02_cleaned.parquet
