from flask import Flask, request
from flask_cors import CORS
import requests
import logging

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Replace with your Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = 'xxxxxxx'
TELEGRAM_CHAT_ID = 'xxxxxxx'

@app.route('/', methods=['POST'])
def contact_form():
    logger.info("Received a POST request")
    logger.debug(f"Request content type: {request.content_type}")
    logger.debug(f"Request data: {request.get_data(as_text=True)}")

    # Explicitly parse form data
    form_data = request.form.to_dict()
    logger.debug(f"Parsed form data: {form_data}")

    # Get form data
    name = form_data.get('name')
    email = form_data.get('email')
    message = form_data.get('message')

    logger.debug(f"Extracted form data: name={name}, email={email}, message={message}")

    # Compose message for Telegram
    telegram_message = f"New contact form submission:\nName: {name}\nEmail: {email}\nMessage: {message}"

    # Send message to Telegram
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': telegram_message
    }

    logger.info("Sending message to Telegram")
    try:
        response = requests.post(telegram_api_url, data=payload)
        response.raise_for_status()
        logger.info("Successfully sent message to Telegram")
        return "Thank you for your message. We'll get back to you soon!"
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending message to Telegram: {str(e)}")
        return "Sorry, there was an error sending your message. Please try again later."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
