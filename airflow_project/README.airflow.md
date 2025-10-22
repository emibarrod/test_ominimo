# Airflow project

This workspace contains a minimal Apache Airflow project skeleton for local development.

Files added:
- `dags/example_dag.py` — a simple DAG demonstrating a BashOperator and PythonOperator.
- `plugins/__init__.py` — plugins package placeholder.
- `.airflowignore` — patterns to ignore.

Quick run (within the project, with a Python environment that has `apache-airflow` installed):

```bash
# initialize the DB and start the webserver + scheduler (development only)
airflow db init
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
airflow webserver --port 8080 &
airflow scheduler
```
