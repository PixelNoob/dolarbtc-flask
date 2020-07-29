import requests as r
import json

def get_ask():
    lb_ask = r.get("https://localbitcoins.com/buy-bitcoins-online/ars/national-bank-transfer/.json").json()
    ask_a = float(lb_ask["data"]["ad_list"][1]["data"]["temp_price"])
    ask_b = float(lb_ask["data"]["ad_list"][2]["data"]["temp_price"])
    ask_c = float(lb_ask["data"]["ad_list"][3]["data"]["temp_price"])
    ask_medium = (ask_a + ask_b + ask_c) / 3
    return round(ask_medium, 2)

def get_buy():
    lb_buy = r.get("https://localbitcoins.com/sell-bitcoins-online/ars/national-bank-transfer/.json").json()
    buy_a = float(lb_buy["data"]["ad_list"][1]["data"]["temp_price"])
    buy_b = float(lb_buy["data"]["ad_list"][2]["data"]["temp_price"])
    buy_c = float(lb_buy["data"]["ad_list"][3]["data"]["temp_price"])
    buy_medium = (buy_a + buy_b + buy_c) / 3
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
    return dict

data = json.dumps(create_dict())

## write to a json file
with open('/root/dolarbtc/dolarbtc/data.json', 'w') as f:
    f.write(data)
