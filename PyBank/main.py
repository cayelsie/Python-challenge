#Modules
import os
import csv

#build relative file path
Pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#List to store the monthly changes?
change_list = []

#List to store the dates that go with the monthly change calcs
date_list = []

#List to store the monthly changes and dates zipped together
change_date_list = []

#Write a function for calculating the average for monthly profit/loss changes - because I just want to include a function for practice!
def average_change(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return round(total/(len(numbers)),2)


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

        #subtract profit/loss value in previous row from value in profit/loss column in next row. Append the changes to a new list, also append the corresponding dates to a new list. 
        monthly_change = int(row[1]) - previous_row
        #Note that it's only storing AFTER the first row has passed
        if total_months >= 1:
            change_list.append(monthly_change)
            date_list.append(row[0])
        previous_row = int(row[1])


        #Start counter for counting rows: aka number of months
        total_months = total_months + 1

       #Can easily get an average from change_list and also search max/min values in that list...but how in the world do I do that in the original list to be able to match it up with original date?? Append original list with change data??

#Zip the list of dates and changes together
change_date_list = zip(date_list, change_list)

#Set initial variables for max increase and decrease
max_increase = 0
max_decrease = 0

for date in change_date_list:
    if date[1] > max_increase:
        max_increase = date[1]
        max_date = date[0]
    if date[1] < max_decrease:
        max_decrease =  date[1]
        min_date = date[0] 
    
    
#Print output to terminal. Need to save everything into a text file output - is the output to the terminal from the text file or do I do as below??
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_sum}')
print(f'Average Change: ${average_change(change_list)}')
print(f'Greatest Increase in Profits: {max_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {min_date} (${max_decrease})')

