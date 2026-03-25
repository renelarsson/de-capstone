# de-capstone

Data Engineering Zoomcamp capstone focused on wholesale electricity market analytics with a streaming-first architecture.

## What A Reviewer Should Know First

This repository has moved from documentation-only planning into the first narrow local implementation slice. The project direction is locked, the first dataset slice is chosen, and the first local download-and-normalize path is now working.

The first implementation pass will use historical ISO-NE day-ahead hourly LMP data only. That is a deliberate scope cut so the project can move from planning into development without blocking on unstable anonymous live endpoints.

## Capstone Goal

Build a reproducible pipeline that can:

1. ingest ISO-NE market data
2. replay it through a streaming stack
3. compute windowed price metrics
4. land analytical results in the warehouse path
5. expose those results in a reviewer-friendly dashboard

## Approved Stack

- cloud target: GCP
- ingestion: dlt
- stream broker: Redpanda
- stream processing: PyFlink
- operational sink: PostgreSQL
- warehouse: BigQuery
- transformation: dbt
- dashboard: Streamlit
- infrastructure: Terraform
- orchestration for non-streaming work: Kestra
- baseline Python version: 3.12
- local environment tool: `uv`
- local service runner: Docker Compose

## Current Scope And Status

### What is already decided

- the capstone lives at the repository root
- `data-engineering-zoomcamp/` and `homework/` are reference-only for this capstone
- the project stays streaming-first
- the first runnable slice is local-first
- the first source family is historical ISO-NE day-ahead hourly CSV files

### What is implemented now

- a schema module for the first canonical day-ahead event shape
- a local download script for one historical ISO-NE day-ahead CSV sample
- a local normalization script that converts the raw sample into canonical output
- replay tooling for loading normalized events into Redpanda
- a first PyFlink job that computes hourly aggregates into PostgreSQL
- validated local commands for the first raw-to-normalized and first stream-processing workflows

### What is not implemented yet

- Terraform
- dbt models
- Streamlit app

That is expected. The current documentation set now supports both planning and the first verified local implementation slice.

## How To Use This Documentation Set

Use the markdown files in this order:

1. `README.md` for the project summary and reviewer recipe
2. `plan.md` for the full sequential implementation manual
3. `logs.md` for the consolidated supporting notes and rationale
4. `TODOS.md` for task tracking only

## Reproducibility Recipe

### Stage 1: Verify the host toolchain

Before creating project code, verify that the machine has the expected baseline:

- Python 3.12
- `uv`
- Docker and Docker Compose
- Git
- later, when cloud work starts: GCP CLI and Terraform

The exact command flow is recorded in `plan.md`.

### Stage 2: Follow the implementation manual

`plan.md` is the procedural source of truth. It records, in order:

1. how to prepare the local environment
2. how to create the repo structure
3. how to define the day-ahead sample path
4. how to create the first scripts
5. how to start the local containers
6. how to validate replay and streaming behavior
7. how to expand to cloud components later

### Stage 3: Use the logs as the rationale layer

`logs.md` consolidates the supporting material that explains why the first slice is day-ahead hourly only, why the architecture is streaming-first, and what counts as a successful first pass.

### Stage 4: Validate against the checklist

After implementation starts, the validation points in `logs.md` and the task tracking in `TODOS.md` should be used to confirm that the repo is reproducible rather than merely executable on one machine.

## Repo Working Model

The practical working model for the next phase is:

1. implement locally first
2. prove the path with one small historical day-ahead sample
3. document exact commands and outputs
4. only then widen scope to real-time data, dbt, Terraform, Kestra, and Streamlit

## Expected Near-Term Deliverable

The next real deliverable is a narrow end-to-end local demo that:

1. downloads a day-ahead hourly ISO-NE sample
2. normalizes it into a canonical event schema
3. replays those events into Redpanda
4. runs one PyFlink aggregation
5. writes results to PostgreSQL
6. records all commands and validation steps in the repo

The first five items in that list now have a documented local path, with Step 8 runtime validation recorded in `plan.md` and `logs.md`.

## Reviewer Notes

If you are reading this before implementation exists, the important point is that the repo is being organized so another person can reproduce the build-out without rediscovering the architecture, dataset assumptions, or local workflow.

If you are reading this after implementation starts, begin with `plan.md` and compare the executed steps against the documented procedure.
