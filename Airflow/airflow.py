from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from functions.download_data import download_data_from_gcs
from functions.train_model import train_model
from functions.recommendation import print_recommendations

# Define default_args dictionary
default_args = {
    'owner': 'me-only',
    'start_date': datetime(2022, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG object
dag = DAG('recommender_system_pipeline',
          default_args=default_args,
          schedule_interval='0 6 * * *')


download_data_task = PythonOperator(
    task_id='download_data',
    python_callable=download_data_from_gcs,
    dag=dag)

train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag)

print_recommendations_task = PythonOperator(
    task_id='print_recommendations',
    python_callable=print_recommendations,
    dag=dag)


download_data_task >> train_model_task >> print_recommendations_task


