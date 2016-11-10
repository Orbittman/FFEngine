""" Game data parser """
import json
from collections import namedtuple

class Enum(set):
    """ Enumeration class """
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

FORMATS = Enum(["dict", "tuple"])

def _json_object_hook(element):
    if "format" in element:
        if element["format"] == FORMATS.dict:
            return element

    return namedtuple('game', element.keys())(*element.values())

def json2obj(data):
    """ Json file loader """
    return json.loads(data, object_hook=_json_object_hook)
