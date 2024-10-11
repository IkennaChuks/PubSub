from google import api_core
from google.cloud import pubsub_v1


project_id = "ikennatest2"
topic_id = "java_topic"

# Configure the retry settings. Defaults shown in comments are values applied
# by the library by default, instead of default values in the Retry object.
custom_retry = api_core.retry.Retry(
    initial=1,  # seconds (default: 0.1)
    maximum=5.0,  # seconds (default: 60.0)
    multiplier=2,  # default: 1.3
    deadline=1000.0,  # seconds (default: 60.0)
    predicate=api_core.retry.if_exception_type(
        api_core.exceptions.Aborted,
        api_core.exceptions.DeadlineExceeded,
        api_core.exceptions.InternalServerError,
        api_core.exceptions.ResourceExhausted,
        api_core.exceptions.ServiceUnavailable,
        api_core.exceptions.Unknown,
        api_core.exceptions.Cancelled,
    ),
)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 1000000):
    data_str = f"Message number {n}"
    # Data must be a bytestring
    data = data_str.encode("utf-8")
    future = publisher.publish(topic=topic_path, data=data, retry=custom_retry)
    print(future.result())

print(f"Published messages with retry settings to {topic_path}.")