
#ticker is typ string (str)
#chartType is type (bool)
#timeSeries is type integer (int)
#startDate is type dictionary (dict)
#endDate is type dictionary (dict)
class queryInput:
    def __init__(self, ticker, chartType, timeSeries, startDate, endDate):
        self.ticker = ticker
        self.chartType = chartType
        self.timeSeries = timeSeries
        self.startDate = startDate
        self.endDate = endDate