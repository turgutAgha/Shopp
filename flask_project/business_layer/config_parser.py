import json
import os


class Config:
    def __init__(self, filename):
        config_file = open(os.path.abspath(filename), 'r')
        self._config = json.load(config_file)

    def get_property(self, key):
        if key in self._config.keys():
            return self._config[key]
        else:
            return None
