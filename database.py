# database.py

import sqlite3
from datetime import datetime, date
from ui import QB, RB, WR, TE, OT, IOL, IDL, Edge, LB, CB, SAF

DB_FILE = 'players.db'


def get_connection():
    return sqlite3.connect(DB_FILE)


def create_table():
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS players
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     college TEXT,
                     height TEXT,
                     weight TEXT,
                     birth_date TEXT,
                     rating TEXT,
                     url TEXT)''')  # Added rating and url columns
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error creating table: {e}")


def add_player(name, college, height, weight, birth_date, position, rating, url, **kwargs):
    try:
        conn = get_connection()
        c = conn.cursor()

        # Check if the table exists, if not, create it
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players'")
        table_exists = c.fetchone()
        if not table_exists:
            create_table()


        # Create player object based on position
        player = None
        if position == "QB":
            player = QB(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "RB":
            player = RB(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "WR":
            player = WR(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "TE":
            player = TE(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "OT":
            player = OT(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "IOL":
            player = IOL(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "IDL":
            player = IDL(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "Edge":
            player = Edge(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "LB":
            player = LB(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "CB":
            player = CB(name, college, height, weight, birth_date, rating, url, **kwargs)
        elif position == "SAF":
            player = SAF(name, college, height, weight, birth_date, rating, url, **kwargs)

        if player:
            c.execute(
                "INSERT INTO players (name, college, height, weight, birth_date, rating, url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (name, college, height, weight, birth_date, rating, url))  # Insert rating and url into the database
            conn.commit()
            print(f"Player added: {name}")
        else:
            print(f"No player created for position: {position}")

        conn.close()
    except Exception as e:
        print(f"Error adding player: {e}")


def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, '%m/%d/%Y').date()
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def get_players():
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM players")
        players = c.fetchall()

        # Convert birth date string to age for each player
        players_with_age = []
        for player in players:
            player_with_age = list(player)
            birth_date_str = player_with_age[5]  # Get the birth date string from the database
            age = calculate_age(birth_date_str)  # Calculate the age using the DOB string
            player_with_age[5] = age  # Replace birth date with age in the player data
            players_with_age.append(player_with_age)

        conn.close()
        return players_with_age
    except Exception as e:
        print(f"Error fetching players: {e}")
        return None


def player_data_exists():
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM players")
        count = c.fetchone()[0]
        conn.close()
        return count > 0
    except Exception as e:
        print(f"Error checking player data: {e}")
        return False
