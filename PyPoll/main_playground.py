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

#Print first part of results in GitBash so that they don't loop 
print(f'Election Results')
print(f'---------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------')


    #Calculates percentage of votes for each candidate
    for candidate in candidate_votes_dict:
        percentage = round(float(candidate_votes_dict[candidate])/float(total_votes) * 100, 3)

        def candidate_data():
            print(f'{candidate}: {percentage}% ({candidate_votes_dict[candidate]})')
            
        candidate_data()

