import pandas as pd, _datetime
import calendar
loc= '/Users/Sneha/Documents/material_for_python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv'
data = pd.read_csv(loc)
#To convert date column to datetime and extract only month and year
data['DATE'] = pd.to_datetime(data['DATE'])
data['year']  = data['DATE'].dt.year
data['MONTH'] = data['DATE'].dt.month
#for the year 2016
x1=data[data['year']==2016]
x=x1[['MONTH','year','BOROUGH']]
#For one month for NYC
h= x.groupby(['MONTH']).size().reset_index(name="NYC")
#print(h)
#For one month for Manhattan
m=x1[x1['BOROUGH']=='MANHATTAN']
n=m[['MONTH','year','BOROUGH']]
h1= n.groupby(['MONTH']).size().reset_index(name="MANHATTAN")
#Converting numbers to month names
h1['MONTH'] = h1['MONTH'].apply(lambda x: calendar.month_abbr[x])
#fcolumns for month, NYC and Manhattan
final=pd.concat([h1['MONTH'], h1['MANHATTAN'],h['NYC']], axis=1, keys=['MONTH','MANHATTAN', 'NYC'])
#Calculating percentage and the final output showing few rows using df.head()
final['PERCENTAGE'] = (final['MANHATTAN']/final['NYC'])
final.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
print(final.head())

#Writing to a csv file
final.to_csv("output_Q1_PART_ONE.csv",index = False)