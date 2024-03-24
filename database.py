import sqlite3
from abc import ABC
from enum import Enum

DB_FILE = 'players.db'


class Grade(Enum):
    A = 5
    B = 4
    C = 3
    D = 2
    F = 1


def set_default_grade():
    return Grade.C.value


class Player(ABC):
    def __init__(self, name, college, height, weight, birth_date, rating, url):
        self.name = name
        self.college = college
        self.height = height
        self.weight = weight
        self.birth_date = birth_date
        self.rating = rating
        self.url = url


class QB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, arm_strength=Grade.C,
                 ball_placement=Grade.C,
                 field_processing=Grade.C, pocket_presence=Grade.C, scrambling=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.arm_strength = arm_strength
        self.ball_placement = ball_placement
        self.field_processing = field_processing
        self.pocket_presence = pocket_presence
        self.scrambling = scrambling


class RB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, acceleration=Grade.C,
                 contact_balance=Grade.C,
                 pass_catching=Grade.C, pass_protection=Grade.C, top_end_speed=Grade.C, vision=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.acceleration = acceleration
        self.contact_balance = contact_balance
        self.pass_catching = pass_catching
        self.pass_protection = pass_protection
        self.top_end_speed = top_end_speed
        self.vision = vision


class WR(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.C,
                 catching=Grade.C,
                 contested_catching=Grade.C, field_awareness=Grade.C, route_running=Grade.C, run_blocking=Grade.C,
                 top_end_speed=Grade.C, quickness=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.ball_carrier_ability = ball_carrier_ability
        self.catching = catching
        self.contested_catching = contested_catching
        self.field_awareness = field_awareness
        self.route_running = route_running
        self.run_blocking = run_blocking
        self.top_end_speed = top_end_speed
        self.quickness = quickness


class TE(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, ball_carrier_ability=Grade.C,
                 catching=Grade.C,
                 movement_skills=Grade.C, pass_blocking=Grade.C, route_running=Grade.C, run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.ball_carrier_ability = ball_carrier_ability
        self.catching = catching
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.route_running = route_running
        self.run_blocking = run_blocking


class OT(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 movement_skills=Grade.C,
                 pass_blocking=Grade.C, power_run_blocking=Grade.C, zone_run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking


class IOL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 movement_skills=Grade.C,
                 pass_blocking=Grade.C, power_run_blocking=Grade.C, zone_run_blocking=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.movement_skills = movement_skills
        self.pass_blocking = pass_blocking
        self.power_run_blocking = power_run_blocking
        self.zone_run_blocking = zone_run_blocking


class IDL(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 block_shedding=Grade.C,
                 movement_skills=Grade.C, pass_rushing=Grade.C, run_stuffing=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing


class Edge(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 coverage_ability=Grade.C,
                 movement_skills=Grade.C, pass_rushing=Grade.C, run_stuffing=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.pass_rushing = pass_rushing
        self.run_stuffing = run_stuffing


class LB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 block_shedding=Grade.C,
                 coverage_ability=Grade.C, movement_skills=Grade.C, tackling=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.coverage_ability = coverage_ability
        self.movement_skills = movement_skills
        self.tackling = tackling


class CB(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C, man_coverage=Grade.C,
                 movement_skills=Grade.C, press=Grade.C, tackling=Grade.C, zone_coverage=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.press = press
        self.tackling = tackling
        self.zone_coverage = zone_coverage


class SAF(Player):
    def __init__(self, name, college, height, weight, birth_date, rating, url, awareness=Grade.C,
                 block_shedding=Grade.C,
                 man_coverage=Grade.C, movement_skills=Grade.C, tackling=Grade.C, zone_coverage=Grade.C):
        super().__init__(name, college, height, weight, birth_date, rating, url)
        self.awareness = awareness
        self.block_shedding = block_shedding
        self.man_coverage = man_coverage
        self.movement_skills = movement_skills
        self.tackling = tackling
        self.zone_coverage = zone_coverage



def get_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DB_FILE)


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


def create_table():
    """Creates the 'players' table in the database if it doesn't exist."""
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
                     url TEXT,
                     arm_strength INTEGER DEFAULT NULL,
                     ball_placement INTEGER DEFAULT NULL,
                     field_processing INTEGER DEFAULT NULL,
                     pocket_presence INTEGER DEFAULT NULL,
                     scrambling INTEGER DEFAULT NULL,
                     acceleration INTEGER DEFAULT NULL,
                     contact_balance INTEGER DEFAULT NULL,
                     pass_catching INTEGER DEFAULT NULL,
                     pass_protection INTEGER DEFAULT NULL,
                     top_end_speed INTEGER DEFAULT NULL,
                     vision INTEGER DEFAULT NULL,
                     ball_carrier_ability INTEGER DEFAULT NULL,
                     catching INTEGER DEFAULT NULL,
                     contested_catching INTEGER DEFAULT NULL,
                     field_awareness INTEGER DEFAULT NULL,
                     route_running INTEGER DEFAULT NULL,
                     run_blocking INTEGER DEFAULT NULL,
                     quickness INTEGER DEFAULT NULL,
                     movement_skills INTEGER DEFAULT NULL,
                     pass_blocking INTEGER DEFAULT NULL,
                     power_run_blocking INTEGER DEFAULT NULL,
                     zone_run_blocking INTEGER DEFAULT NULL,
                     block_shedding INTEGER DEFAULT NULL,
                     pass_rushing INTEGER DEFAULT NULL,
                     run_stuffing INTEGER DEFAULT NULL,
                     coverage_ability INTEGER DEFAULT NULL,
                     tackling INTEGER DEFAULT NULL,
                     man_coverage INTEGER DEFAULT NULL,
                     press INTEGER DEFAULT NULL,
                     zone_coverage INTEGER DEFAULT NULL,
                     awareness INTEGER DEFAULT NULL)''')
        conn.commit()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error creating table: {e}")


def add_player(player_obj):
    """
    Adds a player object to the 'players' table in the database.

    Args:
        player_obj (Player): Player object to be added to the database.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Check if the table exists, if not, create it
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='players'")
        table_exists = c.fetchone()
        if not table_exists:
            create_table()

        # Insert player into the database
        c.execute(
            "INSERT INTO players (name, college, height, weight, birth_date, rating, url) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (player_obj.name, player_obj.college, player_obj.height, player_obj.weight, player_obj.birth_date,
             player_obj.rating, player_obj.url))

        # Insert additional attributes based on player position
        if isinstance(player_obj, QB):
            c.execute(
                "UPDATE players SET arm_strength = ?, ball_placement = ?, field_processing = ?, pocket_presence = ?, scrambling = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, RB):
            c.execute(
                "UPDATE players SET acceleration = ?, contact_balance = ?, pass_catching = ?, pass_protection = ?, "
                "top_end_speed = ?, vision = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    set_default_grade(), player_obj.name))
        elif isinstance(player_obj, WR):
            c.execute(
                "UPDATE players SET ball_carrier_ability = ?, catching = ?, contested_catching = ?, field_awareness = "
                "?, route_running = ?, run_blocking = ?, top_end_speed = ?, quickness = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    set_default_grade(), set_default_grade(), set_default_grade(), player_obj.name))
        elif isinstance(player_obj, TE):
            c.execute(
                "UPDATE players SET ball_carrier_ability = ?, catching = ?, movement_skills = ?, pass_blocking = ?, route_running = ?, run_blocking = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    set_default_grade(), player_obj.name))
        elif isinstance(player_obj, OT):
            c.execute(
                "UPDATE players SET awareness = ?, movement_skills = ?, pass_blocking = ?, power_run_blocking = ?, zone_run_blocking = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, IOL):
            c.execute(
                "UPDATE players SET awareness = ?, movement_skills = ?, pass_blocking = ?, power_run_blocking = ?, zone_run_blocking = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, IDL):
            c.execute(
                "UPDATE players SET awareness = ?, block_shedding = ?, movement_skills = ?, pass_rushing = ?, run_stuffing = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, Edge):
            c.execute(
                "UPDATE players SET awareness = ?, coverage_ability = ?, movement_skills = ?, pass_rushing = ?, run_stuffing = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, LB):
            c.execute(
                "UPDATE players SET awareness = ?, block_shedding = ?, coverage_ability = ?, movement_skills = ?, tackling = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    player_obj.name))
        elif isinstance(player_obj, CB):
            c.execute(
                "UPDATE players SET awareness = ?, man_coverage = ?, movement_skills = ?, press = ?, tackling = ?, zone_coverage = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    set_default_grade(), player_obj.name))
        elif isinstance(player_obj, SAF):
            c.execute(
                "UPDATE players SET awareness = ?, block_shedding = ?, man_coverage = ?, movement_skills = ?, tackling = ?, zone_coverage = ? WHERE name = ?",
                (
                    set_default_grade(), set_default_grade(), set_default_grade(), set_default_grade(),
                    set_default_grade(),
                    set_default_grade(), player_obj.name))

        conn.commit()
        print(f"Player added: {player_obj.name}")

        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error adding player: {e}")


def get_players_by_position(player_position_obj=QB(name="Default Name", college="Default College", birth_date="01/01/1900", height="0ft 0in", weight="0lbs", rating="0",url="www.google.com"), sort_by='rating'):
    """
    Fetches players from the 'players' table in the database based on player position object.

    Args:
        player_position_obj (Player): Player position object (e.g., QB, RB, WR, TE, OT, IOL, IDL, Edge, LB, CB, SAF).
        sort_by (str): Sorting criteria ('name', 'college', 'height', 'weight', 'age', 'rating').

    Returns:
        list: List of players fetched from the database.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Define valid sorting options to prevent SQL injection
        valid_sort_options = ['name', 'college', 'height', 'weight', 'age', 'rating']
        if sort_by not in valid_sort_options:
            sort_by = 'rating'  # Default to sorting by rating if an invalid option is provided

        # Adjust the SQL query and sorting order based on the sorting criteria and player position
        if sort_by == 'name' or sort_by == 'college':
            c.execute(f"SELECT * FROM players WHERE {player_position_obj.__class__.__name__} = ? ORDER BY {sort_by} ASC", (player_position_obj.name,))
        elif sort_by == 'height' or sort_by == 'weight' or sort_by == 'rating':
            c.execute(f"SELECT * FROM players WHERE {player_position_obj.__class__.__name__} = ? ORDER BY {sort_by} DESC", (player_position_obj.name,))
        elif sort_by == 'age':
            c.execute(f"SELECT * FROM players WHERE {player_position_obj.__class__.__name__} = ? ORDER BY birth_date DESC ", (player_position_obj.name,))

        players = c.fetchall()

        conn.close()
        return players
    except Exception as e:
        raise RuntimeError(f"Error fetching players: {e}")
