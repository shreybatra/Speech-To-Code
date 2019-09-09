import requests
import os
from intents import INTENT_TYPES


class CodeBuilder:
    def __init__(self):
        self.luis_url = os.environ["LUIS_APP_URL"]

    def add_next_line(self, code_script, text):

        response = requests.get(self.luis_url + text)

        data = response.json()

        intent = data["topScoringIntent"]["intent"]
        query = data["query"]

        print("Intent - " + intent)
        print("Query - " + query)

        code_script = INTENT_TYPES[intent](code_script, query)

        return code_script, intent, query

