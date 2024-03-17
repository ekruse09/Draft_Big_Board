# scraping.py

from enum import Enum
import requests
from bs4 import BeautifulSoup
from database import add_player, player_data_exists
from datetime import datetime


class Grade(Enum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1


def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def scrape_players(position, page):
    url = f"https://www.nfldraftbuzz.com/positions/{position}/{page}/2024"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_data = []
    for player in soup.find_all('div', class_='player'):
        name = player.find('div', class_='name').text.strip()
        college = player.find('div', class_='college').text.strip()
        height = player.find('div', class_='height').text.strip()
        weight = player.find('div', class_='weight').text.strip()
        birth_date = datetime.strptime(player.find('div', class_='dob').text.strip(), "%m/%d/%Y")
        player_data.append((name, college, height, weight, birth_date, position))
    return player_data


def scrape_and_store_players():
    if not player_data_exists():
        positions = ["QB", "RB", "WR", "TE", "OT", "IOL", "IDL", "Edge", "LB", "CB", "SAF"]
        for position in positions:
            page = 1
            while True:
                url = f"https://www.nfldraftbuzz.com/positions/{position}/{page}/2024"
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                if not soup.find_all('div', class_='player'):
                    break
                for player in soup.find_all('div', class_='player'):
                    name = player.find('div', class_='name').text.strip()
                    college = player.find('div', class_='college').text.strip()
                    height = player.find('div', class_='height').text.strip()
                    weight = player.find('div', class_='weight').text.strip()
                    birth_date = datetime.strptime(player.find('div', class_='dob').text.strip(), "%m/%d/%Y")
                    add_player(name, college, height, weight, birth_date, position)
                page += 1
