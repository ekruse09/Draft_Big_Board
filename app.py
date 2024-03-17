# app.py

from flask import Flask, send_from_directory, jsonify
from database import get_players
from scraping import scrape_and_store_players

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')
'''
@app.route('/players')
def players():
    players_data = get_players()  # Assuming get_players() retrieves player data from the database
    return jsonify(players_data)

@app.route('/scrape')
def scrape():
    scrape_and_store_players()  # Initiates the scraping process to populate the database
    return "Scraping complete!"
'''
if __name__ == '__main__':
    app.run(debug=True)
