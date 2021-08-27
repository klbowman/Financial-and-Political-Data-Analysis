import os
import csv
import sys

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Total number of months included in the dataset
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total_months = len(list(csvreader))
        
#Net total amount of "Profit/Losses" over the entire period
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    for row in csvreader:
        total += int(row[1])

#Average of changes in "Profit/Losses" over the entire period
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    changes = []
    ProfitLoss = []
    for row in csvreader:
        ProfitLoss.append(row[1])
    for i in range(len(ProfitLoss)-1):
        change = int(ProfitLoss[i+1])- int(ProfitLoss[i])
        changes.append(change)
        average_ProfitLoss = round((sum(changes)/len(changes)),2)

#Greatest increase/decrease in profits (date and amount)
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    dates = []        
    max_profit = max(changes)
    min_profit = min(changes)
    for row in csvreader:
        dates.append(row[0])
max_date = dates[changes.index(max_profit)+1]
min_date = dates[changes.index(min_profit)+1]
 
#Print Summary
print('Financial Analysis')
print('-----------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_ProfitLoss} ')
print(f'Greatest Increase in Profits: {max_date} (${max_profit})')
print(f'Greatest Decrease in Profits: {min_date} (${min_profit})')

#Export Summary
output_path = os.path.join("Analysis", "PyBank_ResultsSummary.txt")

sys.stdout = open(output_path, "w")

print('Financial Analysis')
print('-----------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total}')
print(f'Average Change: ${average_ProfitLoss} ')
print(f'Greatest Increase in Profits: {max_date} (${max_profit})')
print(f'Greatest Decrease in Profits: {min_date} (${min_profit})')

sys.stdout.close()


    