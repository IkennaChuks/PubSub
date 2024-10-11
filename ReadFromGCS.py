from google.cloud import storage
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/chuksikenna/Downloads/Applications/ikennatest2-cb3a958cd822.json'

def readFromGCS(bucket_name,file):
  

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name= bucket_name)
    file = bucket.blob(file)

    with file.open("r") as f :
        lines = f.read().splitlines()
        return lines

