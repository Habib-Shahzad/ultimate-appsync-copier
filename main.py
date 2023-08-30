import boto3
from src import AppSyncCopier, AppSyncClient
import os
from dotenv import load_dotenv

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


