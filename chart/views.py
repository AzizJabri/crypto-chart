from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from datetime import datetime

def get_price():
    url = 'https://api.cryptowat.ch/markets/kraken/btcusd/ohlc'
    urleth = 'https://api.cryptowat.ch/markets/kraken/ethusd/ohlc'
    interval = 1800
    parameters = {
    'after':int(time.time()-(86400-interval)),
    'periods':[interval]
    }
    headers = {
    'Accepts': 'application/json',
    'X-CW-API-Key': 'PL91ULH087ORVGZQ8AV0',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        labels = []
        price = []
        for item in data['result'][str(interval)]:
            labels.append(datetime.utcfromtimestamp(item[0]).strftime('%H:%M'))
            price.append(item[1])

        return [labels,price]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)  

# Create your views here.
def ApiView(request):
    data = get_price()
    return JsonResponse({
        'labels': data[0] ,
        'price' : data[1]
    })

class HomeView(View):
    def get(self,request,*arg,**kwarg):
        return render(request,'chart/charts.html')