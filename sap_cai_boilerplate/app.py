#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template
import json, requests

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # use methods = GET


@app.route('/talk', methods=['POST'])
def talk():

    # sample code for parsing data received from chatbot
    #data = json.loads(request.get_data().decode())
    #print(data)

    # sample code for making an API call and parsing response
    #r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    #r = r.json()
    #print(r.keys())

    answer = 'Roger That!'
    return respond(answer)

def respond(answer):
    return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': '%s' % (answer)
    }],
    # conversation={
    #   'memory': { 'name': value}
    # }
)

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data().decode()))
  return jsonify(status=200)


if __name__ == "__main__":

    # local testing
    #app.run(debug=True, host = '0.0.0.0', port = 5000)

    # for Heroku deployment
    #port = int(os.environ['PORT'])
    #app.run(port=port, host="0.0.0.0")

    pass
