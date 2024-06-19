from Defunct_Files.database import get_players_by_position
from scraping import scrape_and_store_players

if __name__ == '__main__':
    scrape_and_store_players()

    players = get_players_by_position()

    if players is None:
        print("NONE")


    else:
        for player in players:
            print(player)
