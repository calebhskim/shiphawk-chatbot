import os
from flask import Flask
from flask import request
import simplejson as json
import requests

app = Flask(__name__)

token = "CAAIQgWB4KZCEBALEK87qe6a5opnlsvPOSxhA3oOAxq6VPynP5Sm1iDUhnu0wIxnd55De0bqlAZA13nUf8qQe7QVxXRBh5faHVZB0MI0K4oRBzbhZCU3Kys1wghZCBZAcc6zmHNuedwvvZCuAtlgyILdI552rDf3ylAeVzcgNSP1SfvImnKjsruShBw2GyFipjMZD"
response_url = "https://graph.facebook.com/v2.6/me/messages?access_token="
sh_url = "https://sandbox.shiphawk.com/api/v4/rates?api_key="
sh_key = "36d461fe37c5f0172baab2f51258702c"

test = '{"items":[{"length": "5", "width" : "10","height": "11","weight": "10","value": 10.00 }],"origin_address":{ "zip": "94546"}, "destination_address":{ "zip": "93405"}}'

def send_text_message(sender, text):
    response = {"recipient": {"id": sender}, "message": {"text": text}}
    r = requests.post(response_url + token, json=response)
    print(r.text)

def request_rate():
    r = requests.post(sh_url + sh_key, json=json.dump(test))
    print(r.text)
    return r.text

@app.route("/")
def hello():
    return "Hello world!"


@app.route("/webhook", methods=['GET'])
def webhook_init():
    if request.args.get('hub.verify_token') == 'sbhacks2016':
        return request.args.get('hub.challenge')

@app.route("/webhook", methods=['POST'])
def message_handler():
    print("MESSAGE EVENTS")
    jsonData = request.get_json()
    print(jsonData)
    message_events = jsonData["entry"][0]["messaging"]
    for message in message_events:
        print("new message")
        print(message)
        sender = message["sender"]["id"]
        if "message" in message and "text" in message["message"]:
            print("sending text message")
            text = message["message"]["text"]
            print("text read " + text)
            send_text_message(sender, "sup")
            send_text_message(sender, request_rate())
    return ('', 200)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
