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

#Set initial variable for the highest amount of votes (winner)
max_votes = 0


#open the file as csv
with open(Pypoll_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row
    csvheader = next(csvfile)
  
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

    #Print first part of results in GitBash so that they don't loop later
    print(f'Election Results')
    print(f'---------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'---------------------------')


    #Calculates percentage of votes for each candidate
    for candidate in candidate_votes_dict:
        percentage = round(float(candidate_votes_dict[candidate])/float(total_votes) * 100, 3)

        #Write function to display and print vote information for each candidate
        def candidate_data():
            print(f'{candidate}: {percentage}% ({candidate_votes_dict[candidate]})')

        #call the function for printing candidate information in GitBash    
        candidate_data()

        #Search for the largest vote count by candidate. Store the largest and store the accompanying candidate 
        if candidate_votes_dict[candidate] > max_votes:
            max_votes = candidate_votes_dict[candidate]
            winner = candidate

    #Print out the winner in GitBash 
    print(f'---------------------------') 
    print(f'Winner: {winner}')
    print(f'---------------------------')    
