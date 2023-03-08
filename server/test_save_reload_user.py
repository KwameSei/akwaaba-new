#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Nat"
my_user.last_name = "Osei"
my_user.email = "akwaaba@mail.com"
my_user.password = "1234"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "Kwame"
my_user.last_name = "Osei"
my_user2.email = "kwame@mail.com"
my_user2.password = "1234"
my_user2.save()
print(my_user2)
