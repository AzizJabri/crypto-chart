from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("api_key")


def get_price_daily():
    urlbtc = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
    urleth = 'https://api.cryptowat.ch/markets/kraken/ethusd/ohlc'
    interval = 1800
    parameters = {
    'after':int(time.time()-(86400-interval)),
    'periods':[interval]
    }
    headers = {
    'Accepts': 'application/json',
    'X-CW-API-Key': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(urlbtc, params=parameters)
        data = json.loads(response.text)
        labels = []
        priceBtc = []
        priceEth = []
        for item in data['result'][str(interval)]:
            labels.append(datetime.utcfromtimestamp(item[0]).strftime('%H:%M'))
            priceBtc.append(item[1])
        response = session.get(urleth, params=parameters)
        data = json.loads(response.text)
        for item in data['result'][str(interval)]:
            priceEth.append(item[1])
        return [labels,priceBtc,priceEth]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)  

def get_price_weekly():
    url = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
    urleth = 'https://api.cryptowat.ch/markets/kraken/ethusd/ohlc'
    interval = 21600
    parameters = {
    'after':int(time.time()-(7*86400-interval)),
    'periods':[interval]
    }
    headers = {
    'Accepts': 'application/json',
    'X-CW-API-Key': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        labels = []
        priceBtc = []
        priceEth = []
        for item in data['result'][str(interval)]:
            labels.append(datetime.utcfromtimestamp(item[0]).strftime('%d/%m|%H:%M'))
            priceBtc.append(item[1])
        response = session.get(urleth, params=parameters)
        data = json.loads(response.text)
        for item in data['result'][str(interval)]:
            priceEth.append(item[1])
        return [labels,priceBtc,priceEth]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e) 

def get_price_monthly():
    url = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
    urleth = 'https://api.cryptowat.ch/markets/kraken/ethusd/ohlc'
    interval = 86400
    parameters = {
    'after':int(time.time()-(30*interval-interval)),
    'periods':[interval]
    }
    headers = {
    'Accepts': 'application/json',
    'X-CW-API-Key': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        labels = []
        priceBtc = []
        priceEth = []
        for item in data['result'][str(interval)]:
            labels.append(datetime.utcfromtimestamp(item[0]).strftime('%d/%m'))
            priceBtc.append(item[1])
        response = session.get(urleth, params=parameters)
        data = json.loads(response.text)
        for item in data['result'][str(interval)]:
            priceEth.append(item[1])
        return [labels,priceBtc,priceEth]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e) 

def get_price_yearly():
    url = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
    urleth = 'https://api.cryptowat.ch/markets/kraken/ethusd/ohlc'
    interval = 604800
    parameters = {
    'after':int(time.time()-(52*interval-interval)),
    'periods':[interval]
    }
    headers = {
    'Accepts': 'application/json',
    'X-CW-API-Key': api_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        labels = []
        priceBtc = []
        priceEth = []
        for item in data['result'][str(interval)]:
            labels.append(datetime.utcfromtimestamp(item[0]).strftime('%m/%Y'))
            priceBtc.append(item[1])
        response = session.get(urleth, params=parameters)
        data = json.loads(response.text)
        for item in data['result'][str(interval)]:
            priceEth.append(item[1])
        return [labels,priceBtc,priceEth]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e) 
