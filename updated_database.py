# database.py

import sqlite3
from updated_class_definitions import QB, RB, WR, TE, OT, IOL, IDL, EDGE, LB, CB, SAF

DB_FILE = 'players.db'


def get_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DB_FILE)

def tables_exist():
    """Checks if the required tables exist in the database."""
    try:
        conn = get_connection()
        c = conn.cursor()

        # Check if the Players table exists
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Players'")
        player_table_exists = c.fetchone()

        conn.close()

        return player_table_exists is not None

    except Exception as e:
        print(f"Error checking table existence: {e}")
        return False


def create_tables():
    """Creates tables in the database."""
    try:
        conn = get_connection()
        c = conn.cursor()

        # Create the parent table "Players"
        c.execute('''CREATE TABLE IF NOT EXISTS Players (
                     player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     college TEXT,
                     height TEXT,
                     weight TEXT,
                     birth_date TEXT,
                     rating TEXT,
                     url TEXT
                     )''')

        # Create subtables for each player position
        subtables = {
            'QB': (
                "arm_strength INTEGER DEFAULT 1,"
                "ball_placement INTEGER DEFAULT 1,"
                "field_processing INTEGER DEFAULT 1,"
                "pocket_presence INTEGER DEFAULT 1,"
                "scrambling INTEGER DEFAULT 1"
            ),
            'RB': (
                "acceleration INTEGER DEFAULT 1,"
                "contact_balance INTEGER DEFAULT 1,"
                "pass_catching INTEGER DEFAULT 1,"
                "pass_protection INTEGER DEFAULT 1,"
                "top_end_speed INTEGER DEFAULT 1,"
                "vision INTEGER DEFAULT 1"
            ),
            'WR': (
                "ball_carrier_ability INTEGER DEFAULT 1,"
                "catching INTEGER DEFAULT 1,"
                "contested_catching INTEGER DEFAULT 1,"
                "field_awareness INTEGER DEFAULT 1,"
                "route_running INTEGER DEFAULT 1,"
                "run_blocking INTEGER DEFAULT 1,"
                "top_end_speed INTEGER DEFAULT 1,"
                "quickness INTEGER DEFAULT 1"
            ),
            'TE': (
                "ball_carrier_ability INTEGER DEFAULT 1,"
                "catching INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "pass_blocking INTEGER DEFAULT 1,"
                "route_running INTEGER DEFAULT 1,"
                "run_blocking INTEGER DEFAULT 1"
            ),
            'OT': (
                "awareness INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "pass_blocking INTEGER DEFAULT 1,"
                "power_run_blocking INTEGER DEFAULT 1,"
                "zone_run_blocking INTEGER DEFAULT 1"
            ),
            'IOL': (
                "awareness INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "pass_blocking INTEGER DEFAULT 1,"
                "power_run_blocking INTEGER DEFAULT 1,"
                "zone_run_blocking INTEGER DEFAULT 1"
            ),
            'IDL': (
                "awareness INTEGER DEFAULT 1,"
                "block_shedding INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "pass_rushing INTEGER DEFAULT 1,"
                "run_stuffing INTEGER DEFAULT 1"
            ),
            'EDGE': (
                "awareness INTEGER DEFAULT 1,"
                "coverage_ability INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "pass_rushing INTEGER DEFAULT 1,"
                "run_stuffing INTEGER DEFAULT 1"
            ),
            'LB': (
                "awareness INTEGER DEFAULT 1,"
                "block_shedding INTEGER DEFAULT 1,"
                "coverage_ability INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "tackling INTEGER DEFAULT 1"
            ),
            'CB': (
                "awareness INTEGER DEFAULT 1,"
                "man_coverage INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "press INTEGER DEFAULT 1,"
                "tackling INTEGER DEFAULT 1,"
                "zone_coverage INTEGER DEFAULT 1"
            ),
            'SAF': (
                "awareness INTEGER DEFAULT 1,"
                "block_shedding INTEGER DEFAULT 1,"
                "man_coverage INTEGER DEFAULT 1,"
                "movement_skills INTEGER DEFAULT 1,"
                "tackling INTEGER DEFAULT 1,"
                "zone_coverage INTEGER DEFAULT 1"
            )
        }

        for position, attributes in subtables.items():
            c.execute(f'''CREATE TABLE IF NOT EXISTS {position} (
                         {position.lower()}_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         player_id INTEGER,
                         {attributes},
                         FOREIGN KEY(player_id) REFERENCES Players(player_id)
                         )''')
        conn.commit()
        conn.close()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")


