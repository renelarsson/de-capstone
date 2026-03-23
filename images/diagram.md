## 🔎 How It Works

This setup demonstrates a **local-first streaming data pipeline** with replayability:

## Plan Step Mapping

- Step 5: Data preparation scripts create the raw-to-normalized handoff file
- Step 6: Local runtime services are started with Docker Compose
- Step 7: Replay publishes normalized records into the broker
- Step 8: Flink consumes the stream and writes hourly aggregates
- Step 9: PostgreSQL queries validate what Step 8 computed

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

## Step-By-Step Architecture Evolution

### After Step 5

* You have files and Python scripts only.
* No broker, no Flink runtime, and no database are required yet.

### After Step 6

* Redpanda, PostgreSQL, Flink JobManager, and Flink TaskManager are running.
* The runtime exists, but no events have been replayed and no Flink job has been submitted yet.

### After Step 7

* The replay script can publish normalized events into Redpanda.
* The broker now contains a stream that later steps can consume.

### After Step 8

* The PyFlink job is submitted to Flink.
* Flink reads events from Redpanda and writes hourly aggregates to PostgreSQL.

### After Step 9

* PostgreSQL queries provide visible proof that the stream processing path worked end to end.

---

## 💡 Why This Architecture Works Well

* **Local-first**: Fully runnable on a laptop (Docker Compose friendly).
* **Replayable**: Redpanda + replay script enables repeatable experiments.
* **Separation of concerns**: Clear stages (ingest → stream → process → validate).
* **Production-aligned**: Mirrors real streaming stacks with minimal overhead.

---

## Mermaid Diagrams
I created two distinct Mermaid diagram files under images:
* step-5-to-9-service-flow.md
* step-5-to-9-architecture-evolution.md

They are intentionally different:
* **step-5-to-9-service-flow.md**:
Shows the actual service and script interactions across Steps 5–9:
`download → normalize → replay → Redpanda topic → Flink job → JDBC sink → Postgres query validation`.

* **step-5-to-9-architecture-evolution.md**:
Shows what exists after each step and what state persists into the next step:
`prepared files after Step 5, runtime after Step 6, topic state after Step 7, sink state after Step 8, visible verification after Step 9`.
