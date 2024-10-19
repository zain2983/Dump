from flask import Flask, request, jsonify
from flask_cors import CORS
import requests  # Import requests library
import os
from groq import Groq

sepr = "\n===============================================\n"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes



GROQ_API_KEY = "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"
DG_API_KEY1 = "d79f7f2dc43b3d2b56e129ba8e3aa74fddd73e8d"


client = Groq(api_key=GROQ_API_KEY)

# # Replace with your Groq API endpoint and credentials
# GROQ_API_URL = "https://your-groq-api-endpoint.com"  # Replace with the actual endpoint
# GROQ_API_KEY = "your_api_key_here"  # Replace with your actual API key

@app.route('/transcription', methods=['POST'])
def transcription():
    data = request.json
    transcription_text = data['text']
    
    print(sepr, "Rcvd:", transcription_text, sepr)

    # Send transcription to Groq API
    print(sepr, "Sending req to groq API " , sepr)
    
    response = send_to_groq_api(transcription_text)
    
    # Print Groq API response
    print("Groq API Response:", response)
    
    return jsonify({'message': 'Transcription received successfully', 'groq_response': response})



def send_to_groq_api(transcription_text):
    prompt = f"""
    You are a customare care agent that is helpful and responds only to the user's query. 
    Respond like a human would, direct and to the point.
    """

    try:
        # Create chat completion using Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "assistant",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": transcription_text,
                },
            ],
            model="llama3-8b-8192",
            max_tokens = 200,
        )
        
        # Return the content of the response
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("Error sending to Groq API:", e)
        return {"error": str(e)}


if __name__ == '__main__':
    app.run(debug=True)









