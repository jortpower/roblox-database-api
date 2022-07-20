from api import *
from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route("/new_database/<name>")
def new_database(name):
    database(name)
    return "database created"

@app.route("/add_user/<database_name>/<user_id>")
def add_user(database_name,user_id):
    temp_db = database(database_name)
    temp_user = user(int(user_id))
    temp_db.add_user(temp_user)
    return "user added"

@app.route("/add_user_value/<database_name>/<user_id>/<value_name>/<value>")
def add_user_value(database_name,user_id,value_name,value):
    temp_db = database(database_name)
    temp_user = user(int(user_id))
    temp_db.add_user_value(temp_user,value_name,value)
    return "value added"

@app.route("/replace_user_value/<database_name>/<user_id>/<value_name>/<value>")
def replace_user_value(database_name,user_id,value_name,value):
    temp_db = database(database_name)
    temp_user = user(int(user_id))
    temp_db.replace_user_value(temp_user,value_name,value)
    return "value replaced"

@app.route("/remove_user_value/<database_name>/<user_id>/<value_name>")
def remove_user_value(database_name,user_id,value_name):
    temp_db = database(database_name)
    temp_user = user(int(user_id))
    temp_db.remove_user_value(temp_user,value_name)
    return "value removed"

@app.route("/get_user_value/<database_name>/<user_id>/<value_name>")
def get_user_value(database_name,user_id,value_name):
    temp_db = database(database_name)
    temp_user = user(int(user_id))
    return str(temp_db.get_user_value(temp_user,value_name))

app.run(debug=False,port=8080)