# Real time mobile money analytics pipeline
This project demonstrates an end to end data engineering pipeline for processing and analyzing telecom transaction data.
## Business Problem
Telecom companies generate large volumes of transactional data.
The goal of this project is to build a reliable pipeline that
ingests, processes, validates, and stores transaction data.

## Objectives
## Architecture
                  ┌────────────────────┐
                  │ Synthetic Data     │
                  │ Generator (Python) │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      Kafka         │
                  │  Transaction Topic │
                  └─────────┬──────────┘
                            │
                            ▼
                  ┌────────────────────┐
                  │      PySpark       │
                  │ Streaming + ETL    │
                  └─────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ PostgreSQL      │   │ Quarantine /    │
        │ Clean Data      │   │ Bad Records     │
        └────────┬────────┘   └─────────────────┘
                 │
                 ▼
        ┌─────────────────┐
        │     Airflow     │
        │ Orchestration   │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │    Power BI     │
        │    Analytics    │
        └─────────────────┘
## Technology stack
### 1. Data Ingestion & MessagingSynthetic 
#### Data Generator (Python)-  This is your data source. It simulates live user transactions (e.g., e-commerce purchases, banking actions) and pushes them into the system.
#### Kafka (Transaction Topic): Acts as your distributed message broker. It absorbs the high-velocity stream of data from Python and acts as a buffer, ensuring no data is lost even if downstream systems slow down.
### 2. Stream Processing & Validation
**PySpark (Streaming + ETL):** This is the heavy-lifting computational engine. It consumes data from Kafka in real time, parses it, and performs data validation.The Split (Clean vs. Quarantine): PySpark acts as a gatekeeper here:
**PostgreSQL (Clean Data):** Valid records that pass your quality checks are saved here for operational use.
**Quarantine / Bad Records:** Corrupted, missing, or fraudulent data points are shunted here (often a separate DB table or a storage bucket) so they don’t ruin your production data.
### 3. Orchestration & Analytics
#### Airflow (Orchestration): Airflow manages the workflow schedules. While PySpark handles the streaming data, Airflow likely triggers batch jobs (like nightly aggregations in PostgreSQL, backups, or processing the quarantined records) and ensures everything runs sequentially.
#### Power BI (Analytics): The final destination. It connects directly to your clean PostgreSQL database to build executive dashboards, monitor live KPIs, and visualize transactional trends.
## Data model
## Pipeline
## Data quality strategy
## Monitoring strategy
## Limitations
## Future improvements
