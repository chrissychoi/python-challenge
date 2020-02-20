import os
import csv

budgetData_csvpath = os.path.join("python-challenge/PyBank/budget_data.csv")

with open(budgetData_csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader,None)

    #create empty lists for values reusing purposes
    dates = []
    profitOrLosses = []

    for row in csv_reader:

        #Headers (csv column nicknames)
        date = row[0]
        profitLosses = row[1]

        #Subbing csv values into empty lists above
        dates.append(date)
        profitOrLosses.append(int(profitLosses))
            
#Equations for assignment objectives
#sum of profit and losses
total = sum(profitOrLosses)
# average of sum over number of months included
averageProfit = total/len(dates)

#max profit
greatestProfit = int(max(profitOrLosses))
#using index() to identify max value's position/coordination in csv, in this case it is col[25]
maxDex = profitOrLosses.index(greatestProfit)
#then apply the index onto a different item for the associated value of the referred cell/value above
maxDate = dates[maxDex]

#'max' losses
greatestLosses = int(min(profitOrLosses))
minDex = profitOrLosses.index(greatestLosses)
minDate = dates[minDex]

print("Total number of months included: " + str(len(dates)))
print("The net total amounf of 'Profit/Losses' over the entire period: $ " + str(total))
print("The average of the changes in 'Profit/Losses' over the entire period: $ " + str(averageProfit))
print("The greatest increase in profits (date and amount) over the entire period: $ " + str(greatestProfit) + " on " + maxDate)
print("The greatest decrease in losses (date and amount) over the entire period: $ " + str(greatestLosses) + " on " + minDate)

with open("python-challenge/PyBank/Output.txt", "w") as text_file:
    print(f"Total number of months included: " + str(len(dates)), file=text_file)
    print(f"The net total amounf of 'Profit/Losses' over the entire period: $ " + str(total), file=text_file)
    print(f"The average of the changes in 'Profit/Losses' over the entire period: $ " + str(averageProfit), file=text_file)
    print(f"The greatest increase in profits (date and amount) over the entire period: $ " + str(greatestProfit) + " on " + maxDate, file=text_file)
    print(f"The greatest decrease in losses (date and amount) over the entire period: $ " + str(greatestLosses) + " on " + minDate, file=text_file)