# -*- coding: utf-8 -*-

import os
import codecs
import json

def _byteify(data, ignore_dicts = False):
    """
    Hook function for json load/loads.
    """

    if isinstance(data, unicode):
        return data.encode("utf-8")
    elif isinstance(data, list):
        return [_byteify(item, ignore_dicts) for item in data]
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts): _byteify(value, ignore_dicts)
            for key, value in data.iteritems()
        }
    return data


def json_load_byteified(file_handle):
    """
    Package json load with hook.
    """
    return _byteify(
        json.load(file_handle, object_hook = _byteify),
        ignore_dicts = True
    )


def json_loads_byteified(json_text):
    """
    Package json loads with hook.
    """
    return _byteify(
        json.loads(json_text, object_hook = _byteify),
        ignore_dicts = True
    )


def json_file_to_pyData(jsonFile):
    """
    Convert json file to python data.
    """
    with codecs.open(jsonFile, encoding="utf-8") as f:
        try:
            return json_load_byteified(f)
        except Exception as e:
            return None


def pyData_to_json_file(inputData, outputFile):
    """
    Convert python data to json file.
    """
    jsonStr = json.dumps(inputData, indent = 4, 
            sort_keys = True, ensure_ascii = False)
    with open(outputFile, "w") as f:
        f.write(jsonStr)


if __name__ == '__main__':
    import sys
    print json_file_to_pyData(sys.argv[1])

