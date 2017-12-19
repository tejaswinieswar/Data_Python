import pandas as pd
loc = '/Users/Sneha/Documents/material_for_python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/cricket_matches.csv'
data= pd.read_csv(loc)
#checking if the winner is home team
home_win=data[data['home']== data['winner']]
#Taking cloumns
home_win1=home_win[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]
#Checking if home has won in both innings 1 and 2
z = home_win1[home_win1['home'] == home_win1['innings1']][['home','innings1_runs']]
y = home_win1[home_win1['home'] == home_win1['innings2']][['home','innings2_runs']]
y=y.rename(columns={'innings2_runs': 'innings1_runs'})
#Concatinating into single df
fr= [z,y]
final=pd.concat(fr)
output = final['innings1_runs'].groupby(final['home']).mean()
output.to_csv("output_Q3_PART_ONE.csv",index = False)
print (output.head())