import json
from os.path import isfile

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def _FileStorage__file_path(self):
        return self.__class__.__file_path

    @property
    def _FileStorage__objects(self):
        return self.__class__.__objects

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self._FileStorage__file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    def reload(self):
        if isfile(self._FileStorage__file_path):
            with open(self._FileStorage__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        else:
            print("File not found. No objects loaded.")