def add_player(player_obj):
    """
    Adds a player object to the database.

    Args:
        player_obj: Player object to be added to the database.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Insert player into the Players table
        c.execute(
            "INSERT INTO Players (name, college, height, weight, birth_date, rating, url) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (player_obj.name, player_obj.college, player_obj.height, player_obj.weight, player_obj.birth_date,
             player_obj.rating, player_obj.url))
        conn.commit()

        # Get the player_id of the inserted player
        player_id = c.lastrowid

        # Insert position-specific information into the corresponding subtable
        if isinstance(player_obj, QB):
            c.execute(
                f"INSERT INTO QB (player_id, arm_strength, ball_placement, field_processing, pocket_presence, scrambling) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.arm_strength.value, player_obj.ball_placement.value,
                 player_obj.field_processing.value, player_obj.pocket_presence.value, player_obj.scrambling.value))
        elif isinstance(player_obj, RB):
            c.execute(
                f"INSERT INTO RB (player_id, acceleration, contact_balance, pass_catching, pass_protection, "
                f"top_end_speed, vision) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.acceleration.value, player_obj.contact_balance.value,
                 player_obj.pass_catching.value, player_obj.pass_protection.value, player_obj.top_end_speed.value,
                 player_obj.vision.value))
        elif isinstance(player_obj, WR):
            c.execute(
                f"INSERT INTO WR (player_id, ball_carrier_ability, catching, contested_catching, field_awareness, "
                f"route_running, run_blocking, top_end_speed, quickness) "
                f"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.ball_carrier_ability.value, player_obj.catching.value,
                 player_obj.contested_catching.value, player_obj.field_awareness.value,
                 player_obj.route_running.value, player_obj.run_blocking.value, player_obj.top_end_speed.value,
                 player_obj.quickness.value))
        elif isinstance(player_obj, TE):
            c.execute(
                f"INSERT INTO TE (player_id, ball_carrier_ability, catching, movement_skills, pass_blocking, "
                f"route_running, run_blocking) "
                f"VALUES (?, ?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.ball_carrier_ability.value, player_obj.catching.value,
                 player_obj.movement_skills.value, player_obj.pass_blocking.value,
                 player_obj.route_running.value, player_obj.run_blocking.value))
        elif isinstance(player_obj, OT):
            c.execute(
                f"INSERT INTO OT (player_id, awareness, movement_skills, pass_blocking, power_run_blocking, zone_run_blocking) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.movement_skills.value,
                 player_obj.pass_blocking.value, player_obj.power_run_blocking.value,
                 player_obj.zone_run_blocking.value))
        elif isinstance(player_obj, IOL):
            c.execute(
                f"INSERT INTO IOL (player_id, awareness, movement_skills, pass_blocking, power_run_blocking, zone_run_blocking) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.movement_skills.value,
                 player_obj.pass_blocking.value, player_obj.power_run_blocking.value,
                 player_obj.zone_run_blocking.value))
        elif isinstance(player_obj, IDL):
            c.execute(
                f"INSERT INTO IDL (player_id, awareness, block_shedding, movement_skills, pass_rushing, run_stuffing) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.block_shedding.value,
                 player_obj.movement_skills.value, player_obj.pass_rushing.value,
                 player_obj.run_stuffing.value))
        elif isinstance(player_obj, EDGE):
            c.execute(
                f"INSERT INTO EDGE (player_id, awareness, coverage_ability, movement_skills, pass_rushing, run_stuffing) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.coverage_ability.value,
                 player_obj.movement_skills.value, player_obj.pass_rushing.value,
                 player_obj.run_stuffing.value))
        elif isinstance(player_obj, LB):
            c.execute(
                f"INSERT INTO LB (player_id, awareness, block_shedding, coverage_ability, movement_skills, tackling) "
                f"VALUES (?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.block_shedding.value,
                 player_obj.coverage_ability.value, player_obj.movement_skills.value,
                 player_obj.tackling.value))
        elif isinstance(player_obj, CB):
            c.execute(
                f"INSERT INTO CB (player_id, awareness, man_coverage, movement_skills, press, tackling, zone_coverage) "
                f"VALUES (?, ?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.man_coverage.value,
                 player_obj.movement_skills.value, player_obj.press.value,
                 player_obj.tackling.value, player_obj.zone_coverage.value))
        elif isinstance(player_obj, SAF):
            c.execute(
                f"INSERT INTO SAF (player_id, awareness, block_shedding, man_coverage, movement_skills, tackling, zone_coverage) "
                f"VALUES (?, ?, ?, ?, ?, ?, ?)",
                (player_id, player_obj.awareness.value, player_obj.block_shedding.value,
                 player_obj.man_coverage.value, player_obj.movement_skills.value,
                 player_obj.tackling.value, player_obj.zone_coverage.value))
        else:
            print("Error adding player! No object instance detected!")

        conn.commit()
        print(f"Player added: {player_obj.name}")

        conn.close()
    except Exception as e:
        raise RuntimeError(f"Error adding player: {e}")


def get_all_players(sort_by='rating'):
    """
    Fetches all players from the 'players' table in the database.

    Args:
        sort_by (str): Sorting criteria ('name', 'college', 'height', 'weight', 'age', 'rating').

    Returns:
        list: List of all players fetched from the database.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Define valid sorting options to prevent SQL injection
        valid_sort_options = ['name', 'college', 'height', 'weight', 'age', 'rating']
        if sort_by not in valid_sort_options:
            sort_by = 'rating'  # Default to sorting by rating if an invalid option is provided

        # Adjust the SQL query and sorting order based on the sorting criteria
        if sort_by in ['name', 'college']:
            c.execute(f"SELECT * FROM players ORDER BY {sort_by} ASC")
        elif sort_by == 'height' or sort_by == 'weight':
            c.execute(f"SELECT * FROM players ORDER BY {sort_by} DESC")
        elif sort_by == 'age':
            c.execute(f"SELECT * FROM players ORDER BY birth_date ASC ")
        elif sort_by == 'rating':
            c.execute(f"SELECT * FROM players ORDER BY rating DESC ")

        players = c.fetchall()

        conn.close()
        return players
    except Exception as e:
        raise RuntimeError(f"Error fetching players: {e}")


