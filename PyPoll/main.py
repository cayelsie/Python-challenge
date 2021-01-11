import os
import csv

#build relative file path
Pypoll_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Lists to store data
voter_id = []
county = []
candidate = []

#open the file as csv
with open(Pypoll_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row and print it
    csvheader = next(csvfile)
    print(f"Header: {csvheader}")