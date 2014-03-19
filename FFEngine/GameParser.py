import json
from collections import namedtuple

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

Formats = Enum(["dict", "tuple"])

def _json_object_hook(d): 
    if "format" in d:
        if d["format"] == Formats.dict:
            return d

    return namedtuple('game', d.keys())(*d.values())
    
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)