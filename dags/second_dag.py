"""
# My Sandbox
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum

default_args = {
    "retries": 2,
    }

dag_Bash = DAG(
    "tiago_dag",
    default_args=default_args,
    description="Sandbox",
    schedule=None,
    start_date=pendulum.datetime(2023, 7, 1, tz="UTC"),
    # catchup=False,
    schedule_interval="*/5 * * * *",
    tags=["sandbox"],
)

my_task = BashOperator(
    task_id="my_task", 
    bash_command=(
        "echo 'Tiago' > /opt/airflow/utils/text.txt "
    ), 
    dag=dag_Bash)

my_task
