import requests

url = 'http://127.0.0.1:5000/transcription'  # The URL of your Flask server
data = {
    'text': 'Hello, this is a test transcription!'
}

try:
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Response from server:", response.json())
    else:
        print("Failed to send data. Status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error connecting to the server: {e}")
