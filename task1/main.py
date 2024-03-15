import json

database = 'bd_players.json'


def data_app(database, mode):
    if mode == 'r':
        with open(database, 'r', encoding='utf-8') as session:
            data = json.load(session)
        pass    

def get_player(player_id):
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        player = data['players'].get(player_id, None)
        return player

def add_player(player_id, name, height):
    with open(database, 'r', encoding='utf-8') as session:
        data = json.load(session)
        player = data['players'].get(player_id, None)
        if player == None:
            with open(database, 'w', encoding='utf-8') as session:
                data['count'] = data['count'] + 1
                player = {
                    "id" : data['count'],
                    "name" : name,
                    "height" : height,
                }
                data['players']['id'] = player
                json.dump(data, session)
    return player


def del_player(database, player_id):
    pass

def create_player(database, player_id, new_height):
    pass



while True:
    print(f'\n\n*****Menu*****\n\n1 - get player\n2 - create player\n3 - add player\n4 - del player\nEnter the command:')
    command = input()
    if command == '1':
        print('tyt')
        player_id = input('Enter ID Player: ')
        player = get_player(player_id)
        if player != None:
            print(player)
        else:
            print('ID - None')
    if command == '2':
        player_id = input('Enter ID Player: ')
        player = get_player(player_id)
        if player == None:
            new_height = input('New height: ')
            player = create_player(database, player_id, new_height)
        else:
            print('ID - None')
    if command == '3':
        player_id = input('Enter ID Player: ')
        player = get_player(player_id)
        if player == None:
            name = input('Enter Name: ')
            height = input('Enter Height: ')
            player = add_player(player_id, name, height)
            if player != None:
                print(f'Player {player} add!')
            else:
                print('ERROR')
    if command == '4':
        player_id = input('Enter ID Player: ')
        player = get_player(database, player_id)
        if player != None:
            del_player(database, player_id)
            print(f'Player {player_id} delete!')
        else:
            print('ID - None')










