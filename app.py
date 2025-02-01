from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

REGISTERED_EMAIL = "paulokla654@gmail.com"
GITHUB_URL = "https://github.com/Paulokla/HNG_Public-API"

@app.route("/", methods=["GET"])
@app.route('/api', methods=['GET'])
def get_info():
    current_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    response = {
        "email": REGISTERED_EMAIL,
        "current_datetime": current_time,
        "github_url": GITHUB_URL
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)