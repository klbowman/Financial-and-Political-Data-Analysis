import os
import csv
import sys

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#Lists for storing data
all_candidates = []
unique_candidates = []
Khan_totalvotes = []
Correy_totalvotes = []
Li_totalvotes = []
OTooley_totalvotes = []

#Total number of votes cast
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_voters = len(list(csvreader))

#List of candidates who received votes
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        all_candidates.append(row[2])
    for candidates in all_candidates:
        if candidates not in unique_candidates:
            unique_candidates.append(candidates)
    print(unique_candidates)

#Total number of votes each candidate won
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        if row[2] == "Khan":
            Khan_totalvotes.append(row[0])
        if row[2] == "Correy":
            Correy_totalvotes.append(row[0])
        if row[2] == "Li":
            Li_totalvotes.append(row[0])
        if row[2] == "O'Tooley":
            OTooley_totalvotes.append(row[0])

total_Khan = len(list(Khan_totalvotes))
total_Correy = len(list(Correy_totalvotes))   
total_Li = len(list(Li_totalvotes))     
total_OTooley = len(list(OTooley_totalvotes))

#Calculate percent wins for each candidate
percent_Khan = round(((total_Khan / total_voters) *100),3)
percent_Correy = round(((total_Correy / total_voters) * 100),3)
percent_Li = round(((total_Li / total_voters) * 100),3)
percent_OTooley = round(((total_OTooley / total_voters) * 100),3)

#Winner of election based on popular vote
candidate_rank = {"Khan" : int(percent_Khan), "Correy": int(percent_Correy), "Li": int(percent_Li), "O'Tooley": int(percent_OTooley)}
max_key=max(candidate_rank,key=candidate_rank.get)


#Print election summary
print('Election Results')
print('-------------------------') 
print(f'Total Votes: {total_voters}')
print('-------------------------')       
print(f'Khan: {percent_Khan}% ({total_Khan})') 
print(f'Correy: {round(percent_Correy,3)}% ({total_Correy})') 
print(f'Li: {round(percent_Li,3)}% ({total_Li})') 
print("O'Tooley:" f'{round(percent_OTooley,3)}% ({total_OTooley})') 
print('-------------------------') 
print(f'Winner: {max_key}')
print('-------------------------')    

#Export Summary
output_path = os.path.join("Analysis", "PyPoll_ResultsSummary.txt")

sys.stdout = open(output_path, "w")

print('Election Results')
print('-------------------------') 
print(f'Total Votes: {total_voters}')
print('-------------------------')       
print(f'Khan: {percent_Khan}% ({total_Khan})') 
print(f'Correy: {round(percent_Correy,3)}% ({total_Correy})') 
print(f'Li: {round(percent_Li,3)}% ({total_Li})') 
print("O'Tooley:" f'{round(percent_OTooley,3)}% ({total_OTooley})') 
print('-------------------------') 
print(f'Winner: {max_key}')
print('-------------------------') 

sys.stdout.close()