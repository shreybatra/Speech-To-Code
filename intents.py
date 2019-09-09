import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")

keywords = [
    "string",
    "value",
    "create",
    "print",
    "name",
    "variable",
    "values",
    "integer",
    "new",
    "variables",
    "list",
    "delete",
]


def process_query(query):
    key_var_name = "TEXT_ANALYTICS_SUBSCRIPTION_KEY"
    if not key_var_name in os.environ:
        raise Exception("Please set/export the environment variable: {}".format(key_var_name))
    subscription_key = os.environ[key_var_name]

    endpoint_var_name = "TEXT_ANALYTICS_ENDPOINT"
    if not endpoint_var_name in os.environ:
        raise Exception("Please set/export the environment variable: {}".format(endpoint_var_name))
    endpoint = os.environ[endpoint_var_name]

    documents = {"documents": [{"id": "1", "language": "en", "text": query}]}

    keyphrase_url = endpoint + "/text/analytics/v2.1/keyphrases"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(keyphrase_url, headers=headers, json=documents)
    key_phrases = response.json()

    key_phrases = key_phrases["documents"][0]["keyPhrases"]
    key_list = list(set((" ".join(key_phrases).lower()).split(" ")))
    query = "".join([char for char in query if char not in [".", ",", "'", '"', "!", "?"]])
    terms = [term for term in query.split(" ") if term in key_list]
    print("keyPhrases ----------------")
    print(terms)

    entities_url = endpoint + "/text/analytics/v2.1/entities"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(entities_url, headers=headers, json=documents)
    entities = response.json()["documents"][0]["entities"]
    entities.sort(key=lambda x: x["matches"][0]["offset"])
    entities = [doc["matches"][0]["text"] for doc in entities]
    entity_list = list(set((" ".join(entities).lower()).split(" ")))
    entities = [entity for entity in entities if entity in entity_list]
    print(entities)

    return terms, entities


def print_variable(code_script, query):

    key_phrases, entities = process_query(query)
    for term in key_phrases:
        if term not in keywords:
            new_line = "print({variable})".format(variable=term)
            code_script = code_script + new_line + "\n"
    return code_script


def delete_line(code_script, query):

    key_phrases, entities = process_query(query)
    if "line" in key_phrases:
        code_script = code_script.split("\n")

        size = len(code_script)
        code_script = "\n".join(code_script[0 : size - 2]) + "\n"
        if code_script == "\n":
            code_script = ""
        return code_script
    else:
        return ""


def create_string(code_script, query):
    key_phrases, entities = process_query(query)

    flag = False
    variable_name = ""
    value = ""

    for term in key_phrases:
        if term == "value":
            flag = True
        if term in keywords:
            continue

        if not flag:
            variable_name += term
        else:
            value += term

    code_script = code_script + '{variable_name} = "{value}"\n'.format(variable_name=variable_name, value=value)
    return code_script


def create_list(code_script, query):
    key_phrases, entities = process_query(query)

    flag = False
    variable_name = ""
    value = []

    for term in key_phrases:
        if term == "value" or term == "values":
            flag = True
        if term in keywords:
            continue

        if not flag:
            variable_name += term
        else:
            break
            try:
                term = int(term)
            except:
                pass
            value.append(term)

    value = entities

    code_script = code_script + "{variable_name} = {value}\n".format(variable_name=variable_name, value=value)
    return code_script


def create_integer(code_script, query):
    key_phrases, entities = process_query(query)

    flag = False
    variable_name = ""
    value = "0"

    for term in key_phrases:
        if term == "value":
            flag = True
        if term in keywords:
            continue

        if not flag:
            variable_name += term
        else:
            try:
                value = int(term)
            except:
                value = 0
            break

    try:
        value = int(entities[0])
    except:
        value = 0

    code_script = code_script + "{variable_name} = {value}\n".format(variable_name=variable_name, value=value)
    return code_script


def create_for_loop(code_script, query):
    key_phrases, entities = process_query(query)

    numbers = []

    num_obj = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
    }

    for num in entities:
        try:
            numbers.append(int(num))
        except:
            try:
                numbers.append(int(num_obj[num]))
            except:
                pass

    if len(numbers) == 1:
        code_script = code_script + "for i in range ({value1}):\n".format(value1=numbers[0])
    elif len(numbers) == 2:
        code_script = code_script + "for i in range ({value1},{value2}):\n".format(value1=numbers[0], value2=numbers[1])
    else:
        pass

    return code_script


# def check_condition(code_script, query):
#     key_phrases, entities = process_query(query)


def add_indent(code_script, query):
    code_script = code_script + "\t"
    return code_script


def remove_indent(code_script, query):

    if len(code_script) and code_script[-1] == "\t":
        code_script = code_script[:-1]

    return code_script


INTENT_TYPES = {
    "print variable": print_variable,
    "delete line": delete_line,
    "create string": create_string,
    "create list": create_list,
    "create integer": create_integer,
    "create for loop": create_for_loop,
    # "check condition": check_condition,
    "add indent": add_indent,
    "remove indent": remove_indent
    # "none": none_condition
}
