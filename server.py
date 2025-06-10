import os
import json
import smtplib
from email.mime.text import MIMEText
from flask import Flask, request, jsonify

EMAIL_RECIPIENTS = [e.strip() for e in os.getenv('ALERT_EMAILS', '').split(',') if e.strip()]

app = Flask(__name__)


def send_email(subject: str, body: str) -> None:
    """Send an email using SMTP if configuration is present."""
    if not EMAIL_RECIPIENTS:
        return
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_user = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    email_from = os.getenv('EMAIL_FROM')
    if not all([smtp_server, smtp_user, smtp_password, email_from]):
        return

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = ', '.join(EMAIL_RECIPIENTS)

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_user, smtp_password)
        smtp.sendmail(email_from, EMAIL_RECIPIENTS, msg.as_string())

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    body = json.dumps(data)
    send_email('TradingView Alert', body)
    return jsonify({'received': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
