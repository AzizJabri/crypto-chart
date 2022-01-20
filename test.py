from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
from datetime import datetime

url = 'https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc'
parameters = {
  'after':int(time.time()-(86400-3600)),
  'periods':[3600]
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
  for item in data['result']['3600']:
      item[0] = datetime.utcfromtimestamp(item[0]).strftime('%H:%M')
      print(item)
  #print(data['result']['3600'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)