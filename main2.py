from pydantic import BaseModel, field_validator, field_serializer
import re
from datetime import datetime

class Person(BaseModel):
    name: str
    family: str
    age: int
    birthday: int

    def __str__(self):
        return f"Person (name = {self.name}, family = {self.family}, age = {self.age}, birthday = {self.birthday})"

    # Renamed validate method for better readability
    @field_validator('name')
    def validate_name(cls, name):
        pattern = r'^[a-zA-Z\s]+$'
        if not bool(re.match(pattern, name)):
            raise ValueError("Name cannot contain numbers, special characters, or symbols")
        return name

    # Serializer for birthday field
    @field_serializer("birthday")
    def serialize_birthday(self, value):
        dt_object = datetime.fromtimestamp(value)
        return dt_object.strftime("%m-%d-%Y %H:%M")

# Example data
data = {
    'name': "shahram",
    'family': "samar",
    'age': 35,
    'birthday': 1725477010
}

# Validate the data and create an instance of Person
p = Person.model_validate(data)

# Output serialized birthday field correctly
print(p.serialize_birthday(p.birthday))

# Dump the model to JSON
print(p.model_dump_json(indent=2))

data_json = """{
    'name': "shahram",  
    'family': "samar",
    'age' : 35    
}""" 

# p = Person.model_validate_json(data_json)
# print(p)

# str -> model_dump_json
# p.model_dump_json(data_json)
# print(p)
# p.model_dump_json(indent=2)
# print(p)
# # dict -> model_dump
# p.model_dump(data_json)

# p.model_json_schema(data_json)
# print(p)