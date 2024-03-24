# app.py

from flask import Flask, render_template, redirect, url_for, request, jsonify
from updated_database import get_players_by_position, tables_exist, create_tables, update_grade
from updated_class_definitions import Grade
from scraping import scrape_and_store_players
from datetime import datetime

app = Flask(__name__)


def calculate_age(dob):
    """
    Calculate age based on the date of birth.

    Parameters:
        dob (datetime): Date of birth in datetime format.

    Returns:
        int: Age calculated based on the current date.
    """
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age


@app.route('/')
def index():
    # Check if player data exists in the database
    if not tables_exist():
        # If player data does not exist, create the table
        create_tables()  # Call create_table function if the table doesn't exist
        # Redirect to the scrape route to populate the database
        return redirect(url_for('scrape'))

    # If player data exists, retrieve players from the database
    sort_by = request.args.get('sort_by', 'rating')  # Default sorting by rating
    players = get_players_by_position(sort_by=sort_by)

    # Iterate through players, modify the tuple to include age and map grades to letter values
    modified_players = []
    for player in players:
        dob = datetime.strptime(player[5], '%Y-%m-%d')
        age = calculate_age(dob)
        grade_letters = [str(Grade(char).name) for char in player[10:15]]  # Map grades to letter values
        modified_player = player[:5] + (age,) + player[6:10] + tuple(grade_letters) + player[
                                                                               15:]  # Create a new tuple with grade letters included
        modified_players.append(modified_player)

    players = modified_players  # Update players with the modified list of tuples

    return render_template('quarterbacks.html', players=players)


@app.route('/scrape')
def scrape():
    # Call the scraping function to scrape and store players
    scrape_and_store_players()
    # Redirect back to the index route after scraping
    return redirect(url_for('index'))


@app.route('/save_changes', methods=['POST'])
def save_changes():
    """
    Endpoint to save changes to player grades.
    """
    try:
        data = request.json
        player_id = data.get('player_id')
        grade_index = data.get('grade_index')
        grade_value = data.get('grade_value')

        # Call the update_grade function with all required arguments
        success = update_grade(player_id, grade_index, grade_value)

        return jsonify({'success': success})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
