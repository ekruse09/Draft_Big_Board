'''
This file takes in a website, scrapes the player data off of it, prompts Gemini with that player data to
make a scouting report on that player, and puts it all in a csv file.

Inputs: International prospects or draft prospects, url to the prsopect website
Outputs: A csv file containing the player data
Side Effects: Creates a new csv file
'''

# Import Block
import requests
import re
import csv
import google.generativeai as genai
import vertexai
import time

intl = False;

# configure Gemini API for later use
genai.configure(api_key="AIzaSyDMfC-aJbzwI7QQVgccAZW9F-pEBw1RBmg")
vertexai.init(project="mlb-draft-2024", location="us-central1")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Fetch the HTML content from the URL

if intl:
    url = "https://www.mlb.com/prospects/international/" 
else:
    url = "https://www.mlb.com/prospects/draft/" 

# fetching content from working url
response = requests.get(url)
html_content = response.text

# Define patterns for data extraction from MLB.com
patterns = {
    'rank': r'&quot;rank&quot;:(\d+),',
    'last_name': r'useLastName&quot;:&quot;([^&]*)(?:&\#x27;)?([^&]*)&quot;',
    'first_name': r'useName&quot;:&quot;([^&]*)(?:&\#x27;)?([^&]*)&quot;',
    'position': r'&quot;position&quot;:(?:&quot;([^&]*)&quot;|null),',
    'height': r'&quot;height&quot;:&quot;(\d+)&#x27; (\d+)\\&quot;&quot;',
    'weight': r'&quot;weight&quot;:(\d+)',
    'dob': r'&quot;(\d{4}-\d{2}-\d{2})&quot;',
    'school': r'&quot;colleges&quot;:(?:\[\{&quot;__typename&quot;:&quot;College&quot;,&quot;name&quot;:&quot;((?:[^&]|&amp;|&lt;|&gt;|&quot;|&apos;)+)&quot;\}\]|null)',
    'bats': r'batSideCode&quot;:&quot;([^&]*)&quot;',
    'throws': r'pitchHandCode&quot;:&quot;([^&]*)&quot;',
}

# Extract data using regex patterns
extracted_data = {key: re.findall(pattern, html_content, re.DOTALL) for key, pattern in patterns.items()}

# Process school data to handle special cases
schools = extracted_data['school']
for i in range(len(schools)):
    if schools[i] == '':
        extracted_data['school'][i] = "High School"
    elif schools[i] == 'Texas A&amp;M':
        extracted_data['school'][i] = "Texas A&M"

# Initialize list to store players' data
players = []

# Combine extracted data into structured format
for i in range(len(extracted_data['rank'])):

    feet, inches = extracted_data['height'][i]  # Unpack the tuple into feet and inches

    # Format the height into 'x' y"
    height_str = f"{feet}' {inches}\""

    extracted_data['first_name'][i][0].replace('(', '').replace(')', ''),
    extracted_data['last_name'][i][0].replace('(', '').replace(')', ''),

    # Handle last name formatting
    if len(extracted_data['last_name'][i]) == 2:
        last_name = extracted_data['last_name'][i][0] + extracted_data['last_name'][i][1]
    else:
        last_name = extracted_data['last_name'][i][0]

    # Handle first name formatting
    if len(extracted_data['first_name'][i]) == 2:
        first_name = extracted_data['first_name'][i][0] + extracted_data['first_name'][i][1]
    else:
        first_name = extracted_data['first_name'][i][0]


    player = {
        'Rank': int(extracted_data['rank'][i]),
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': extracted_data['dob'][i],
        'Height': height_str,
        'Weight': int(extracted_data['weight'][i]),
        'Position': extracted_data['position'][i],
        'Bats': extracted_data['bats'][i],
        'Throws': extracted_data['throws'][i],
        'School': extracted_data['school'][i],
        'Scouting Report' : """ """,

    }
    players.append(player)

# Function for prompting the Gemini API
def generate_scouting_report(player):
    # scouting_report_data = Part.from_uri(r"C:\Users\elija\Downloads\draft_player_data.pdf", mime_type="text/xml")
    prompt = (
        "You are a top tier MLB prospect scout. Given your knowledge as an MLB prospect scout, I want you to grade" 
        + player['First Name'] + " " + player['Last Name'] + ", a " + player['Position'] + " from " + player['School']
        + " on an A to F scale on his individual traits as well as an overall grade."
    )
    
    while True:
        try:
            gemini_response = model.generate_content([prompt])
            player_report = gemini_response.text
            player['Scouting Report'] = player_report
            break  # Exit loop if successful
        except Exception as e:
            print(f"Error generating content: {e}")
            print("Retrying in 1 minute...")
            time.sleep(60)  # Wait for 1 minute before retrying


# Generate scouting reports for each player
for player in players:
    generate_scouting_report(player)
    print(f"Scouting report generated for {player['First Name']} {player['Last Name']}.")


# Write data to CSV file
if intl:
    csv_file = "raw_mlb_prospects_international.csv"
else:
    csv_file = "raw_mlb_prospects_draft.csv"

# Open the CSV file in 'w' mode with newline='' and utf-8 encoding
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Define the field names for the CSV header
    fieldnames = ['Rank', 'First Name', 'Last Name', 'Date of Birth', 'Height', 'Weight', 'Position', 'Bats', 'Throws', 'School', 'Scouting Report']
    
    # Initialize the csv.writer
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
    # Write the header row
    writer.writerow(fieldnames)
    
    # Iterate through each player
    for player in players:
        # Escape newline characters in the Scouting Report
        scouting_report = player['Scouting Report'].replace('"', '""').replace('\n', ' ')
        
        # Write each player's data to a new row
        writer.writerow([
            player['Rank'],
            player['First Name'],
            player['Last Name'],
            player['Date of Birth'],
            player['Height'],
            player['Weight'],
            player['Position'],
            player['Bats'],
            player['Throws'],
            player['School'],
            scouting_report  # Write the scouting report
        ])

print(f"Data successfully written to {csv_file}.")










