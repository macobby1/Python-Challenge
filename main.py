# Import Operating system and csv
import os, csv


# File location
csv_file = os.path.join('..', 'Practice', 'budget_data.csv')

# Track Variables
total_months = []
total_profit = []
monthly_profit_change = []
 
# Read the budget_data file
with open(csv_file) as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 
    next(csvreader)  

    # Loop through the data
    for row in csvreader: 

        # Append the total months and total profit 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Loop through the profits to get the monthly change 
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Max and Min monthly profit change 
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Add + 1 to Correlate max and min to the proper month using month list and index 

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Budget Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output File
output_file = os.path.join('..','Practice', 'budget_analysis.txt')

with open(output_file,"w") as file:
    
# Write Budget_Analysis_Summary 
    file.write("Budget Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
