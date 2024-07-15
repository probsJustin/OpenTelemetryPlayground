from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/catfact')
def get_cat_fact():
    response = requests.get('https://catfact.ninja/fact')
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
