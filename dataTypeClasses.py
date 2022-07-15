
#ticker is typ string (str)
#chartType is type (bool) 0 for bar, 1 for line
#timeSeries is type integer (int)
#startDate is type dictionary (dict)
#endDate is type dictionary (dict)
class queryInput:
    def __init__(self, ticker, chartType, timeSeries, interval, startDate, endDate):
        self.ticker = ticker
        self.chartType = chartType
        self.timeSeries = timeSeries
        self.interval = interval
        self.startDate = startDate
        self.endDate = endDate




#example of a queryInput object
#object = queryInput('TMUS', 0, 3, {"year" : 2007, "month" : 11, "day" : 12}, {"year" : 2008, "month" : 1, "day" : 5})

