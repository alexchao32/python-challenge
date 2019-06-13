import pandas as pd


file = "Resources/budget_data.csv"
budget_df = pd.read_csv(file)

# Get the total number of months
total_months = len(budget_df)

# Get the net total Profit/Losses
net_total = budget_df['Profit/Losses'].sum()


# Generate a column of net change for each month
change_list = []
change_list.append(None) # No change applicable for first month

profit_list = budget_df['Profit/Losses'].tolist()

for i in range(1, len(profit_list)):
    temp_change = profit_list[i] - profit_list[i-1]
    change_list.append(temp_change)

# Add the change list back to the dataframe
budget_df['Change'] = change_list

# Get the mean change
mean_change = budget_df['Change'].mean()

# Get row with largest increase
largest_increase = budget_df.loc[budget_df['Change'].idxmax()]

# Get row with largest decrease
largest_decrease = budget_df.loc[budget_df['Change'].idxmin()]

# Print all the results
print('Financial Analysis')
print('----------------------------')
print('Total Months:', total_months)
print('Total: $' + str(net_total))
print(f'Average Change: $ {mean_change:.2f}')
print('Greatest Increase in Profits: ' + largest_increase['Date'] + ' (' + str(largest_increase['Change']) + ')')
print('Greatest Decrease in Profits: ' + largest_decrease['Date'] + ' (' + str(largest_decrease['Change']) + ')')