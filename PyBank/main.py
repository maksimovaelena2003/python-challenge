import csv
import os

# Set the path for the input file
file_path = os.path.join("..", "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)

    # Iterate through rows
    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate profit/loss change
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        # Update previous profit/loss
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / (total_months - 1)

# Find the greatest increase and decrease
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the results to a text file
output_path = os.path.join("PyBank", "analysis", "financial_analysis.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

