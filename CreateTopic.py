from google.cloud import pubsub_v1


project_id = "ikennatest2"
topic_id = "Python_Topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

topic = publisher.create_topic(request={"name": topic_path})

print(f"Created topic: {topic.name}")