# scraping.py

from datetime import datetime
from bs4 import BeautifulSoup
import requests
from ui import QB, RB, WR, TE, IOL, IDL, Edge, LB, CB, SAF

# Define a constant fake birthdate
FAKE_BIRTH_DATE = datetime(1990, 1, 1)  # For example, January 1st, 1990


def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch HTML content from URL: {url}")
        return None


def scrape_and_store_players():
    positions_to_scrape = ["QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB"]

    positions_mapping = {
        "QB": "QB",
        "RB": "RB",
        "WR": "WR",
        "TE": "TE",
        "OL": "IOL",
        "C": "IOL",
        "OG": "IOL",
        "OT": "OT",
        "DL": "IDL",
        "DT": "IDL",
        "NT": "IDL",
        "DE": "Edge",
        "DL/ED": "Edge",
        "DE/ED": "Edge",
        "OLB/ED": "Edge",
        "LB/ED": "Edge",
        "LB": "LB",
        "CB": "CB",
        "DB": "SAF",
        "S": "SAF"
    }

    for web_position in positions_to_scrape:
        if web_position in positions_mapping:
            print(f"Scraping players for position: {web_position}")

            page = 1
            while True:
                url = f"https://www.nfldraftbuzz.com/positions/{web_position}/{page}/2024"
                print(f"Fetching HTML content from URL: {url}")
                html_content = get_html_content(url)
                if html_content is None:
                    break

                soup = BeautifulSoup(html_content, 'html.parser')
                player_data = []

                for row in soup.select('tbody tr[data-href]'):
                    rank = row.select_one('.team-result__status').text.strip()
                    name = row.select_one(
                        '.team-meta__info .team-meta__name .firstName').text.strip() + " " + row.select_one(
                        '.team-meta__info .team-meta__name .lastName').text.strip()
                    player_position_scraped = row.select_one('.team-result__status:nth-of-type(3)').text.strip()
                    college = row.select_one('.team-result__score img')['alt'].split()[0]
                    height = row.select_one('.team-result__status:nth-of-type(6)').text.strip()
                    weight = row.select_one('.team-result__status:nth-of-type(5)').text.strip()
                    rating = row.select_one('.team-result__status.whiteBold').text.strip()
                    summary = row.select_one('.team-result__status:nth-of-type(11)').text.strip()

                    mapped_position = positions_mapping[player_position_scraped]

                    # Create player object based on mapped position
                    player = create_player_object(mapped_position, name, college, height, weight,
                                                  FAKE_BIRTH_DATE)  # Birthdate faked for now
                    add_player_to_database(player)

                # Inside the while loop where you check for pagination links
                pagination_nav = soup.find('nav', class_='post-pagination')
                if pagination_nav:
                    page_numbers = [int(link.text) for link in pagination_nav.find_all('a', class_='page-link')]
                    if all(page_number <= page for page_number in page_numbers):
                        break  # No next page link found, indicating no more pages for this position
                else:
                    break  # No pagination nav found, indicating no more pages for this position

                page += 1  # Move to the next page for the current position

            print(f"Scraping for position {web_position} complete")
        else:
            print(f"No mapping found for web position: {web_position}")


def create_player_object(position, name, college, height, weight, birth_date):
    if position == "QB":
        return QB(name, college, height, weight, birth_date)
    elif position == "RB":
        return RB(name, college, height, weight, birth_date)
    elif position == "WR":
        return WR(name, college, height, weight, birth_date)
    elif position == "TE":
        return TE(name, college, height, weight, birth_date)
    elif position == "IOL":
        return IOL(name, college, height, weight, birth_date)
    elif position == "IDL":
        return IDL(name, college, height, weight, birth_date)
    elif position == "Edge":
        return Edge(name, college, height, weight, birth_date)
    elif position == "LB":
        return LB(name, college, height, weight, birth_date)
    elif position == "CB":
        return CB(name, college, height, weight, birth_date)
    elif position == "SAF":
        return SAF(name, college, height, weight, birth_date)


def add_player_to_database(player):
    from database import add_player  # Move the import statement here
    if player:
        try:
            add_player(player.name, player.college, player.height, player.weight, player.birth_date, player.__class__.__name__)
            print(f"Player added to the database: {player.name}")
        except Exception as e:
            print(f"Error adding player to the database: {e}")