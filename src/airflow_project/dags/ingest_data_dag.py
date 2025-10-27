from __future__ import annotations

from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils.dates import days_ago


PROJECT_DIR = "/Users/emilio/code/test_ominimo/src/dbt_project"
# Path to the virtualenv dbt binary that has dbt installed
VENV_DBT = "/Users/emilio/code/test_ominimo/.venv/bin/dbt"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 0,
}

with DAG(
    dag_id="ingest_data_dag",
    default_args=default_args,
    description="Ingest data from parquet files",
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    dbt_cmd = (
        f"cd {PROJECT_DIR} && {VENV_DBT} run --models stg_policies stg_quotes"
    )

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command=f"echo 'Running dbt command: {dbt_cmd}' && {dbt_cmd}",
    )
