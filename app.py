from flask import Flask, render_template, jsonify
import requests as r
import json
from flask_bootstrap import Bootstrap
from flask import Response

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()

@app.route('/')
@app.route('/home')
def home():
    fname = "data.csv"
    file= open(fname)
    list= []
    for line in file:
        line= line.rstrip()
        words = line.split()
        list.append(words[1][1:])
    return render_template("bootstrap.html", value1 = list[1], value2 = list[2], value3 = list[3], value4 = "{:,.0f}".format(int(list[4])))

@app.route('/api')
def api():
    fname = "data.csv"
    file= open(fname)
    list= []
    for line in file:
        line= line.rstrip()
        words = line.split()
        list.append(words[1][1:])
    dict = {}
    dict.update({'compra':float(list[1])})
    dict.update({'venta':float(list[2])})
    dict.update({'promedio':float(list[3])})
    dict.update({'bitcoin':int(list[4])})    
    return jsonify(dict)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=False)
