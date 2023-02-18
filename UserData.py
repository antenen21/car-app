class UserData:
    def __init__(self, firstname, lastname, age, username, password, type):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.username = username
        self.password = password
        self.type = type


user_list = []  # is still empty

user_list = [
    {"firstname": "Andreas", "lastname": "Antenen", "age": 34, "username": "1", "password": "1", "type": "admin"},
    {"firstname": "Robert", "lastname": "Antenen", "age": 72, "username": "2", "password": "2", "type": "guest"}
]

