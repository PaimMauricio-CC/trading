import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    body = json.dumps(data)
    # Print the alert payload so it appears in the console logs
    print(f"Received alert: {body}")
    return jsonify({'received': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
