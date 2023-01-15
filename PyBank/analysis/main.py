# Import modules os and csv

import os
import csv

#  Set the path for the CSV file in PyBankcsv

PyBankcsv = os.path.join('..', 'Resources', 'budget_data.csv')

# Lists to store data. 
month=[]
profit_losses = []
change_in_profit = []
date = []
year=[]

# Initialize the variables as required.
 
count = 0
total_profit = 0
greatest_increase=0
greatest_decrease=0
date_great_increase=0
date_great_decrease=0

# Open the CSV as csvfile:

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # looping through all rows of csvreader
    for row in csvreader:    
      
      # Add/append the date then split into month and year using split method/function
      date.append(row[0])
      split_date=row[0].split("-")
      month.append(split_date[0])
      year.append(split_date[1])

      # Append each row data under the profit/losses column and add with next row to calculate total profit
      profit_losses.append(row[1])
    #
    for i in range(len(profit_losses)):
        if i==0:
           net_profit=0
        else:
            net_profit= int(profit_losses[i]) - int(profit_losses[i-1])
            if (net_profit >= greatest_increase):
                date_great_increase = date[i]
                greatest_increase = net_profit
            if (net_profit <= greatest_increase):
                date_great_decrease = date[i]
                greatest_decrease = net_profit
        change_in_profit.append(net_profit)
        i=i+1
average_change = round(sum(change_in_profit)/(len(change_in_profit)-1),2)
      
print(int(average_change))
print(int(len(month)))
print(str(date_great_increase))
print(int(greatest_increase))
