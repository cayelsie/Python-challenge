import os
import csv

#build relative file path
Pypoll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Lists to store data
voter_id = []
county = []
candidates = []

#Set initial variable for the number of votes
total_votes = 0

#Set initial variable for each candidate vote counter
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0

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

        #loop through and make a list of candidates that obtained votes, without duplicates
        if row[2] not in candidates:
            candidates.append(row[2])

        #Count number of votes for each candidate
        if row[2] == "Khan":
            Khan = Khan + 1
        if row[2] == "Correy":
            Correy = Correy + 1
        if row[2] == "Li":
            Li = Li + 1
        if row[2] == "O'Tooley":
            O_Tooley = O_Tooley + 1

#Calculate percent for each candidate
Khan_percent = round((Khan/total_votes) * 100, 3)
Correy_percent = Correy/total_votes
Li_percent = Li/total_votes
O_Tooley_percent = O_Tooley/total_votes


print(f'Election Results')
print(f'---------------------------')
print(f'Total Votes: {total_votes}')
print(f'---------------------------')
print(f'Khan: {Khan_percent}% ({Khan})')
