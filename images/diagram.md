## 🔎 How It Works

This setup demonstrates a **local-first streaming data pipeline** with replayability:

### 1. Data Preparation

* `download_day_ahead.py` fetches raw external data (e.g., market or LMP data).
* `normalize_day_ahead.py` cleans and structures it into a consistent event format.

### 2. Replay into Streaming System

* `replay_day_ahead.py` simulates real-time streaming by publishing normalized records into **Redpanda**.
* This enables **deterministic replays**, which is key for testing and demos.

### 3. Stream Processing (Flink)

* **Flink JobManager** coordinates the job.
* **Flink TaskManager** executes the workload.
* `hourly_lmp_job.py` (PyFlink) consumes events from Redpanda and performs transformations/aggregations.

### 4. Validation Sink

* Processed results are written to **PostgreSQL**.
* You can query this database to verify correctness and inspect outputs.

---

## 💡 Why This Architecture Works Well

* **Local-first**: Fully runnable on a laptop (Docker Compose friendly).
* **Replayable**: Redpanda + replay script enables repeatable experiments.
* **Separation of concerns**: Clear stages (ingest → stream → process → validate).
* **Production-aligned**: Mirrors real streaming stacks with minimal overhead.

---
