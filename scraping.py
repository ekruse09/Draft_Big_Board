# scraping.py

from datetime import datetime
import requests
from bs4 import BeautifulSoup
from database import add_player, player_data_exists


def scrape_players(position, page):
    url = f"https://www.nfldraftbuzz.com/positions/{position}/{page}/2024"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    player_data = []
    for player in soup.select('tr[data-href]'):
        name = player.select_one('.team-meta__name .firstName').text.strip() + ' ' + player.select_one('.team-meta__name .lastName').text.strip()
        college = player.select_one('.team-result__score img')['alt'].split()[0]
        height = player.select_one('.team-result__status:nth-of-type(5)').text.strip()
        weight = player.select_one('.team-result__status:nth-of-type(6)').text.strip()
        dob_str = player.select_one('.team-result__status:nth-of-type(8)').text.strip()
        birth_date = datetime.strptime(dob_str, "%m/%d/%Y")
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
                if not soup.select('tr[data-href]'):
                    break
                for player in soup.select('tr[data-href]'):
                    name = player.select_one('.team-meta__name .firstName').text.strip() + ' ' + player.select_one('.team-meta__name .lastName').text.strip()
                    college = player.select_one('.team-result__score img')['alt'].split()[0]
                    height = player.select_one('.team-result__status:nth-of-type(5)').text.strip()
                    weight = player.select_one('.team-result__status:nth-of-type(6)').text.strip()
                    dob_str = player.select_one('.team-result__status:nth-of-type(8)').text.strip()
                    birth_date = datetime.strptime(dob_str, "%m/%d/%Y")
                    add_player(name, college, height, weight, birth_date, position)
                page += 1
