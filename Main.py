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

data = DataQuery.query(userInput.ticker, userInput.timeSeries, userInput.interval)

#this is a sample query to the APIQuery.py file. 
#query uses the arguments ticker, function, and interval.
#data = DataQuery.query('TMUS', 'TIME_SERIES_INTRADAY', '5min')
#print(data)
###########End Code for Query######################


###########Start Code for DataFilter####################

filteredData = dateFilter.datefilter(data, userInput.startDate, userInput.endDate)

###########End Code for DataFilter######################

###########Start Code for Result Graphing###############

graphResults.graph(filteredData)

###########End Code for Result Graphing################
