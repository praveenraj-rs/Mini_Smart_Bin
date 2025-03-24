import requests
import json
import sys

def post_sensor_data(username, location, organic, inorganic):
    # Backend URL
    url = "https://hex-backend.vercel.app/smartbin"

    # Sensor data payload
    data = {
        "username": username,
        "location": location,
        "organic": organic,
        "inorganic": inorganic
    }

    # Headers
    headers = {"Content-Type": "application/json"}

    try:
        # Sending POST request
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        # Checking response
        if response.status_code == 200:
            print("Data posted successfully:", response.json())
        else:
            print("Failed to post data:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Error while posting data:", e)

post_sensor_data('yuvan','chennai',25,50)

