import os
import csv

#build relative file path
Pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []

#open the file as csv
with open(Pybank_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row and print it
    csvheader = next(csvfile)
    print(f"Header: {csvheader}")

    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
        for i in range(0, len(profit_loss)): 
            profit_loss[i] = int(profit_loss[i]) 

print(len(date))
print(f'{max(profit_loss)}')	