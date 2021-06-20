from flask import Flask
from flask import request

def register_user(str: request):
   register_data = request.get_json()
   # app.db.todos.insert_one(register_data)
   return "Your register username is {}".format(register_data['username'])

