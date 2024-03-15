import json
import random

database = 'bd_user.json'

def empty_id():
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        empty = []
        for i in range(len(data['users'])):
            empty.append(int(i)+random.randint(1, random.randint(1, 100)))
            return empty


def get_user(id_user):
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        user = data['users'].get(id_user, None)
        return user

def add_user(last_name:str, first_name:str, number_fone:int, post:str, office:int):
    new_user = {}
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        with open(database, 'w', encoding='utf-8') as session:
            new_user = {
                "id" : id_user,
                "first_name" : first_name,
                "last_name" : last_name,
                "number_fone" : number_fone,
                "post" : post,
                "office" : office
            }
            data['users'][id_user] = new_user
            json.dump(data, session)
            return new_user
            
def creat_user(last_name:str, first_name:str, number_fone:int, post:str, office:int):
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        with open(database, 'w', encoding='utf-8') as session:
            new_user = {
                "id" : id_user,
                "first_name" : first_name,
                "last_name" : last_name,
                "number_fone" : number_fone,
                "post" : post,
                "office" : office
            }
            data['users'][id_user] = new_user
            json.dump(data, session)
            return new_user

def del_user(id_user) -> str:
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        del data['users'][id_user]
        with open(database, 'w', encoding='utf-8') as session: 
            json.dump(data, session)
    return id_user


while True:
    print(f'**** Menu ****\n1 - Get User\n2 - Add User\n3 - Create User\n4 - Delete User')
    command:str = input()
    if command == '1':
        id_user:str = input('Enter User ID: ')
        user = get_user(id_user) 
        if user != None:
            print(f'USER : {user}')
        else:
            print(f'User ID - {id_user} NONE')
    if command == '2':
        id_user = input('Enter New User ID: ')
        user = get_user(id_user)
        if user == None:
            first_name:str = input('Enter First Name User: ')
            last_name:str = input('Enter Last Name User: ')
            number_fone:int = input('Enter Number Fone User: ')
            post:str = input('Enter Post User: ')
            office:int = input('Enter Office User: ')
            new_user = creat_user(last_name, first_name, number_fone, post, office)
            print(f'Add New User\n{new_user}')
        else:
            empty = empty_id()
            print(f'ID {id_user} - Busy!\nEmpty ID {empty}')
    if command == '3':
        id_user = input('Enter Create User ID: ')
        user = get_user(id_user)
        if user != None:
            first_name:str = input('Enter New First Name User: ')
            last_name:str = input('Enter New Last Name User: ')
            number_fone:int = input('Enter New Number Fone User: ')
            post:str = input('Enter New Post User: ')
            office:int = input('Enter New Office User: ')
            new_user = add_user(last_name, first_name, number_fone, post, office)
            print(f'Add Create User\n{new_user}')
    if command == '4':
        id_user = input('Enter Delete User ID: ')
        user:str = get_user(id_user)
        if user != None:
            del_user(id_user)
            print(f'User {id_user} Delete')


            
    



















