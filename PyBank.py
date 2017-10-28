import csv


csv_load_file = "budget_data_1.csv"
csv_file_output = "budget_analysis_1.txt"

with open(csv_load_file,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)[1:] 
    
    revenue = []
    revenue_change = []
    

    for row in data:
        revenue.append((row[1]))
        revenue = list(map(int, revenue)) 

change = 0
change = int(change)
previous_row = revenue[0]

for row in revenue:
    change = row - previous_row
    revenue_change.append((change))
    previous_row = row

revenue_change = revenue_change[1:]
revenue_change = list(map(int, revenue_change)) 

 
row_count =  len(revenue) 

total_revenue = sum(revenue) 

total_change = sum(revenue_change)
total_change = int(total_change)
number_of_changes = len(revenue[1:])
number_of_changes = int(number_of_changes)
average_change = total_change / number_of_changes



month2 = []

for row in data:
        
    month2.append((row[0]))
        
month2 = month2[1:]
month_changes = [
     ("Month", [month2]),
     ("Changes in Revenue", [revenue_change])]



Max = max(revenue)
Min = min(revenue)
Max2 = max(revenue_change)
Min2 = min(revenue_change)   



for row in data:
    if row[1] == str(Max):
        max_row = row

for row in data:
    if row[1] == str(Min):
        min_row = row

keys = month2
values = revenue_change
dictionary = dict(zip(keys, values))


for row in month_changes:
    if row[1] == Max2:
        max_row2 = row




print(" Financial Analysis -------------------------")
print("      Total Months - ", row_count)
print("      Total Reveue- ", total_revenue)
print("      Average Revenue Change- ", average_change)
print("      Month with the Greatest Revenue- ", max_row)
print("      Month with the Lowest Revenue- ", min_row)
print("      Greatest Increase in Revenue- ", max(dictionary), Max2)
print("      Greatest Decrease in Revenue- ", min(dictionary), Min2)
print("---------------------------------------------")
