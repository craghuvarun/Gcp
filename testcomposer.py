from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import GoogleCloudStorage

# Define the start date for the DAG
start_date = datetime(year=2023, month=3, day=5)

# Define the default arguments for the DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': start_date,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
dag = DAG(
    'my_dag',
    default_args=default_args,
    description='My DAG',
    schedule_interval=timedelta(days=1),
)

# Create the storage task
storage_task = GoogleCloudStorage(
    task_id='write_file',
    bucket='testingpurpose',
    object='file.txt',
    
    dag=dag,
)