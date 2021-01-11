#import os module (allows us to create file path across operating systems)
import os

#import csv module (allows us to read csv files)
import csv

#read the budget_data csv file
csvpath = os.path.join('Resources/','budget_data.csv')
output_file=os.path.join('output/', 'financial_analysis.txt') #pushes file to output folder

#declare variables
total_months = 0 #sets the initial value of total months of data to 0
profits_losses = [] #creates an empty list for the profits or losses of each transaction
dates = [] #creates an empty list for the dates of each transaction

#open the csv file
with open(csvpath) as csvfile: #don't need to close this loop
    csvreader=csv.reader(csvfile, delimiter=',')
    row_index = 0
    header = next(csvreader) #grabs the first row and determine these as headers

    for row in csvreader: #iterates through all rows in the csv file
        transaction = row[0] #declares column A in each row as a transaction
        profit_or_loss = row[1] #declares column B in each row as profit or loss on that transaction

        if row: #if the row contains values
            total_months = total_months + 1 #add one to the total months count
            profits_losses.append(int(profit_or_loss)) #add the profit or loss from that transaction to the profit_losses list
            dates.append(transaction) #add the date of that transaction to the dates list

    #find the total profit or losses from all transactions
    total_profits_losses = sum(profits_losses) #create a new variable for the total profits/losses from transactions

    #find the average change between transactions
    #create list of deltas
    deltas = [profits_losses[n]-profits_losses[n-1] for n in range(1,len(profits_losses))] #create new list of deltas
    deltas.insert(0, 0) #add value 0 to beginning of the new list

    #create new dictionary of dates and deltas
    delta_dic = {dates[i]: deltas[i] for i in range(len(dates))}

    #find average delta
    import numpy as np
    avg_delta = np.mean(list(delta_dic.values())) #determine the average delta

    #find the transaction with the largest increase in profit from deltas
    largest_profit= max(delta_dic.values()) #identify the max value in the delta_dic disctionary
    profit_date= max(delta_dic, key=delta_dic.get) #identify the date of the max value

    #find the transaction with the largest decrease in losses between transactions
    largest_loss= min(delta_dic.values()) #identify the min value in the delta_dic dictionary
    loss_date= min(delta_dic, key=delta_dic.get) #identify the date of the min value

#print the financial analysis
print('Financial Analysis')
print('------------------')
print('Total Months: ', str(total_months))
print('Total: ', '$'+str(total_profits_losses))
print('Average Change: ', '$'+str(avg_delta))
print('Greatest Increase in Profits: ', profit_date, '($'+str(largest_profit)+')')
print('Greatest Decrease in Profits: ', loss_date, '($'+str(largest_loss)+')')

#create a "financial_analysis.txt" file
my_file=open('financial_analysis.txt', 'w') #create and open "financial_analysis.txt" file
#add results to file
my_file.write("Financial Analysis\n") 
my_file.write("------------------\n")
my_file.write(f"Total Months: {total_months}\n")
my_file.write(f"Total: ${total_profits_losses}\n")
my_file.write(f"Average Change: ${avg_delta}\n")
my_file.write(f"Greatest Increase in Profits: {profit_date} (${largest_profit})\n")
my_file.write(f"Greatest Decrease in Profits: {loss_date} (${largest_loss})")
my_file.close()

#import shutil
#os.rename('/PyBank/financial_analysis.txt', 'PyBank/output/financial_analysis.txt')
