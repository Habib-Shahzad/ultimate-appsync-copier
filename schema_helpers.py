import re

def get_child_models(model, schema_content):
    target_type = f': {model["__typename"]}'
    pattern = r'\b' + re.escape(target_type) + r'\b'
    matches = re.finditer(pattern, schema_content)
    referencing_models = []

    for match in matches:
        type_definition = re.findall(r'type\s+(\w+)\s*{', schema_content[:match.start()])
        if type_definition:
            referencing_models.append(type_definition[-1])

    attribute_references = {}

    for referencing_model in referencing_models:
        pattern = rf'({referencing_model})\s*{{([\s\S]*?)}}'
        match = re.search(pattern, schema_content)
        if match:
            attribute = re.search(r'(\w+)\s*:\s*' + model["__typename"], match.group(2))
            if attribute:
                attribute_references[referencing_model] = attribute.group(1)

    return (attribute_references)




def get_model_attributes(model_name, schema_content):
    pattern = rf'{model_name}\s*{{([\s\S]*?)}}'
    match = re.search(pattern, schema_content)
    if match:
        attributes = re.findall(r'(\w+)\s*:\s*[^!]', match.group(1))
        return attributes
    return []

