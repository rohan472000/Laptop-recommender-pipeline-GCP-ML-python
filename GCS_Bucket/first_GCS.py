from google.cloud import storage

import json
from google.oauth2.credentials import Credentials

# Authentication
json_file = 'path/service_account.json'
service_account_info = json.load(json_file)
creds = Credentials.from_service_account_info(service_account_info)


# Create a client object
client = storage.Client(credentials=creds)

# Specify the bucket and file name
bucket_name = 'my-bucket1'
file_name = './dataset-purchased-laptops.csv'

# Upload the file
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(file_name)
blob.upload_from_filename('laptops.csv')
