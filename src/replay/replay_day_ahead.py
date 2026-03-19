import csv
import json
import time
from pathlib import Path
from datetime import datetime

from kafka import KafkaProducer


BROKER_URL = "localhost:19092"
TOPIC_NAME = "day_ahead_events"
NORMALIZED_DATA_PATH = Path("data/normalized/WW_DALMP_ISO_20260317_normalized_small.csv")
EVENT_ORDERING_FIELD = "market_timestamp_utc"
REPLAY_DELAY_SECONDS = 0.031  # Adjusted for ~15 minutes replay duration


def load_normalized_data(file_path: Path) -> list[dict[str, str]]:
    """Load normalized events from the CSV created by normalize_day_ahead.py."""
    with file_path.open("r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file)
        events = list(reader)

    events.sort(
        key=lambda event: (
            event[EVENT_ORDERING_FIELD],
            event["location_id"],
            event["location_name"],
        )
    )
    return events


def replay_events(
    producer: KafkaProducer,
    topic: str,
    events: list[dict[str, str]],
    delay_seconds: float = REPLAY_DELAY_SECONDS,
) -> None:
    """Publish normalized events one-by-one in a deterministic order."""
    start_time = datetime.now()
    for event in events:
        producer.send(topic, value=event)
        print(
            "published",
            event[EVENT_ORDERING_FIELD],
            event["location_id"],
            event["location_name"],
        )
        time.sleep(delay_seconds)

    producer.flush()
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Replay completed in {elapsed_time.total_seconds()} seconds.")


def main() -> None:
    """Main entry point for the replay script."""
    if not NORMALIZED_DATA_PATH.exists():
        raise FileNotFoundError(
            "Normalized CSV not found at "
            f"{NORMALIZED_DATA_PATH}. Run src.ingestion.normalize_day_ahead first."
        )

    producer = KafkaProducer(
        bootstrap_servers=BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    )

    events = load_normalized_data(NORMALIZED_DATA_PATH)
    replay_events(producer, TOPIC_NAME, events)


if __name__ == "__main__":
    main()