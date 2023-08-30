from ..schema import Schema
from ..query import QueryHelper
from ..example import *
import json


class AppSyncCopier:

    def __init__(self,
                 schema_path: str,
                 testing: bool = False
                 ) -> None:
        self.schema = Schema(schema_path)
        self.testing = testing

    def recursive_copier(self, parent_name: str, parent_id: str, new_parent_id: str = None):

        model = None

        if self.testing:
            model = get_by_id(parent_name, parent_id)

        if model is None:
            return

        children = self.schema.get_child_models(model)
        if new_parent_id is None:
            parent_creation = run_mutation(parent_name, model.copy())
            new_parent_id = parent_creation['id']

        for child_name, _ in children.items():
            reference_parent = parent_name.lower()+'ID'

            if self.testing:
                data_list = run_filter_query(
                    child_name, reference_parent, parent_id)

            for item in data_list:
                item[reference_parent] = new_parent_id

                if self.testing:
                    child_creation = run_mutation(child_name, item.copy())
                    self.recursive_copier(item['__typename'], item['id'],
                                          child_creation['id'])

    def copy_model(self, parent_name: str, parent_id: str, new_parent_id: str = None):
        self.recursive_copier(parent_name, parent_id, new_parent_id)
        if self.testing:
            open('database.json', 'w').write(
                json.dumps(new_database, indent=2))
