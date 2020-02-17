import os
import csv



#cite csv file directory
budgetData_csvpath = os.path.join("python-challenge/PyBank/budget_data.csv")

profitOrLosses = []

#load csv file, newline separated by no space
with open(budgetData_csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader,None)

    #loop through rows in csv reader
    for row in csv_reader:

        

    #Number of months: add 1 to variable for every row detected, save the header row
        numberOfMonths = sum(1 for row in csv_reader ) 
        print("The total number of months included: " + str(numberOfMonths))

    #Total profit and losses: sum of the values in row 1
        totalProfitLosses = 0
        totalProfitLosses += float(row[1])
        print("The total amount of Profit/Losses over the entire period: $ " + str(totalProfitLosses))

    #The average of the changes in Profit/Losses over the entire period
        averageChanges = totalProfitLosses / numberOfMonths
        print("The average of the anges over the entire period: $ " + str(averageChanges))

    
    #Put profit and losses values into a list 
       # profitOrLosses.append(row[1])
        

    #The greatest increase in profits and date extracted from list 'profitOrLosses'
       # greatestProfit = max(profitOrLosses, key = int)
       # print("The greatest increase in profit is " + row[1] + " on " + row[0])

    #The greatest decrease in losses and date extracted from list 'profitOrLosses'    
       # greatestLosses = min(profitOrLosses, key = int)
       # print("The greatest decrease in losses is " + row[1] + " on " + row[0])

       
   
