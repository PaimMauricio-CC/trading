# TradingView Webhook Receiver

This repository contains a minimal example of a server that receives webhook alerts from [TradingView](https://www.tradingview.com/).

## Setup

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the server

Start the Flask server:

```bash
python server.py
```

The server listens on port `5000` and exposes a single POST endpoint `/webhook` which expects JSON data. TradingView can be configured to send alerts to `http://<your-server-ip>:5000/webhook`.

Whenever an alert is received the server simply prints the JSON payload to the
console. This allows you to see incoming TradingView alerts without any extra
configuration.

## Testing

Run the automated tests with `pytest`:

```bash
pytest
```
