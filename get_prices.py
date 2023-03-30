import requests as r
import json
from datetime import datetime, date, timedelta

hora = datetime.now()
hora = datetime.strftime(hora,'%d-%m-%Y %H:%M:%S')
try:
    belo = r.get('https://criptoya.com/api/belo/btc/ars/0.1').json()
    lemon = r.get('https://criptoya.com/api/lemoncash/btc/ars/0.1').json()
except Exception as e:
    print(e)

def get_ask():
    ask_medium=(belo['ask'] + lemon['ask']) / 2
    return round(ask_medium, 2)

def get_buy():
    buy_medium = (belo['bid'] + lemon['bid']) / 2
    return round(buy_medium, 2)

def get_btc():
    medium = round((get_ask() + get_buy()) / 2)
    return medium


def get_dolarbtc():
    btc = r.get("https://blockchain.info/ticker").json()
    price_btc = float(btc["USD"]["15m"])
    list = []
    list.append(round(get_ask()/price_btc,2))
    list.append(round(get_buy()/price_btc,2))
    list.append(round(get_btc()/price_btc,2))
    return list

def create_dict():
    dict = {}
    list = get_dolarbtc()
    dict.update({'compra':list[0]})
    dict.update({'venta':list[1]})
    dict.update({'promedio':list[2]})
    dict.update({'bitcoin':get_btc()})
    dict.update({'time':hora})
    return dict

data = json.dumps(create_dict())

## write to a json file
with open('data.json', 'w') as f:
    f.write(data)
