import csv
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path("logs/predictions.csv")


def log_prediction(temp, humid, co2, predicted_kg):
    # Create the logs folder if it doesn't exist
    LOG_PATH.parent.mkdir(exist_ok=True)

    # Check whether the CSV file already exists
    write_header = not LOG_PATH.exists()

    # Open the CSV file in append mode
    with LOG_PATH.open("a", newline="") as f:
        writer = csv.writer(f)

        # Write the header only once
        if write_header:
            writer.writerow([
                "timestamp_utc",
                "temp_c",
                "humidity_pct",
                "co2_ppm",
                "predicted_kg"
            ])

        # Write one prediction record
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            temp,
            humid,
            co2,
            round(predicted_kg, 3)
        ])