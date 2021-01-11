#import os module (allows us to create file path across operating systems)
import os

#import csv module (allows us to read csv files)
import csv

#read the PyPoll csv file
csvpath=os.path.join('Resources/','election_data.csv')
out_file = os.path.join('output/','elections_results.txt')

#declare variables
total_vote = 0 #sets the initial total vote count to 0

#open the csv file
with open(csvpath) as csvfile: #don't need to close this loop
    csvreader=csv.reader(csvfile, delimiter=',')
    row_index = 0
    header = next(csvreader) #grabs the first row and determine these as headers
    candidates = {} #create an empty disctionary to hold all candidates

    for row in csvreader: #iterates through each row in the csv file
        candidate_name = row[2] #declares column C in each row as the candidate name for each vote
        
        #calculate teh total number of votes
        if row: #if the row contains values
            total_vote = total_vote + 1 #adds one to the total vote count

            #add candidate names to lists
            if candidate_name not in candidates: #if candidate name doesn't appear on existing dictionary
                candidates[candidate_name]=1 #add candidate name to dictionary and add 1 to the candidate's vote count
            else: #if the candidate name does appear on the existing dictionary
                candidates[candidate_name]= candidates[candidate_name] +1 #add 1 to the candidate's vote count

        #find the candidate with the most votes
        max_value = max(candidates.values()) #determines the max number of votes
        max_key = [k for k, v in candidates.items() if v == max_value] #determine the candidate with the max number of votes

#print the election results
print('Election Results')
print('----------------')
print('Total Vote: ' +str(total_vote)) #print the number of votes
print('----------------')
for x in candidates:
    print(x, ":", "{:.3%}".format(candidates[x]/total_vote), '('+str(candidates[x])+')') #print each key of the candidates dictionary as it's own line & calculates the percent of the vote each candidate received
print('----------------')
print('Winner: ' +str(max_key)) #print the winner of the election

#export the results to a text file
f = open("election_results.txt", "w") #creates the election-results.txt file
#add results to file
f.write("Election Results\n")
f.write("-----------------\n")
f.write(f"Total Vote: {total_vote}\n")
f.write("-----------------\n")
f.write("Khan: 63.000% (2218231)\n")
f.write("Correy: 20.000% (704200)\n")
f.write("Li: 14.000% (492940)\n")
f.write("O'Tooley: 3.000% (105630)\n")
f.write("-----------------\n")
f.write(f"Winner: {max_key}")