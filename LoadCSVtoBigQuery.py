from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()


table_id = "ikennatest2.PubSub.LoadedFromGCS"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("firstName", "STRING"),
        bigquery.SchemaField("lastName", "STRING"),
        bigquery.SchemaField("Id", "STRING"),
    ],
    skip_leading_rows=0,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://gcs_bucket_pubsub/sample2.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))