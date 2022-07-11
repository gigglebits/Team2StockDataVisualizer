from APIQuery import DataQuery
from DataFilter import *
from DataVisualizer import *
from DisplayResults import *
from FrontEnd import *
from ResultGraphing import *

#query uses the arguments ticker, function, and interval.
data = DataQuery.query('TMUS', '5min', 'TIME_SERIES_INTRADAY')
print(data)