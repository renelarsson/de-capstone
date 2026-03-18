from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# ISO-NE Day-Ahead Schema
# This module defines the schema for normalizing ISO-NE day-ahead market data.

# Raw column names from the CSV
RAW_COLUMNS = [
    "Date",
    "Hour Ending",
    "Location ID",
    "Location Name",
    "Location Type",
    "Locational Marginal Price",
    "Energy Component",
    "Congestion Component",
    "Marginal Loss Component"
]

# Normalized field names (initial event model)
NORMALIZED_FIELDS = [
    "market_date",  # Derived from 'Date'
    "hour_ending",  # Derived from 'Hour Ending'
    "market_timestamp_utc",  # Constructed from 'Date' and 'Hour Ending'
    "market_type",  # Static value for day-ahead market
    "location_id",  # From 'Location ID'
    "location_name",  # From 'Location Name'
    "location_type",  # From 'Location Type'
    "lmp_total",  # From 'Locational Marginal Price'
    "energy_component",  # From 'Energy Component'
    "congestion_component",  # From 'Congestion Component'
    "marginal_loss_component",  # From 'Marginal Loss Component'
    "source_file",  # File name for traceability
    "ingest_run_id"  # Unique ID for the ingestion run
]

SOURCE_TIMEZONE = ZoneInfo("America/New_York")
UTC_TIMEZONE = ZoneInfo("UTC")

def construct_market_timestamp_utc(date_str, hour_ending):
    """
    Constructs a UTC timestamp from the given date and hour ending.

    Args:
        date_str (str): The date in 'MM/DD/YYYY' format.
        hour_ending (int): The hour ending (1-24).

    Returns:
        datetime: The UTC timestamp.
    """
    # ISO-NE reports publish market dates in New England local market time.
    date = datetime.strptime(str(date_str), "%m/%d/%Y")
    hour = int(hour_ending) - 1  # Hour Ending is 1-based, so subtract 1
    local_time = (date + timedelta(hours=hour)).replace(tzinfo=SOURCE_TIMEZONE)

    # Convert the source market time to UTC for a canonical timestamp.
    utc_time = local_time.astimezone(UTC_TIMEZONE)
    return utc_time