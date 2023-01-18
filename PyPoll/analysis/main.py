# Objective 1: Import modules os and csv. Importing numpy in order to use the unique function
import os
import csv

# Objective 2: Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join('..','Resources','election_data.csv')

# Objective 3: Create the lists to store data. Initialize

total_votes=0
candidates_list = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv
found=True
with open(PyPollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # looping through the csv file
    for row in csvreader:
        total_votes=total_votes+1
        # Count the total number of votes
        #count = count + 1
        # Checking the unique names of candidated and store the candidate names to candidatelist
        candidate_name=row[2]
        if candidate_name in candidates_list:
            candidate_index = candidates_list.index(candidate_name)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates_list.append(candidate_name)
            vote_count.append(1)

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
candidate_roster=zip(candidates_list,percentages,vote_count)

print("Election Results")  
print("-------------------------")
print("Total Votes: " + str(total_votes)) 
print("-------------------------")
for a,b,c in candidate_roster:
    print(f'{a}: {b}% ({c})')
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write to a text file: election summary analysis in text.txt format
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("-------------------------\n")
    for i in range(len(candidates_list)):
        text.write(candidates_list[i] + ": " + str(percentages[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + winner+ "\n")
    text.write("-------------------------")

 