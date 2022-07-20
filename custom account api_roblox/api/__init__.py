from os import mkdir,remove
from os.path import exists

class user():
    def __init__(self,id: int) -> None:
        self.id = id

class database():
    def __init__(self,name):
        self.name = name
        if (exists(f"./{self.name}") == False):
            mkdir(f"./{self.name}")
        

    def add_user(self,_user:user):
        if (exists(f"./{self.name}")):
            if exists(f"./{self.name}/{_user.id}") == False:
                mkdir(f"./{self.name}/{_user.id}")

    def add_user_value(self,_user:user,value_name:str,value):
        if (exists(f"./{self.name}")):
            if exists(f"./{self.name}/{str(_user.id)}"):
                if exists(f"./{self.name}/{str(_user.id)}/{value_name}.txt" == False):
                    with open(f"./{self.name}/{str(_user.id)}/{value_name}.txt", "w") as f:
                        f.write(value)

    def get_user_value(self,_user:user,value_name:str):
        if (exists(f"./{self.name}")):
            if exists(f"./{self.name}/{str(_user.id)}"):
                if exists(f"./{self.name}/{str(_user.id)}/{value_name}.txt"):
                    if exists(f"./{self.name}/{str(_user.id)}/{value_name}.txt"):
                        with open(f"./{self.name}/{str(_user.id)}/{value_name}.txt", "r") as f:
                            line = f.readline()
                            return line

    def replace_user_value(self,_user:user,value_name:str,value):
        if (exists(f"./{self.name}")):
            if exists(f"./{self.name}/{str(_user.id)}"):
                if exists(f"./{self.name}/{str(_user.id)}/{value_name}.txt" == True):
                    remove(f"./{self.name}/{str(_user.id)}/{value_name}.txt")
                    with open(f"./{self.name}/{str(_user.id)}/{value_name}.txt", "w") as f:
                        f.write(value)
                else:
                    self.add_user_value(_user,value_name,value)
                    self.replace_user_value(_user,value_name,value)

    def remove_user_value(self,_user:user,value_name:str):
        if (exists(f"./{self.name}")):
            if exists(f"./{self.name}/{str(_user.id)}"):
                if exists(f"./{self.name}/{str(_user.id)}/{value_name}.txt"):
                        remove(f"./{self.name}/{str(_user.id)}/{value_name}.txt")
