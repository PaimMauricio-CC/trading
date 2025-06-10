import json
from flask import Flask, request, jsonify

app = Flask(__name__)


def handle_alert(data: dict) -> None:
    """Process the alert by printing it to the console."""
    print(f"Received alert: {json.dumps(data)}")


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    handle_alert(data)
    return jsonify({'received': data}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
