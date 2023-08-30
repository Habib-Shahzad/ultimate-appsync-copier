
from schema_helpers import *
from query_helpers import *
from test_data import *


def singular_to_plural(input_word):
    if input_word.endswith('y'):
        return input_word[:-1] + 'ies'
    elif input_word.endswith('s'):
        return input_word + 'es'
    else:
        return input_word + 's'

with open('schema.graphql', 'r') as file:
    schema_content = file.read()


def run_mutation(model_name, params):
    old_id = params.get('id')
    if 'new' in old_id:
        print('Something weird happened')
        exit()

    del params['id']
    created = {
        'id': f'new-{old_id}',
        **params
    }

    plurar = singular_to_plural(model_name)

    new_database[f'list{plurar}'].append(created)
    return created

def run_query(query, modelName):
    plurar = singular_to_plural(modelName)
    return database[f'list{plurar}']


def run_filter_query(child, reference_parent, parent_id):
    plurar = singular_to_plural(child)
    lst = database[f'list{plurar}']
    result = []
    for item in lst:
        if item[reference_parent] == parent_id:
            result.append(item)
    return result



def get_by_id(model_name, id):
    plurar = singular_to_plural(model_name)
    lst = database[f'list{plurar}']
    for item in lst:
        if item['id'] == id:
            return item
    
    
def copy_model(parent_name: str, parent_id: str, new_parent_id: str = None):
    model = get_by_id(parent_name, parent_id)
    if model is None:
        return

    children = get_child_models(model, schema_content)
    if new_parent_id is None:
        parent_creation = run_mutation(parent_name, model.copy())
        new_parent_id = parent_creation['id']

    for child_name, attribute in children.items():
        reference_parent = parent_name.lower()+'ID'
        data_list = run_filter_query(child_name, reference_parent, parent_id)

        for item in data_list:
            item[reference_parent] = new_parent_id
            child_creation = run_mutation(child_name, item.copy())
            copy_model(item['__typename'], item['id'], child_creation['id'])


copy_model("Company", 'company-1') 
open('database.py', 'w').write(f'new_database = {new_database}')




