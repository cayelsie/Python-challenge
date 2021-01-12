import os
import csv

#build relative file path
Pybank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []

#List to store the monthly changes
monthly_changes = []

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

#open the file as csv
with open(Pybank_csv, newline = '', encoding = 'utf-8') as csvfile:
    
    #decipher the file for python
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header, store the header row and print it
    csvheader = next(csvfile)
    print(f"Header: {csvheader}")

    #i don't know if the for j part works, but the for i works great to transform that list into integers. I doubt the for j part works.
    for row in csvreader:
        length = len(row[1])
        date.append(row[0])
        profit_loss.append(row[1])
        for i in range(0, len(profit_loss)): 
            profit_loss[i] = int(profit_loss[i])
        #change the data in index [1] to integers to be able to do calculations
        for j in range(0, len(row[1])):
            row[1] = int(row[1]) 


#Write steps within the whole csv file for calculating the monthly profit/loss change. This will be stored in a separate list for later -this doesn't work
 #This code does not work with the row + 1 or using x+1 etc.    

        for x in range(length):
            if x < length -1:
                difference = row[x+1][1] - row[x][1]
                monthly_changes.append(difference)
            for y in range(0, len(monthly_changes)):
                monthly_changes[y] = int(monthly_changes[y])
   
   
    print(f'{monthly_changes}')  


#All of these work with the functions
print(len(date))
print(f'{max(profit_loss)}')
print(f'{sum(profit_loss)}')


print(f'{average_change(profit_loss)}')
print(f'{monthly_change(profit_loss)}')