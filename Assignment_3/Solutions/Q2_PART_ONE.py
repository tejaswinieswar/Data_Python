import pandas as pd
loc= "/Users/Sneha/Documents/python/Python_assignments/Assignment_3/Data/employee_compensation.csv"
data = pd.read_csv(loc)
#Selecting required columns
req_data= data[['Organization Group','Department','Total Compensation']]
#Performing groupby and mean of the total compensation
gr= req_data.groupby(['Organization Group','Department']).mean().reset_index()
#sorting in descending order
final= gr.sort(['Total Compensation'], ascending=[False])
#Writing to a csv file
final.to_csv('output_Q2_PART_ONE.csv',index = False)
print(final.head())