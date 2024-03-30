import time
import gspread
from google.oauth2.service_account import Credentials
import mpu6050
import numpy as np
from tflite_runtime.interpreter import Interpreter

# Create MPU6050 object
mpu6050_sensor = mpu6050.mpu6050(0x68)

# Set up Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('/home/satwik/Desktop/Credentials.json', scopes=scope)
client = gspread.authorize(creds)
sheet = client.open('RaspberrypiData').sheet1

model_path = "/home/satwik/Desktop/test_data/converted_model (1).tflite"
interpreter = Interpreter(model_path=model_path)

interpreter.allocate_tensors()
# Replace 'Your Google Sheet Name' with your actual sheet name
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Main loop
while True:
    # Read MPU6050 sensor data
    accelerometer_data, gyroscope_data, temperature = mpu6050_sensor.get_all_data()

    # Write sensor values to Google Sheet
    row = [accelerometer_data['x'], accelerometer_data['y'], accelerometer_data['z'],
           gyroscope_data['x'], gyroscope_data['y'], gyroscope_data['z'],temperature]
    sheet.append_row(row)
    input_data = np.array([[[accelerometer_data['x']], [accelerometer_data['y']], [accelerometer_data['z']],
           [gyroscope_data['x']],[ gyroscope_data['y']],[ gyroscope_data['z']]]])
    input_data = input_data.astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    ot = 0 if output_data[0]>1 else "No Fall Detected"
    print(f"predicted Data {ot}")

    # Delay for 1 second before next reading
    time.sleep(1)



