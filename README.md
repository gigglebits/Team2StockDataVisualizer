# Team2StockDataVisualizer

This repo will be used by Scrum Team 2 for Mizzou's IT4320s Summer 2022 semester project 3, Stock Data Visualizer. 

This project will use the following python modules to get data, ask for parameters, and then display formatted results:

Front End - TKinter
API Querying - Requests
Graphing - pygal
Displaying of Results - lxml



This project will be divided into several modules: 

.Front End

  ..This will be a Graphical User Interface that will be able to allow the user to enter the preferred parameter's to filter the data.
  
.API Querying 

  ..This will be the module will provide a class that will allow for input from the front end and then will query the API for the sought after data. 
  
.Filtering Results

  ..If results are not filterable through the API querying this module will be necessary to filter the results. 
  
.Graphing Results

  ..This will take the results from the query or from the filtering and will graph them using pygal. 
  
.Displaying Results

  ..This will take the graph made with pygal and will display them through the web browser. 
  
.Main

  ..Main will bring everything together. It may just end up being called data visualizer or something, but will serve as the main program to run. 
