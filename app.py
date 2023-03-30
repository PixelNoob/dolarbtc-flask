from flask import Flask, render_template, jsonify
import requests as r
import json
from flask_bootstrap import Bootstrap
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()
limiter = Limiter(
    app,
    default_limits=["250 per day", "50 per hour"])
limiter.key_func = get_remote_address

@app.route('/')
@app.route('/home')
def home():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return render_template("bootstrap.html", value1 = data['compra'], value2 = data['venta'], value3 = data['promedio'], value4 = "{:,.0f}".format(int(data['bitcoin'])))

@app.route('/api')
@limiter.limit("1/second", override_defaults=False)
def api():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=False)
