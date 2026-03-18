# de-capstone Copilot Instructions

## Project Scope

This repository root is the capstone project.

- Project root: `/workspaces/de-capstone`
- Reference material only: `data-engineering-zoomcamp/`
- Reference material only: `homework/`

Do not treat the course or homework folders as the capstone implementation area unless explicitly asked to work on those folders for a separate reason.

## Approved Technical Direction

- Cloud platform: GCP
- Dashboard: Streamlit
- Historical and API ingestion: dlt
- Streaming posture: streaming-first
- Baseline Python version: 3.12
- Warehouse: BigQuery
- Transformations: dbt
- Infrastructure: Terraform
- Orchestration for non-streaming tasks: Kestra
- Stream stack: Redpanda plus PyFlink

Prefer this stack unless the user explicitly changes direction.

## Explicit Non-Goals

- Do not switch ingestion to Bruin by default.
- Do not reframe the project as batch-first.
- Do not create deliverables inside the course folders.
- Do not edit homework files as part of capstone implementation.
- Do not invent a different cloud provider unless the user requests it.

## Teach-First Workflow

For planning and implementation tasks, prioritize learning clarity over speed.

Before major work:

1. State what you are about to do.
2. State why it matters for this capstone.
3. Keep the first implementation slice narrow.

When the user asks for planning:

- produce practical repo-facing documents
- make the next decision explicit
- avoid writing pipeline, infra, streaming, dbt, or dashboard code unless the user asks to move into implementation

When the user asks for implementation:

- keep changes scoped to the current milestone
- explain the files, commands, and validation steps
- avoid broad scaffolding unless it is required for the current milestone

## Planning Priorities

Prefer this order when the user says to continue or asks what is next:

1. dataset validation
2. architecture note
3. repo structure and local workflow
4. smallest end-to-end implementation slice
5. only then broader infrastructure and presentation work

## File Placement Guidance

- Put capstone documentation at the repo root or in clearly named capstone folders created under the root.
- Keep future code in dedicated project directories under the root.
- Leave `data-engineering-zoomcamp/` unchanged unless explicitly asked to compare against course examples.
- Leave `homework/` unchanged unless explicitly asked to reuse patterns from prior work.

## Response Style For This Repo

- Be practical and specific, not generic.
- Tie recommendations back to the approved stack and project story.
- When proposing next steps, favor the smallest decision-reducing step.
- If a requested change conflicts with the approved direction, call out the conflict clearly before proceeding.

## Default Assumptions

Unless the user says otherwise, assume:

- the dataset direction remains ISO-NE-centric
- GCP remains the target deployment environment
- Streamlit remains the dashboard choice
- dlt remains the ingestion tool of choice
- Python 3.12 remains the baseline runtime
- the user wants to learn the stack, not just generate code quickly