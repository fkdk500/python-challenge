#--------------
# Steps
#---------------
#1.Import modules os and csv, defining the link for targeted file, Declear variables, open and read the file
#2.looping through the csv file and grab the decleared variables, create additional for loop to grab remaining decleared variable
#3.Zip diffrent poll lists to make them immutable
#4. Printing the required summary anlysis and write them on specific formats and location

# Import os and csv modules
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

with open(PyBankcsv) as csvfile:
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
    for i in range(len(profit_losses)-1):
        if i==0:
           change= 0
        #else:
        change = float(profit_losses[i+1]) - float(profit_losses[i])
        change_in_profit.append(change)

    
    greatest_increase_amount= int(max(change_in_profit))
    greatest_decrease_amount= int(min(change_in_profit))
   
  
    month_greater = change_in_profit.index(int(max(change_in_profit)))
    great_increase_date = date [(int(month_greater))+1]
                        
    month_smaller = change_in_profit.index(int(min(change_in_profit)))
    great_decrease_date = date [(int(month_smaller))+1]

#Data type fot decimal numbers should be FloatingPointError rather than integer
average_change = round((sum((change_in_profit)))/(len(change_in_profit)),2)
formated_average_change=round(int(average_change),0)
count=len(month)

#Print summary of anaysis as per the requirement
print("'''text")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(net_total))
print("Average Change: " + "$" + str(FloatingPointError(average_change)))
print("Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_amount) + ")")
print("Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_amount)+ ")")
print("----------------------------------------------------------")

#Write finacial anaysis summary on targeted location
with open('financial_analysis.txt', 'w') as text:
    text.write("'''text \n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(net_total) +"\n")
    text.write("    Average Change: " + '$' + str(formated_average_change) + "\n")
    text.write("    Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_amount) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_amount) + ")\n")
    text.write("'''")
            


