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
net_total = 0
greatest_increase_amount=0
greatest_decrease_amount=0
great_increase_date=0
great_decrease_date=0

# Open the CSV as csvfile:

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # looping through all rows of csvreader
    for row in csvreader:  
        #Calculate the net  total  through adding the profit/losses
        net_total= net_total+int(row[1])
      
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
           net_profit= 0
        else:
            net_profit= int(profit_losses[i]) - int(profit_losses[i-1])
            if (net_profit >= greatest_increase_amount):
                great_increase_date = date[i]
                greatest_increase_amount = net_profit
            if (net_profit <= greatest_increase_amount):
                great_decrease_date = date[i]
                greatest_decrease_amount = net_profit
        change_in_profit.append(net_profit)
        i=i+1


average_change = round(sum(change_in_profit)/(len(change_in_profit)-1),2)
count=len(month)

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(net_total))
print("Average Change: " + "$" + str(int(average_change)))
print("Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_amount)+ ")")
print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(net_total) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_amount) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_amount) + ")\n")
    text.write("----------------------------------------------------------\n")


