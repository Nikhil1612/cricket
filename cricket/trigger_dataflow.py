from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "learned-acronym-425420-a7"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load-nik",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://dataflow_metadata_bq/udf.js",
        "JSONPath": "gs://dataflow_metadata_bq/bigquery_schema.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "learned-acronym-425420-a7:cricket_dataset.icc-test-ranking",
        "inputFilePattern": "gs://icc-ranking-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow_metadata_bq",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
