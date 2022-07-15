from APIQuery import *
from DataFilter import *
from FrontEnd import *
from ResultGraphing import *

###########Code for Front End#######################
#Front end will bring up a GUI for user to put in their input of (string) stock symbol, (bool) Chart type (0 for bar, 1 for line), (int) Time Series 1 for Intraday 2 for Daily 3 for Weekly 4 for Monthly
# (dict) Start date, (dict) End Date

userInput = FrontEnd.frontEnd()

#Front end needs to return type queryInput from the queryInput class in the dataTypeClases.py file
###########End Code for Front End###################

###########Start Code for Query#####################

#Makes sense of the time series code in the userInput object. 
if userInput.timeSeries == 1:
    ts = "TIME_SERIES_INTRADAY"
elif userInput.timeSeries == 2:
    ts = "TIME_SERIES_DAILY"
elif userInput.timeSeries == 3:
    ts = "TIME_SERIES_WEEKLY"
else:
    ts = "TIME_SERIES_MONTHLY"

#Makes sense of the interval code in the userInput object. 
if userInput.interval == 1:
    interval = "1min"
elif userInput.interval == 2:
    interval = "5min"
elif userInput.interval == 3:
    interval = "15min"
elif userInput.interval == 4:
    interval = "30min"
else:
    interval = "60min"

#Calls the query object to make the api call. 
data = DataQuery.query(userInput.ticker, ts, interval)

#this is a sample query to the APIQuery.py file. 
#query uses the arguments ticker, function, and interval.
#data = DataQuery.query('TMUS', 'TIME_SERIES_INTRADAY', '5min')
#print(data)
###########End Code for Query######################


###########Start Code for DataFilter####################

filteredData = dateFilter.dateFilter(data, userInput.startDate, userInput.endDate)

###########End Code for DataFilter######################

###########Start Code for Result Graphing###############

graphResults.graph(filteredData, userInput.chartType)

###########End Code for Result Graphing################
