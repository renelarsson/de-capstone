import os
from uuid import uuid4

import pandas as pd
from src.schema.iso_ne_day_ahead_schema import construct_market_timestamp_utc


RAW_DATA_COLUMNS = [
    "record_type",
    "Date",
    "Hour Ending",
    "Location ID",
    "Location Name",
    "Location Type",
    "Locational Marginal Price",
    "Energy Component",
    "Congestion Component",
    "Marginal Loss Component",
]

def normalize_day_ahead_file(input_path, output_path):
    """
    Normalizes the day-ahead market file and saves the output to the specified path.

    Args:
        input_path (str): The path to the raw input CSV file.
        output_path (str): The path to save the normalized CSV file.

    Returns:
        None
    """
    # Skip report metadata and the field-type row, then assign stable column names.
    df = pd.read_csv(input_path, skiprows=6, header=None, names=RAW_DATA_COLUMNS)

    # Rename columns to normalized schema
    df = df.rename(columns={
        "Date": "market_date",
        "Hour Ending": "hour_ending",
        "Location ID": "location_id",
        "Location Name": "location_name",
        "Location Type": "location_type",
        "Locational Marginal Price": "lmp_total",
        "Energy Component": "energy_component",
        "Congestion Component": "congestion_component",
        "Marginal Loss Component": "marginal_loss_component"
    })

    df = df[df["record_type"] == "D"].copy()
    df = df.drop(columns=["record_type"])

    ingest_run_id = str(uuid4())

    # Add derived fields
    df["market_timestamp_utc"] = df.apply(
        lambda row: construct_market_timestamp_utc(row["market_date"], row["hour_ending"]), axis=1
    )
    df["market_type"] = "day-ahead"
    df["source_file"] = os.path.basename(input_path)
    df["ingest_run_id"] = ingest_run_id

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the normalized file
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Example usage for quick testing
    input_path = "data/raw/WW_DALMP_ISO_20260317.csv"
    output_path = "data/normalized/WW_DALMP_ISO_20260317_normalized.csv"
    normalize_day_ahead_file(input_path, output_path)