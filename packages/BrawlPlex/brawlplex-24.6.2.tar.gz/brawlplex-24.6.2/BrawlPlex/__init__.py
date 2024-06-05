from . import player, clubs, brawlers, events, rankings

def get_API_key(file_path:str):
    with open(file_path, 'r') as file:
        key = file.read()
        return key