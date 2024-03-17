# scraping_test.py

from scraping import scrape_and_store_players

if __name__ == "__main__":
    # scrape_and_store_players()

    from database import get_players

    # Call the get_players() function
    players = get_players()

    # Print the retrieved players
    for player in players:
        print(player)
