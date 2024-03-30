import time
import gspread
from google.oauth2.service_account import Credentials
import mpu6050

# Create MPU6050 object
mpu6050_sensor = mpu6050.mpu6050(0x68)

# Set up Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('/home/satwik/Desktop/Credentials.json', scopes=scope)
client = gspread.authorize(creds)
sheet = client.open('RaspberrypiData').sheet1  # Replace 'Your Google Sheet Name' with your actual sheet name

# Main loop
while True:
    # Read MPU6050 sensor data
    accelerometer_data, gyroscope_data, temperature = mpu6050_sensor.get_all_data()

    # Write sensor values to Google Sheet
    row = [accelerometer_data['x'], accelerometer_data['y'], accelerometer_data['z'],
           gyroscope_data['x'], gyroscope_data['y'], gyroscope_data['z'], temperature]
    sheet.append_row(row)

    # Output sensor values
    print(f"Accelerometer data: {accelerometer_data}")
    print(f"Gyroscope data: {gyroscope_data}")
    print(f"Temperature: {temperature}")

    # Delay for 1 second before next reading
    time.sleep(1)
