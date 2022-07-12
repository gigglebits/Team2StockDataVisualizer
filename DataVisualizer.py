from APIQuery import DataQuery
from DataFilter import *
from FrontEnd import *
from ResultGraphing import *

###########Code for Front End#######################
#Front end will bring up a GUI for user to put in their input of (string) stock symbol, (bool) Chart type (0 for bar, 1 for line), (int) Time Series 1 for Intraday 2 for Daily 3 for Weekly 4 for Monthly
# (dict) Start date, (dict) End Date






#Front end needs to return type queryInput from the queryInput class in the dataTypeClases.py file
###########End Code for Front End###################


###########Start Code for Query#####################

#this is a sample query to the APIQuery.py file. 
#query uses the arguments ticker, function, and interval.
data = DataQuery.query('TMUS', 'TIME_SERIES_INTRADAY', '5min')
print(data)
###########End Code for Query######################


###########Start Code for DataFilter####################



###########End Code for DataFilter######################

###########Start Code for Result Graphing###############



###########End Code for Result Graphing################

###########Start Code for DisplayResult################


##########End Code for Display Results#################

