import json


class Environment(object):
    def __init__(self):
        self.path = "config/Environment.json"
        self.topology = {}
        with open(self.path) as config:
            self.topology = json.load(config)
