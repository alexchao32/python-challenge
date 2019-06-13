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


# Export results to text file
line1 = ('Financial Analysis')
line2 = ('----------------------------')
line3 = ('Total Months:', total_months)
line4 = ('Total: $' + str(net_total))
line5 = (f'Average Change: $ {mean_change:.2f}')
line6 = ('Greatest Increase in Profits: ' + largest_increase['Date'] + ' (' + str(largest_increase['Change']) + ')')
line7 = ('Greatest Decrease in Profits: ' + largest_decrease['Date'] + ' (' + str(largest_decrease['Change']) + ')')


with open('bank_results.txt','w') as out:
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
