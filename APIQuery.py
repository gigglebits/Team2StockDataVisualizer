from requests import *

class DataQuery:
    def __init__(self, compticker, function, interval):
        self.ticker = compticker
        self.function = function
        self.interval = interval
        self.apiKey = "UTGQEG3HJTTA6S8T"

    def query(self):
        url = 'https://www.alphavantage.co/query?function=${self.function}&symbol=${self.ticker}&interval=${self.interval}&apikey=${self.apikey}'
        r = requests.get(url)
        data = r.json()
        return data
            