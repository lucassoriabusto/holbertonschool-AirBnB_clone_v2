#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            obj = {}
            # Create an empty dictionary to store the filtered objects
            for key, value in FileStorage.__objects.items():
                # Iterate through the items in the __objects dictionary
                if key.split(".")[0] == cls.__name__:
                    # If the first segment of the key matches the class name
                    obj[key] = value
                    # Add this entry to the obj dictionary
            return obj
            # Return the dictionary obj with objects of the given class
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Removes 'obj' from  __objects if present. If 'obj' is None,
          the method does nothing"""
        if obj is not None:
            # Check if 'obj' is a valid object
            key = f"{obj.__class__.__name__}.{obj.id}"
            # Generate a unique key for the object using
            # its class name and 'id' attribute.
            if key in FileStorage.__objects:
                # If the key exists in the '__objects' dictionary
                del FileStorage.__objects[key]
                # Delete the corresponding object from the dictionary.
                self.save
