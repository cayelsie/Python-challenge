import os
import csv

#build relative file path
Pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#List to store the monthly changes?


#write a function for summing the profits/losses
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#Write a function for calculating the average for monthly profit/loss changes. This is probably not going to be used in final version but works to get the correct number.
def average_change(numbers):
    length = len(numbers)
    total = 0
    for x in range(length):
        if x < length - 1:
            difference = numbers[x + 1] - numbers[x]
            total += difference
    return total/(length-1)

#Write a function for calculating the monthly profit/loss change. This will be stored in a separate list for later
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

#open the file as csv
with open(Pybank_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row 
    csvheader = next(csvfile)
 
    #i don't know if the for j part works, but the for i works great to transform that list into integers. I doubt the for j part works.
    for row in csvreader:
       #Start counter for counting rows: aka number of months
        total_months = total_months + 1

        #loop through and calculate sum
        total_sum = total_sum + int(row[1])
        
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_sum}')