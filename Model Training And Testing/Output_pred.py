import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from tensorflow.keras.models import load_model

# Load your machine learning model
model = load_model('/content/Fall_Detection.h5')  # Replace '/path/to/your/model.h5' with the actual path to your model file

# Define the scope and credentials to access Google Sheets and Google Drive
scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/content/manvitha _credetnials.json', scope)


client = gspread.authorize(credentials)


sheet = client.open("RaspberrypiData")
worksheet = sheet.get_worksheet(0)


try:
    sensor_data = worksheet.get_all_values()
except requests.exceptions.ReadTimeout as e:
    print("Timeout while reading data from Google Sheet:", e)
    sensor_data = []
import numpy as np

processed_data = []
# Iterate through each row in sensor_data
for row in sensor_data:
    # Check if all elements in the row are empty strings
    if all(cell == '' for cell in row):
        continue  # Skip empty rows

    # Convert each element in the row to float
    processed_row = []
    for cell in row:
        processed_row.append(float(cell))

    # Convert sensor values to posture labels (0 for correct posture, 1 for wrong posture)
    posture_label = 1 if any(value > 0 for value in processed_row) else 0
    processed_row.append(posture_label)

    processed_data.append(processed_row)

if processed_data:
    # Extract features and labels
    X = np.array([row[:-1] for row in processed_data])  # Features
    y = np.array([row[-1] for row in processed_data])   # Labels

    # Make predictions using the model
    predictions = model.predict(X)

    print("Predicted activities:")
    for i, prediction in enumerate(predictions):
        if any(prediction>0):
            print("Fall Detected.")
        else:
            print("No Fall Detected")

else:
    print("No valid sensor data found in the Google Sheet.")