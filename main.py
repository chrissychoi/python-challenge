import os
import csv


Financial Analysis = 

#cite csv file directory
budgetData_csvpath = os.path.join(C:/Users/Christopher/UT-TOR-DATA-PT-01-2020-U-C/03-Python/Instructions/PyBank/budget_data.csv)

#load csv file, newline separated by no space
with open(budgetData_csvpath, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #skip first row (header)
    next(csv_reader)

    #loop through rows in csv reader
    for row in csv_reader
        #add 1 to variable for every row detected, save the header row
        numberOfMonths = sum(1 for row in csv_reader)
        #Total profit and losses: sum of the values in row 1
        totalProfitLosses = sum(int(row[1]))
        greatestProfit = max(int(row[1]))
        greatestProfitDate = 
        greatestLosses = min(int(row[1]))


Financial Analysis = {"Total Months": "Rex",
           "Total": "dog",
           "Average Change": 21,
           "Greatest Increase in Profits": ["barking", "eating", "sleeping", "loving my owner"],
           "Greatest Decrease in Profits": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}

