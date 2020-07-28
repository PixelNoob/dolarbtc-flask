import requests as r
import json
import time
import csv

# Function to turn url int json
def url_json(url):
    json = r.get(url).json()
    return json

# 3 ask prices from lb ads
lb_ask = "https://localbitcoins.com/buy-bitcoins-online/ars/national-bank-transfer/.json"
lb_ask = url_json(lb_ask)

ask_a = float(lb_ask["data"]["ad_list"][1]["data"]["temp_price"])
ask_b = float(lb_ask["data"]["ad_list"][2]["data"]["temp_price"])
ask_c = float(lb_ask["data"]["ad_list"][3]["data"]["temp_price"])

# 3 buy prices from lb ads
lb_buy = "https://localbitcoins.com/sell-bitcoins-online/ars/national-bank-transfer/.json"
lb_buy = url_json(lb_buy)

buy_a = float(lb_buy["data"]["ad_list"][1]["data"]["temp_price"])
buy_b = float(lb_buy["data"]["ad_list"][2]["data"]["temp_price"])
buy_c = float(lb_buy["data"]["ad_list"][3]["data"]["temp_price"])

ask_medium = (ask_a + ask_b + ask_c) / 3
buy_medium = (buy_a + buy_b + buy_c) / 3

medium = (ask_medium + buy_medium) / 2
print ("Precio Bitcoin en Argentina " + "{:,.0f}".format(medium))

# international price of bitcoin in usd from Blockchain.info api
btc = "https://blockchain.info/ticker"
btc = url_json(btc)

price_btc = float(btc["USD"]["15m"])
# print ("El precio internacional del Bitcoin es", price_btc)

# precio del Dolar Bitcoin
buy_dolar_btc = ask_medium / price_btc
sell_dolar_btc = buy_medium / price_btc
dolar_btc = medium / price_btc
bitcoin = "{:.0f}".format(medium)
print ("El precio del Dólar Bitcoin en Argentina es...")
time.sleep(1)
print ("Compra", "{:.2f}".format(buy_dolar_btc))
time.sleep(1)
print ("Venta", "{:.2f}".format(sell_dolar_btc))
time.sleep(1)
print ("Promedio", "{:.2f}".format(dolar_btc))

### Put prices on a csv file

csvfile=open('/root/dolarbtc/dolarbtc/data.csv','w', newline='')
file=csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

file.writerow([time.ctime()])
file.writerow(["compra ", "{:.2f}".format(buy_dolar_btc)])
file.writerow(["venta ", "{:.2f}".format(sell_dolar_btc)])
file.writerow(["promedio ", "{:.2f}".format(dolar_btc)])
file.writerow(["Bitcoin ", bitcoin])

