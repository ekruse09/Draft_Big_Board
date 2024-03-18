# app.py

from flask import Flask, render_template, redirect, url_for
from database import get_players, player_data_exists, create_table
from scraping import scrape_and_store_players

app = Flask(__name__)


@app.route('/')
def index():
    # Check if player data exists in the database
    if not player_data_exists():
        # If player data does not exist, create the table
        create_table()  # Call create_table function if the table doesn't exist
        # Redirect to the scrape route to populate the database
        return redirect(url_for('scrape'))

    # If player data exists, retrieve players from the database
    players = get_players()

    return render_template('index.html', players=players)


@app.route('/scrape')
def scrape():
    # Call the scraping function to scrape and store players
    scrape_and_store_players()
    # Redirect back to the index route after scraping
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