def get_players_by_position(position='QB', sort_by='rating'):
    """
    Fetches players of a certain position from the database.

    Args:
        position (str): Position of the players (e.g., 'QB', 'RB', 'WR', etc.). Defaults to 'QB'.
        sort_by (str): Sorting criteria ('name', 'college', 'height', 'weight', 'age', 'rating').

    Returns:
        list: List of players of the specified position fetched from the database.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Define valid sorting options to prevent SQL injection
        valid_sort_options = ['name', 'college', 'height', 'weight', 'age', 'rating']
        if sort_by not in valid_sort_options:
            sort_by = 'rating'  # Default to sorting by rating if an invalid option is provided

        # Adjust the SQL query and sorting order based on the sorting criteria
        if sort_by in ['name', 'college']:
            c.execute(f"SELECT DISTINCT Players.*, {position}.* FROM Players JOIN {position} ON Players.player_id = {position}.player_id ORDER BY Players.{sort_by} ASC")
        elif sort_by == 'height' or sort_by == 'weight':
            c.execute(f"SELECT DISTINCT Players.*, {position}.* FROM Players JOIN {position} ON Players.player_id = {position}.player_id ORDER BY Players.{sort_by} DESC")
        elif sort_by == 'age':
            c.execute(f"SELECT DISTINCT Players.*, {position}.* FROM Players JOIN {position} ON Players.player_id = {position}.player_id ORDER BY Players.birth_date ASC ")
        elif sort_by == 'rating':
            c.execute(f"SELECT DISTINCT Players.*, {position}.* FROM Players JOIN {position} ON Players.player_id = {position}.player_id ORDER BY Players.rating DESC ")

        players = c.fetchall()

        conn.close()
        return players
    except Exception as e:
        raise RuntimeError(f"Error fetching players by position: {e}")


def update_grade(player_id, position, grade_index, grade_value):
    """
    Updates the grade of a player for a specific position in the database.

    Args:
        player_id (int): The ID of the player whose grade is to be updated.
        position (str): The position of the player (e.g., 'QB', 'RB', 'WR', etc.).
        grade_index (int): The index of the grade to be updated (0 for the first grade, 1 for the second, etc.).
        grade_value (str): The new grade value to be assigned.

    Raises:
        RuntimeError: If an error occurs while updating the grade.
    """
    try:
        conn = get_connection()
        c = conn.cursor()

        # Construct the SQL query to update the grade for the specified player and position
        query = f"UPDATE {position} SET grade_{grade_index} = ? WHERE player_id = ?"

        # Execute the SQL query
        c.execute(query, (grade_value, player_id))

        # Commit the changes to the database
        conn.commit()

        conn.close()
        print(f"Grade updated successfully for player ID {player_id}, position {position}, grade index {grade_index}.")
    except Exception as e:
        raise RuntimeError(f"Error updating grade: {e}")
