# this module retrieves from the json configuration file the tags for a specified instrument

import json
import logging
import sys
import os


class ConfigReader:
    def __init__(self):
        self.configDirpath = os.getcwd()

    # TODO: use os.path.join
    def readTags(self):
        with open(f"{self.configDirpath}/data/tags.json") as data:
            return json.load(data)

    def readInstruments(self):
        with open(f"{self.configDirpath}/data/instruments.json") as data:
            return json.load(data)

    def readNewspaper(self):
        with open(f"{self.configDirpath}/data/newspaper.json") as data:
            return json.load(data)

    def readTwitterProfiles(self):
        with open(f"{self.configDirpath}/data/twitter_names.json") as data:
            return json.load(data)
