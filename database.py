import sqlite3
from datetime import datetime
from ui import QB, RB, WR, TE, OT, IOL, IDL, Edge, LB, CB, SAF

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


def add_player(name, college, height, weight, birth_date, position, **kwargs):
    try:
        # Create player object based on position
        player = None
        if position == "QB":
            player = QB(name, college, height, weight, birth_date, **kwargs)
        elif position == "RB":
            player = RB(name, college, height, weight, birth_date, **kwargs)
        elif position == "WR":
            player = WR(name, college, height, weight, birth_date, **kwargs)
        elif position == "TE":
            player = TE(name, college, height, weight, birth_date, **kwargs)
        elif position == "OT":
            player = OT(name, college, height, weight, birth_date, **kwargs)
        elif position == "IOL":
            player = IOL(name, college, height, weight, birth_date, **kwargs)
        elif position == "IDL":
            player = IDL(name, college, height, weight, birth_date, **kwargs)
        elif position == "Edge":
            player = Edge(name, college, height, weight, birth_date, **kwargs)
        elif position == "LB":
            player = LB(name, college, height, weight, birth_date, **kwargs)
        elif position == "CB":
            player = CB(name, college, height, weight, birth_date, **kwargs)
        elif position == "SAF":
            player = SAF(name, college, height, weight, birth_date, **kwargs)

        if player:
            c.execute(
                "INSERT INTO players (name, college, height, weight, birth_date, position) VALUES (?, ?, ?, ?, ?, ?)",
                (name, college, height, weight, birth_date, position))
            conn.commit()
            print(f"Player added: {name}")  # Add this line for debugging
        else:
            print(f"No player created for position: {position}")
    except Exception as e:
        print(f"Error adding player: {e}")  # Add this line for debugging


def get_players():
    try:
        c.execute("SELECT * FROM players")
        return c.fetchall()
    except Exception as e:
        print(f"Error fetching players: {e}")  # Add this line for debugging


def player_data_exists():
    try:
        c.execute("SELECT COUNT(*) FROM players")
        return c.fetchone()[0] > 0
    except Exception as e:
        print(f"Error checking player data: {e}")  # Add this line for debugging
