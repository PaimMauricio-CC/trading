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

Every incoming alert is printed to the console, allowing you to verify that the
server is receiving data correctly. This example does not send emails or
forward the alert anywhere else.

## Testing

Run the automated tests with `pytest`:

```bash
pytest
```
