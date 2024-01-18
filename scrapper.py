import re
from clases import Game
import os

def get_page_number(soup):
    number_list = soup.find_all('a', rel='nofollow')
    for number in number_list:
        texto = number.text
        if 'next' in texto.lower():
            parent = number.parent
            parent_text = parent.text
            numbers_match = re.search(r'\[ Page \d+ of (\d+) \]', parent_text)
            if numbers_match:
                result = int(numbers_match.group(1))
                return result
            else:
                return None

def generate_urls(url, soup):
    lista = []
    last_page_number = get_page_number(soup)
    for i in range(last_page_number):
        url_list = f"{url}page:{i}/"
        lista.append(url_list)
    return lista


def save_urls_to_json(json_object: str, path: str, filename: str):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{path}/{filename}.json", "w") as outfile:
        outfile.write(json_object)

def get_data_game(soup):
    games = []
    tr_list = soup.find_all('tr')

    for tr in tr_list:
        name_tag = tr.find('a', href=lambda href: href and 'mobygames.com/game/' in href)
        if name_tag:
            game_name = name_tag.text.strip()
            type_tags = tr.find_all('a', href=lambda href: href and '/game/genre' in href)
            game_types = [tag.text.strip() for tag in type_tags] if type_tags else None
            release_tag = tr.find('td', class_="text-center text-nowrap")
            release_year = release_tag.text.strip() if release_tag else None
            game_instance = Game(name=game_name, categories=game_types, date=release_year)
            games.append(game_instance)
    return games

