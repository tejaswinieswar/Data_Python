import pandas as pd
loc= "/Users/Sneha/Documents/python/Python_assignments/Assignment_3/Data/employee_compensation.csv"
data = pd.read_csv(loc)
#For Calendar year
req_dat = data[ (data["Year Type"]== "Calendar")]
#Calculating avg of all the salaries for gven employee
req_dat=req_dat[["Employee Identifier","Job Family","Salaries","Overtime","Other Salaries","Total Salary","Retirement","Health/Dental","Other Benefits","Total Benefits","Total Compensation"]]
req_data= req_dat.groupby(["Employee Identifier","Job Family"]).mean().reset_index()
#Picking up employees whose overtime salary is greater than 5% of the salary
req_data1=req_data[req_data['Overtime']> 0.05*req_data['Salaries']]
req_data2=req_data1[['Job Family','Total Benefits','Total Compensation']]
#Groupby based on job family and calculating avg
req_data2= req_data2.groupby(['Job Family']).mean().reset_index()
#Calculating percentage
req_data2['Percent_Total_Benefits']= req_data2['Total Compensation']/req_data2['Total Benefits']
req_data2.to_csv('output_Q2_PART_TWO.csv',index = False)
print (req_data2.head())