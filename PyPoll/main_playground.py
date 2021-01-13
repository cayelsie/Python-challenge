import os
import csv

#build relative file path
Pypoll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# List to hold names of candidates who received votes
candidates = []

#make a dictionary that will hold each candidate and their number of votes
candidate_votes_dict = {}

#Set initial variable for the number of votes
total_votes = 0

#Set initial variable for the winner's name
winner = ""

#Set intiial variable of winner's votes to 0
winner_votes = 0

#Set initial variable of winner's percentage to 0
winner_percentage = 0

#open the file as csv
with open(Pypoll_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row and print it
    csvheader = next(csvfile)
    print(f"Header: {csvheader}")

    #Loop through the rows in the list
    for row in csvreader:

        #loop through and use a counter to calculate how many votes total
        total_votes = total_votes + 1

        
        #Set a value for the name of the candidate
        candidate = row[2]

        #loop through and make a list of candidates that obtained votes, without duplicates
        if row[2] not in candidates:
            candidates.append(candidate)
        
        #Start tallying the votes for each candidate and store with candidate's name in dictonary
            candidate_votes_dict[candidate] = 0
        candidate_votes_dict[candidate] = candidate_votes_dict[candidate] + 1

        #
 

print(candidate_votes_dict)

#Calculate percent for each candidate
Khan_percent = round((Khan/total_votes) * 100, 3)
Correy_percent = round((Correy/total_votes) * 100, 3)
Li_percent = round((Li/total_votes) * 100, 3)
O_Tooley_percent = round((O_Tooley/total_votes) * 100, 3)



print(f'Election Results')
print(f'---------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------')
print(f'Khan: {Khan_percent}% ({Khan})')
print(f'Correy: {Correy_percent}% ({Correy})')
print(f'Li: {Li_percent}% ({Li})')
print(f"O'Tooley: {O_Tooley_percent}% ({O_Tooley})")
print(f'---------------------------')
print(f'Winner:')
print(f'---------------------------')