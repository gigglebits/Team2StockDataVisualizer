# Team2StockDataVisualizer

This repo will be used by Scrum Team 2 for Mizzou's IT4320s Summer 2022 semester project 3, Stock Data Visualizer. 

NOTE - This project will use the following python modules to get datA and then display formatted results. YOU NEED TO INSTALL THESE MODULES TO RUN THE PROGRAM:


API Querying - Requests

Graphing - pygal

Displaying of Results - lxml





*****Once all Modules are installed you can run the code by running Main.py*****










This project is divided into several modules: 

.Front End

  ..FrontEnd.py - This will be a command line tool to get the required parameters from the user. 
  
.API Querying 

  ..APIQuery.py - This will be the module will provide a class that will allow for input from the front end and then will query the API for the sought after data. 
  
.Filtering Results

  ..DataFilter.py - If results are not filterable through the API querying this module will be necessary to filter the results. 
  
.Graphing Results

  ..ResultGraphing.py - This will take the results from the query or from the filtering and will graph them using pygal. Then using lxml will render the results into a web browser. 
  
.Main

  ..Main.py - Main will bring everything together and will be the script to run the program.  
