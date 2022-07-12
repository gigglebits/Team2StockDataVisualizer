from requests import *

class DataQuery:
    def query(ticker, function, interval):
        apiKey = "UTGQEG3HJTTA6S8T"
        url = 'https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&apikey=%s' % (function, ticker, interval, apiKey)
        r = get(url)
        data = r.json()
        return data
            