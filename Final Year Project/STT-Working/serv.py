from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

sepr = "\n===============================================\n"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/transcription', methods=['POST'])
def transcription():
    data = request.json
    print(sepr, "Rcvd:", data['text'],sepr)
    return jsonify({'message': 'Transcription received successfully'})


if __name__ == '__main__':
    app.run(debug=True)

