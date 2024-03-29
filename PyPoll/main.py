import pandas as pd


file = "Resources/election_data.csv"
election_df = pd.read_csv(file)

# Get the total number of votes
total_votes = len(election_df)

# Get the list of candidates
candidate_list = election_df['Candidate'].unique().tolist()

vote_list = []
percent_list = []

max_percent = 0 # INitialize highest percentage at zero

# Iterate through each candidate performing the calculations for counting/percentages
for i in candidate_list:
    
    # Count the votes for each candidate
    temp_vote_count = len(election_df.loc[election_df['Candidate'] == i])
    
    #Calculate vote percentage
    temp_percent = temp_vote_count/total_votes*100

    vote_list.append(temp_vote_count)
    percent_list.append(temp_percent)
    
    # Check if the vote percent is a new highest percent... if so, store the candidate as the winner
    if temp_percent > max_percent:
        max_percent = temp_percent
        winner = i # Store the winner's name
    
    
# print the results
print('Election Results')
print('-------------------------')
print(f'Total votes: {total_votes}')
print('-------------------------')

for j in range(0, len(candidate_list)):
    #print(f'{candidate_list[j]}: {percent_list[j]:.3f} ({vote_list[j]})')
    print(f'{candidate_list[j]}: {percent_list[j]:.3f}% ({vote_list[j]})')
    
print('-------------------------')
print('Winner:', winner)



# Export results to text file


line1 = ('Election Results')
line2 = ('-------------------------')
line3 = (f'Total votes: {total_votes}')
line4 = ('-------------------------')

result_list = []
for j in range(0, len(candidate_list)):
    #print(f'{candidate_list[j]}: {percent_list[j]:.3f} ({vote_list[j]})')
    result_list.append(f'{candidate_list[j]}: {percent_list[j]:.3f}% ({vote_list[j]})')
    
line5 = ('-------------------------')
line6 = ('Winner:', winner)



with open('poll_results.txt','w') as out:
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,result_list[0],result_list[1],
              result_list[2],result_list[3],line5,line6))
