from __future__ import annotations

from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.utils.dates import days_ago


PROJECT_DIR = "/workspaces/test_ominimo/dbt_project"
# Path to the virtualenv dbt binary that has dbt installed
VENV_DBT = os.environ.get("VENV_DBT", "/workspaces/test_ominimo/.venv/bin/dbt")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 0,
}

with DAG(
    dag_id="dbt_run_from_project",
    default_args=default_args,
    description="Run dbt models from the local dbt_project folder",
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Allow passing models via dag_run.conf (e.g., {"models": "my_model+"})
    models = "{{ dag_run.conf.get('models', '') if dag_run else '' }}"

    # Construct a safe dbt run command that uses the venv's dbt binary
    # If models is empty, dbt will run all models in the project (omit --models)
    dbt_cmd = (
        "cd %s && %s run" % (PROJECT_DIR, VENV_DBT)
    ) + (" --models %s" % models if models else "")

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="echo 'Running dbt command: %s' && %s" % (dbt_cmd, dbt_cmd),
    )
