from appsync_copier import AppSyncCopier, AppSyncClient
from dotenv import load_dotenv
import boto3
import os
load_dotenv()

region = boto3.Session().region_name
client = AppSyncClient(os.getenv("GRAPHQL_URL"),
                       os.getenv("ACCESS_KEY"),
                       os.getenv("SECRET_KEY"),
                       region)

copier = AppSyncCopier(
    schema_path="schema.graphql",
    client=client,
)


copier.copy_model(
    "MODEL_NAME",
    "MODEL_ID"
)
