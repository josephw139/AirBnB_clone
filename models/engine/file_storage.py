#!/usr/bin/python3
"""Doc stuff"""
import json
import os.path


class FileStorage():
    """Doc"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[type(obj).__name__ + "." + obj.id] = str(obj.__dict__)

    def save(self):
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
        else:
            pass

