from flask import Flask, render_template, jsonify
import requests as r
import json
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

@app.route('/')
@app.route('/home')
def home():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return render_template("bootstrap.html", value1 = data['compra'], value2 = data['venta'], value3 = data['promedio'], value4 = "{:,.0f}".format(int(data['bitcoin'])))

@app.route('/api')
def api():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False)
