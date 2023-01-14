from google.cloud import storage

import json
from google.oauth2.credentials import Credentials

from GCS_Bucket.first_GCS import bucket_name, file_name

# Authentication
json_file = './laptop_recommender/service_account.json'
service_account_info = json.load(json_file)
creds = Credentials.from_service_account_info(service_account_info)

# Create a client object
client = storage.Client(credentials=creds)


# function to download the data from GCS
def download_data_from_gcs():
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.download_to_filename('laptops.csv')


#download_data_from_gcs(bucket_name, file_name)
