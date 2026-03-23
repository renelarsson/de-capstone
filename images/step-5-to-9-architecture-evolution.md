# Step 5 To Step 9 Architecture Evolution
* **step-5-to-9-architecture-evolution.md**:
Shows what exists after each step and what state persists into the next step:
`prepared files after Step 5, runtime after Step 6, topic state after Step 7, sink state after Step 8, visible verification after Step 9`.

```mermaid
flowchart TB
    classDef state fill:#f8f8f8,stroke:#555,color:#111,stroke-width:1px;
    classDef added fill:#e8f5e9,stroke:#2e7d32,color:#102510,stroke-width:1px;
    classDef data fill:#eaf3ff,stroke:#2c5d9b,color:#102234,stroke-width:1px;

    step5[After Step 5\nOnly host-side scripts and files exist\n- raw CSV in data/raw\n- normalized CSVs in data/normalized\n- no containers\n- no Kafka topic\n- no sink table]:::state

    step6[After Step 6\nRuntime is added with Docker Compose\n- Redpanda running\n- PostgreSQL running\n- Flink JobManager running\n- Flink TaskManager running\n- still no replayed events\n- still no running Flink job]:::added

    step7[After Step 7\nStream state is added\n- replay script reads normalized CSV\n- topic day_ahead_events receives JSON messages\n- broker now holds consumable event history]:::added

    step8[After Step 8\nProcessing state is added\n- hourly_lmp_job.py submitted via Flink REST\n- TaskManager consumes from Redpanda\n- tumbling-window aggregates computed\n- JDBC writes into stream_hourly_lmp]:::added

    step9[After Step 9\nValidation layer is added\n- SQL queries read sink table\n- end-to-end correctness becomes visible\n- replay, processing, and sink can be compared]:::added

    data_ready[Prepared artifacts persist\nraw + normalized files + connector JARs]:::data
    runtime_ready[Running local services persist\nRedpanda + Postgres + Flink]:::data
    stream_ready[Topic state persists\nJSON events in day_ahead_events]:::data
    sink_ready[Sink state persists\nrows in stream_hourly_lmp]:::data

    step5 -->|adds runtime| step6
    step6 -->|adds topic data| step7
    step7 -->|adds Flink job and sink writes| step8
    step8 -->|adds verification queries| step9

    step5 -.produces.-> data_ready
    step6 -.keeps plus adds.-> runtime_ready
    step7 -.keeps plus adds.-> stream_ready
    step8 -.keeps plus adds.-> sink_ready

    data_ready --> step6
    runtime_ready --> step7
    stream_ready --> step8
    sink_ready --> step9
```