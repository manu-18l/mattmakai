import os
from flask import Flask, request, Response


app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET', None)


@app.route('/slack', methods=['POST'])
def inbound():
    if request.form['token'] == SLACK_WEBHOOK_SECRET:
        channel = request.form['channel_name']
        username = request.form['user_name']
        text = request.form['text']
        inbound_message = username + " in " + channel + " says: " + text
        print(inbound_message)
    return Response(), 200


@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)
