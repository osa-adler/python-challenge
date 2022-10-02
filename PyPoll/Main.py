import os
import csv

election_csv = os.path.join("..","PyPoll","Resources","election_data.csv")

total_votes = 0
candidate = []
charles = 0
diana = 0
raymon = 0
winner = []

with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    print(f"Header: {header}")


    for row in csv_reader:
        total_votes += 1
        candidate.append(row[2])
        if row[2] == 'Charles Casper Stockham':
            charles += 1
        elif row[2] == 'Diana DeGette':
            diana += 1
        else:
            raymon += 1
          

def unique(blank):
    unique_list = []     
    for x in blank:
        if x not in unique_list:
            unique_list.append(x)        
    return unique_list
candidates = list(unique(candidate))


if charles > diana and charles > raymon:
        winner = candidates[0]
elif diana > charles and diana > raymon:
        winner = candidates[1]
elif raymon > charles and raymon > diana:
        winner = candidates[2]
else:
    pass

print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------")
print(f"Charles Casper Stockham: {'{:.3%}'.format(charles/total_votes)} ({charles})")
print(f"Diana DeGette: {'{:.3%}'.format(diana/total_votes)} ({diana})")
print(f"Raymon Anthony Doane: {'{:.3%}'.format(raymon/total_votes)} ({raymon})")
print("--------------------------------")
print(f"Winner: {winner}")

csvpath2 = os.path.join("..", "Python-Challenge", "PyPoll", "PyPoll_Analysis_Summary.txt")

with open(csvpath2, "w", newline = "") as text:

    text.write("Election Results\n")
    text.write("--------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("--------------------------------\n")
    text.write(f"Charles Casper Stockham: {'{:.3%}'.format(charles/total_votes)} ({charles})\n")
    text.write(f"Diana DeGette: {'{:.3%}'.format(diana/total_votes)} ({diana})\n")
    text.write(f"Raymon Anthony Doane: {'{:.3%}'.format(raymon/total_votes)} ({raymon})\n")
    text.write("--------------------------------\n")
    text.write(f"Winner: {winner}\n")
