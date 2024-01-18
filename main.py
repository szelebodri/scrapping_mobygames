import requests
import json
from bs4 import BeautifulSoup

from constants import HOME_URL, JSON_FOLDER, JSON_FILEPATH
from scrapper import generate_urls, save_urls_to_json, get_data_game
from clases import BannedException

res = requests.get(HOME_URL)
sopa = BeautifulSoup(res.text, 'html5lib')

if __name__ == '__main__':
    if res.status_code == 429:
        raise BannedException()
    links = generate_urls(HOME_URL, sopa)
    json_object = json.dumps(links, indent=4)
    save_urls_to_json(json_object, JSON_FOLDER, "links2")
    with open(JSON_FILEPATH, 'r') as links2:
        urls = json.load(links2)
        for url in urls[:2]:
            game_instances = get_data_game(sopa)
            for game in game_instances:
                print(f"Name: {game.name}, Categories: {game.categories}, Date: {game.date}")

