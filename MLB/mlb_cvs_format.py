'''
This file takes in a CSV file generated from mlb_scrape.py and reorganizes it to a better format
for scouting data collection.

Inputs: International prospects or draft prospects, corresponding csv file
Outputs: An organized csv file
Side Effects: Creates a new csv file
'''


# Import necessary libraries
import google.generativeai as genai
import vertexai
import pandas as pd
import os
import json

# MLB Draft prospects or international draft prospects
intl = False;

# Configure Gemini API
genai.configure(api_key="AIzaSyDMfC-aJbzwI7QQVgccAZW9F-pEBw1RBmg")
vertexai.init(project="mlb-draft-2024", location="us-central1")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Function to upload the CSV file
def upload_csv(file_path):
    sample_file = genai.upload_file(path=file_path, display_name=os.path.basename(file_path))
    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    return sample_file.uri

# Path to input CSV file and output CVS file
if intl:
    input_file_path = r"C:\Users\elija\.vscode\Draft_Big_Board\MLB\raw_mlb_prospects_international.csv"
    output_file_path = r"C:\Users\elija\.vscode\Draft_Big_Board\MLB\mlb_prospects_international.csv"
else:
    input_file_path = r"C:\Users\elija\.vscode\Draft_Big_Board\MLB\raw_mlb_prospects_draft.csv"
    output_file_path = r"C:\Users\elija\.vscode\Draft_Big_Board\MLB\mlb_prospects_draft.csv"

# Upload the CSV file and get its URI
file_uri = upload_csv(input_file_path)

# Create the prompt
prompt = (
    "You are an expert data engineer and MLB scout. Using your skills, reorganize this CSV file "
    "to have appropriate columns for the different attributes discussed in each player's description."
)

# Generate content using the prompt and CSV URI
gemini_response = model.generate_content(prompt=[prompt, file_uri])

# Process the response
organized_data = gemini_response['text']  # Adjust based on actual response structure

# Assuming the response is in JSON format
organized_data = json.loads(organized_data)

# Convert the organized data back to a DataFrame
organized_df = pd.DataFrame(organized_data)

# Save the reorganized data to a new CSV file
organized_df.to_csv(output_file_path, index=False)

print(f"Reorganized CSV file saved to {output_file_path}")
