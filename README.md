# python-challenge
# Project Description <h1> 
  This repository contains two separate projects, PyBank and PyPoll.
  
  **PyBank** is a python script written to analyze two columns of financial data in a .csv file. The first column of data is dates, and the second column of data is monetary values.  
  
  The **PyBank** folder contains:
  * An *Analysis* folder with a .txt file of summary outputs
  * A *Resources* folder that contains the budget_data.csv file used in this analysis 
  * A python file titled *main.py*
  
    The *main.py* file in the **PyBank** folder:
      * Counts the total number of rows in the first column of the csv file
      * Calculates the difference between two successive rows in a series 
        * Differences are stored as a new list ("changes")
        * The average, and maximum and minimum values are determed from the "changes" list 
      * Using list indexes, maximum and minimum values from the "changes" list are associated with the first column of data in the csv file
  
  **PyPoll** is a python script written to analyze three columns of election data in a .csv file. The first column of data contains voter identification numbers, the second column contains voter county, and the third column contains candidates last names.  
  
  The **PyPoll** folder contains:
  * An *Analysis* folder with a .txt file of summary outputs
  * A *Resources* folder that contains the election_data.csv file used in this analysis 
  * A python file titled *main.py*
  
    The *main.py* file in the **PyBank** folder:
      * Creates a new list of unique candidate names from a series
      * Calculates the total number of votes 
        * Calculates the total and percentage of votes assinged to each candidate
      * Creates a dictionary of candidate names and percentage of votes won 
        * Uses the dictionary to identify the candidate with the greatest percentage of votes
  
