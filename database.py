# database.py

import sqlite3
from datetime import datetime

conn = sqlite3.connect('players.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS players
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             college TEXT,
             height TEXT,
             weight TEXT,
             birth_date TEXT,
             position TEXT)''')

def add_player(name, college, height, weight, birth_date, position):
    c.execute("INSERT INTO players (name, college, height, weight, birth_date, position) VALUES (?, ?, ?, ?, ?, ?)",
              (name, college, height, weight, birth_date, position))
    conn.commit()

def get_players():
    c.execute("SELECT * FROM players")
    return c.fetchall()

def player_data_exists():
    c.execute("SELECT COUNT(*) FROM players")
    return c.fetchone()[0] > 0
