from google.cloud import pubsub_v1 as pub
from ReadFromGCS import readFromGCS

project_id = 'ikennatest2'
topic_id = 'Python_Topic'

publisher = pub.PublisherClient()
topic_path = publisher.topic_path(project_id,topic_id)

bucket_name = 'gcs_bucket_pubsub'
file = 'PubSub_52610489.csv'
words = readFromGCS(bucket_name,file)
attribute = {"origin" : "PythonPublisedWithAttribute", "Year" : "2024", "env" : "test"}

for word in words:
    for value in word.split(","):
        if len(value) > 0:
            data = value.encode("utf-8")
            future = publisher.publish(topic_path,data, **attribute)
            print(future.result())

print("publish completed")