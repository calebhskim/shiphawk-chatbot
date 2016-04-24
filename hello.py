import os
from flask import Flask
from flask import request
import requests

client = Client(auth)

app = Flask(__name__)

token = "CAAYEgJivQC0BADelicwG55A3gnFTmZC2u8u8b6cw7IZBZCtsmZCgirvzTnf52Bj0qdeBuOnIejrHjGo3nINbt2EjZBHaQnZAmBAPDQBsAHMkxlLa1fUAHXALALgRPY5ZBZAuB30c9qb5XTODuZAsSUpCXpL9TdDAJvFaUhSdycOeL8ZCDsLBBZArnoSS1DzCHXXSugZD"
response_url = "https://graph.facebook.com/v2.6/me/messages?access_token="


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/webhook", methods=['GET'])
def webhook_init():
    if request.args.get('hub.verify_token') == 'anewworld':
        return request.args.get('hub.challenge')
    else:
        return 'Error, wrong validation token'


def parse_food(text):
    :wq




def send_text_message(sender, text):
    response = {"recipient": {"id": sender}, "message": {"text": text}}
    r = requests.post(response_url + token, json=response)
    print(r.text)


@app.route("/webhook", methods=['POST'])
def message_handler():
    print("MESSAGE EVENTS")
    jsonData = request.get_json()
    print(jsonData)
    message_events = jsonData["entry"][0]["messaging"]
    for message in message_events:
        print("new message")
        sender = message["sender"]["id"]
        if "message" in message and "text" in message["message"]:
            print("sending text message")
            text = message["message"]["text"]
            print("text read " + text)


    return ('', 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
