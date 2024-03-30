
#FALL GUARDIAN
Fall Guardian is a human fall detection system designed and implemented using MPU6050 sensor technology. This intelligent system detects falls in real-time.

Installation
Option 1: Downloading ZIP File
Go to the GitHub repository: Fall Guardian Repository.
Click on the "Code" button.
Select "Download ZIP".
Extract the downloaded ZIP file to your desired location.
Navigate to the extracted folder to access the project files.

Option 2: Cloning Repository
bash
Copy code
git clone https://github.com/your-username/fall-guardian.git

Usage
Devices/Components Required
Windows Laptop/System
1)Raspberry Pi
2)IMU MPU6050 Sensor
3)RJ45 Cable (For Wired Connection)
4)Jumper Wires
5)Setup Instructions

->Connect the Raspberry Pi to your system using HDMI (for desktop) or using Putty and RealVNC Viewer for laptops through wired or wireless connection.

wpa_supplicant.conf file can be used for Wirelsess Connections.This should be placed in bootfs drive aka Memory Card Of Pi.And Should Use A Single wifi for both Pi And System To Connect.SSID And pass Key should be mentioned in the file inorder to connect

Make the sensor connections according to the provided specifications.

Install the required modules on the Raspberry Pi.

Run the Data_Reading.py script to check if the sensor is working properly.

Google Sheets Integration

Create a Google Sheet named "RaspberryPiData" in Google Sheets.

Go to Google Cloud Console and enable the Google Sheets and Google Drive API.

Create the required credentials and grant access to the generated email in Google Cloud Console.

Generate a JSON file named Credentials and use it for authentication.

->Model Training
Train the model using the falldetectiondata.csv dataset.
Save both the H5 model and TensorFlow Lite (Tflite) model.
Upload the Credentials.json file to Google Colab and Raspberry Pi.

->Testing
a)Google Colab (H5 Model)
Use Output_pred.py for testing.
Place the sensor and Raspberry Pi on the thigh and sensor above the pocket.
Data transfer to Google Sheets is handled by data_tranfer_to_sheets.py,
Test the data received from Raspberry Pi and sensor From Sheets.

b)Raspberry Pi (Tflite Model)
Use App.py for testing.
The output will be generated seamlessly in the terminal.
Data transfer to Google Sheets is handled by data_tranfer_to_sheets.py, which is included within App.py.
Contributing
Contributions to Fall Guardian are welcome! Feel free to submit bug reports, suggest enhancements, or create pull requests.
