# scraping.py

from datetime import datetime
from bs4 import BeautifulSoup
import requests
from updated_database import add_player
from updated_class_definitions import QB, RB, WR, TE, OT, IOL, IDL, EDGE, LB, CB, SAF


def get_html_content(url):
    """Fetches HTML content from the specified URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch HTML content from URL: {url}")
        return None


def scrape_and_store_players():
    """Scrapes player data from NFL Draft Buzz and stores it in the database."""
    positions_to_scrape = ["QB"] #,"RB", "WR", "TE", "OL", "DL", "LB", "DB"]

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
        "DE": "EDGE",
        "DL/ED": "EDGE",
        "DE/ED": "EDGE",
        "OLB/ED": "EDGE",
        "LB/ED": "EDGE",
        "OLB" : "LB",
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
                # Visit a page with all listed players of that position
                url = f"https://www.nfldraftbuzz.com/positions/{web_position}/{page}/2024"
                print(f"Fetching HTML content from URL: {url}")
                html_content = get_html_content(url)
                if html_content is None:
                    break

                soup = BeautifulSoup(html_content, 'html.parser')

                for row in soup.select('tbody tr[data-href]'):
                    player_position_scraped = row.select_one('.team-result__status:nth-of-type(3)').text.strip()
                    height = row.select_one('.team-result__status:nth-of-type(6)').text.strip()
                    weight = row.select_one('.team-result__status:nth-of-type(5)').text.strip()

                    rating_text = row.select_one('.team-result__status.whiteBold').text.strip()
                    rating = rating_text.split()[0]

                    mapped_position = positions_mapping[player_position_scraped]

                    # Visit individual player page to get more details
                    player_url = row.select_one('a[href^="/Player/"]')['href']
                    player_html_content = get_html_content(f"https://www.nfldraftbuzz.com{player_url}")
                    print(f"Fetching HTML content from URL: https://www.nfldraftbuzz.com{player_url}")
                    if player_html_content:
                        player_soup = BeautifulSoup(player_html_content, 'html.parser')

                        player_first_name = player_soup.find('span', class_='player-info__first-name')
                        player_last_name = player_soup.find('span', class_='player-info__last-name')
                        if player_first_name and player_last_name:
                            player_name = f"{player_first_name.text.strip()} {player_last_name.text.strip()}"
                        else:
                            player_name = "Unknown"  # Set a default value if the name is not found

                        college_parts = player_soup.find('img', alt=lambda x: x and x.endswith('Mascot'))['alt'].split(
                            ' ')
                        college_parts = [part for part in college_parts if part != 'Mascot']
                        college = ' '.join(college_parts)

                        dob_element = player_soup.find('span', title=lambda x: x and "Date of birth" in x)
                        dob = dob_element.find_next_sibling('span').get_text(
                            strip=True) if dob_element else "01/01/1900" # Set a default value when not found

                        player_photo = player_soup.find('div', class_='player-info__item player-info__item--photo')
                        if player_photo:
                            player_photo_url = "https://www.nfldraftbuzz.com" + \
                                               player_soup.find('figure', class_='player-info__photo stopShift').find(
                                                   'img')['src']
                        else:
                            player_photo_url = "https://i.imgflip.com/d0tb7.jpg"  # Set a default value if photo is
                            # not found

                        # Create player object based on mapped position
                        player = create_player_object(mapped_position, player_name, college, height, weight, dob,
                                                      rating,
                                                      player_photo_url)

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


def create_player_object(position, name, college, height, weight, birth_date_str, rate, url):
    """Creates a player object based on the provided position."""
    birth_date = datetime.strptime(birth_date_str, '%m/%d/%Y').date()

    if position == "QB":
        return QB(name, college, height, weight, birth_date, rate, url)
    elif position == "RB":
        return RB(name, college, height, weight, birth_date, rate, url)
    elif position == "WR":
        return WR(name, college, height, weight, birth_date, rate, url)
    elif position == "TE":
        return TE(name, college, height, weight, birth_date, rate, url)
    elif position == "OT":
        return OT(name, college, height, weight, birth_date, rate, url)
    elif position == "IOL":
        return IOL(name, college, height, weight, birth_date, rate, url)
    elif position == "IDL":
        return IDL(name, college, height, weight, birth_date, rate, url)
    elif position == "EDGE":
        return EDGE(name, college, height, weight, birth_date, rate, url)
    elif position == "LB":
        return LB(name, college, height, weight, birth_date, rate, url)
    elif position == "CB":
        return CB(name, college, height, weight, birth_date, rate, url)
    elif position == "SAF":
        return SAF(name, college, height, weight, birth_date, rate, url)
    else:

        return None


def add_player_to_database(player):
    """Adds a player to the database."""
    if player:
        try:
            add_player(player)

        except Exception as e:
            print(f"Error adding player to the database: {e}")
