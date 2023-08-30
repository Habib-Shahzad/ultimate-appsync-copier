from src import AppSyncCopier


copier = AppSyncCopier(
    schema_path="schema.graphql",
    testing=True
)


copier.copy_model("Company", "company-1")
