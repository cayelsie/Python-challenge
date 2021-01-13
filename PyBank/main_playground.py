#Modules
import os
import csv

#build relative file path
Pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#List to store the monthly changes?
change_list = []

#List to store the dates that go with the monthly change calcs
date_list = []

change_date_list = []

#Write a function for calculating the average for monthly profit/loss changes. This is probably not going to be used in final version but works when I pull out the profit/loss data into its own list.
def average_change(numbers):
    length = len(numbers)
    total = 0
    for x in range(length):
        if x < length - 1:
            difference = numbers[x + 1] - numbers[x]
            total += difference
    return total/(length-1)

#Write a function for calculating the monthly profit/loss change without the average. This will be stored in a separate list for later.
def monthly_change(numbers):
    length = len(numbers)
    total = 0
    for x in range(length):
        if x < length -1:
            difference = numbers[x + 1] - numbers[x]
            monthly_changes.append(difference)
            for y in range(0, len(monthly_changes)):
                monthly_changes[y] = int(monthly_changes[y])
   
    print(f'{monthly_changes}')

#Set variable for total months to 0 initially for the counter
total_months = 0
#Set variable for total sum to 0 initially
total_sum = 0
#Set variable for previous row to 0 initially
previous_row = 0

#open the file as csv
with open(Pybank_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row 
    csvheader = next(csvfile)
 
    #Loop through the rows in the list
    for row in csvreader:

        #loop through and calculate sum
        total_sum = total_sum + int(row[1])

        #subtract profit/loss value in previous row from value in profit/loss column in next row 
        monthly_change = int(row[1]) - previous_row
        if total_months >= 1:
            change_list.append(monthly_change)
            date_list.append(row[0])
        previous_row = int(row[1])


        #Start counter for counting rows: aka number of months
        total_months = total_months + 1

       #Can easily get an average from change_list and also search max/min values in that list...but how in the world do I do that in the original list to be able to match it up with original date?? Append original list with change data??

change_date_list = zip(date_list, change_list)
for dates in change_date_list:
    print(dates)
#Print output to terminal. Need to save everything into a text file output - is the output to the terminal from the text file or do I do as below??
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_sum}')
print(change_date_list)