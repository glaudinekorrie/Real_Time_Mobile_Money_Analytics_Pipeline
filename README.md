# Real time mobile money analytics pipeline
This project demonstrates an end to end data engineering pipeline for processing and analyzing telecom transaction data.
## Business Problem
Telecom companies generate large volumes of transactional data.
The goal of this project is to build a reliable pipeline that
ingests, processes, validates, and stores transaction data.

## Objectives
The main objectives are to:

1. Build a real-time data ingestion pipeline.
2. Learn how Apache Kafka handles streaming data.
3. Process streaming data using PySpark.
4. Implement data quality and validation checks.
5. Store processed data in PostgreSQL.
6. Use Apache Airflow for pipeline orchestration.
7. Monitor pipeline and data-quality metrics.
8. Create a Power BI dashboard for analytics.
9. Apply data engineering best practices.
10. Understand how the different technologies work together in an end-to-end pipeline.
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
**Data Generator (Python)-**  This is your data source. It simulates live user transactions (e.g., e-commerce purchases, banking actions) and pushes them into the system.
**Kafka (Transaction Topic):** Acts as your distributed message broker. It absorbs the high-velocity stream of data from Python and acts as a buffer, ensuring no data is lost even if downstream systems slow down.
### 2. Stream Processing & Validation
**PySpark (Streaming + ETL):** This is the heavy-lifting computational engine. It consumes data from Kafka in real time, parses it, and performs data validation.The Split (Clean vs. Quarantine): PySpark acts as a gatekeeper here:
**PostgreSQL (Clean Data):** Valid records that pass your quality checks are saved here for operational use.
**Quarantine / Bad Records:** Corrupted, missing, or fraudulent data points are shunted here (often a separate DB table or a storage bucket) so they don’t ruin your production data.
### 3. Orchestration & Analytics
#### Airflow (Orchestration): Airflow manages the workflow schedules. While PySpark handles the streaming data, Airflow likely triggers batch jobs (like nightly aggregations in PostgreSQL, backups, or processing the quarantined records) and ensures everything runs sequentially.
#### Power BI (Analytics): The final destination. It connects directly to your clean PostgreSQL database to build executive dashboards, monitor live KPIs, and visualize transactional trends.
## Data model
The project uses synthetic mobile money transaction data.

Example fields include:

* transaction_id
* customer_id
* timestamp
* amount
* transaction_type
* location
* merchant_id
* status
* channel

The generated data will also contain intentionally invalid records to simulate real-world data-quality problems.

Examples include:

* Missing values
* Duplicate transactions
* Negative transaction amounts
* Invalid transaction types
* Invalid timestamps
## Pipeline
**Phase 1** — Data Generation

Generate realistic synthetic transaction data using Python.

**Phase 2** — Batch Processing

Load and process transaction data using Python and PostgreSQL.

**Phase 3** — Streaming

Introduce Apache Kafka to continuously stream transaction events.

**Phase 4** — Data Processing

Use PySpark to process and transform streaming data.

**Phase 5** — Data Quality

Implement validation, duplicate detection, and invalid-record handling.

**Phase 6** — Data Storage

Store clean and processed data in PostgreSQL while separating invalid records into a quarantine area.

**Phase 7** — Orchestration

Introduce Apache Airflow to schedule and manage pipeline workflows.

**Phase 8** — Analytics

Connect PostgreSQL to Power BI to create analytical dashboards.

**Phase 9** — Monitoring

Track pipeline and data-quality metrics such as:

* Records processed
* Records rejected
* Processing latency
* Data freshness
* Duplicate records
## Data quality strategy
## Monitoring strategy
## Limitations
## Future improvements
