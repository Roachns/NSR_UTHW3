import csv
import os

csv_load_file = "election_data_2.csv"
csv_output_file = "election_analysis_1.txt"

with open(csv_load_file,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)[1:] 

Voter_ID = []
Candidate_Vote = []

for row in data:
    Voter_ID.append((row[0]))

for row in data:
    Candidate_Vote.append((row[2]))


Total_Votes = len(Candidate_Vote)
Total_Votes = int(Total_Votes)

Candidate_Set = set(Candidate_Vote)
names = []

for row in Candidate_Set:
    names.append(row)


print(" Election Results   ")

print( "---------------------")

print("Total Number of Votes -  ", Total_Votes)

can = 0
Candidate_Dictionary = {}

for row in names:
    candidate = str(names[can])
    Votes = Candidate_Vote.count(candidate)
    Votes = int(Votes)
    percentage = Votes / Total_Votes * 100
    Candidate_Dictionary.update({ candidate : Votes})
    print(candidate, ":  ", percentage, " %  (", Votes, ")" )
    can = can + 1


dictlist = ()

import operator

winner = max(Candidate_Dictionary, key=lambda key: Candidate_Dictionary[key])


print("-------------------")
print("Winner:  ", winner)

