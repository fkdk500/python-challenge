#--------------
# Steps
#---------------
#1.Import modules os and csv, defining the link for targeted file, Declear variables, open and read the file
#2.looping through the csv file and grab the decleared variables, create additional for loop to grab remaining decleared variable
#3.Zip diffrent poll lists to make them immutable
#4. Printing the required summary anlysis and write them on specific formats and location

#import os and csv modules
import os
import csv

# Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join('..','Resources','election_data.csv')

#Create the lists to store data. Initialize
total_votes=0
candidates_list = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # looping through the csv file
    for row in csvreader:
        # Count the total number of votes
        total_votes=total_votes+1
        # Checking the unique candidates name and store the candidate names in a list 
        candidate_name=row[2]
        if candidate_name in candidates_list:
            candidate_index = candidates_list.index(candidate_name)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates_list.append(candidate_name)
            vote_count.append(1)

#Declear additional variables
percentages = []
max_votes = 0
max_index = 0

#find percentage of vote for each candidate and the winner
for i in range(len(candidates_list)):
    percentage =round((vote_count[i]/(total_votes)*100),3)
    percentages.append(percentage)
    if vote_count[i] > max_votes:
        max_votes = vote_count[i]
        max_index = i
winner = candidates_list[max_index]

#Creating zip or tuples of diffrent Poll lists to make them  immutable
candidate_roster=zip(candidates_list,percentages,vote_count)

#Printing the summary report as per the requirement
print("Election Results")  
print("-------------------------")
print("Total Votes: " + str(total_votes)) 
print("-------------------------")
for a,b,c in candidate_roster:
    print(f'{a}: {b}% ({c})')
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write election result summary analysis on specific file location and in text format
with open('election_results.txt', 'w') as text:
    text.write("'''text\n")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("-------------------------\n")
    for i in range(len(candidates_list)):
        text.write(candidates_list[i] + ": " + str(percentages[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + winner+ "\n")
    text.write("-------------------------\n")
    text.write("'''")

 