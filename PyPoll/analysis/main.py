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
    percentage =vote_count[i]/(total_votes)*100
    percentages.append(percentage)

candidate_roster=zip(candidates_list,vote_count,percentages)

#print(candidate_roster)
#print(percentages)
#first_candidate_vote=0
#second_cadidate_vote=0
#third_candidate_vote=0
    
#if candidate_name[0]==candidates_list[2]:
    #first_cadidate_vote=first_candidate_vote+1
    #vote_count.append(first_cadidate_vote)
        #found=True
        # Create a set from the candidatelist to get the unique candidate names
    #for x in set(candidate_list):
        #unique_candidate.append(x)
        # y is the total number of votes per candidate
        #y = candidate_list.count(x)
        #vote_count.append(y)
        # z is the percent of total votes per candidate
        #z = (y/count)*100
        #vote_percent.append(z)
        
    #winning_vote_count = max(vote_count)
    #winner = unique_candidate[vote_count.index(winning_vote_count)]

#print(int(total_votes))
#print(vote_count)
#print(f'{candidate_roster[candidate_name]}')

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(total_votes))    
print("-------------------------")
#for i in range(len(candidates_list)):
#for candidates_list,vote_count,percentages in candidate_roster:
    #print(f'{candidates_list}  : {percentages}')
#print(*candidate_roster)
for a,b,c in candidate_roster:
    print(*(a,c))
#print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

#with open('election_results.txt', 'w') as text:
    #text.write("Election Results\n")
    #text.write("---------------------------------------\n")
    #text.write("Total Vote: " + str(count) + "\n")
    #text.write("---------------------------------------\n")
    #for i in range(len(set(unique_candidate))):
      #  text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
   # text.write("---------------------------------------\n")
    #text.write("The winner is: " + winner + "\n")
    #text.write("---------------------------------------\n")