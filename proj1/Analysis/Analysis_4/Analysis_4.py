#4)To find the quarterly profits of the carriers for every year
import pandas as pd
import matplotlib.pyplot as plt
##Reading the CSV file from the disk
loc='/Users/Sneha/Downloads/Final_dataset.csv'
loc1='/Users/Sneha/Downloads/Carrier_finances.csv'

carrier_data=pd.read_csv(loc1)

#Filling all the NAN values in float columns to 0.0
carrier_data['CURR_ASSETS'].fillna(0.0,inplace=True)
carrier_data['FLIGHT_EQUIP'].fillna(0.0,inplace=True)
carrier_data['ASSETS'].fillna(0.0,inplace=True)
carrier_data['CURR_LIABILITIES'].fillna(0.0,inplace=True)
carrier_data['NON_REC_LIAB'].fillna(0.0,inplace=True)
carrier_data['DEF_CREDITS'].fillna(0.0,inplace=True)
data= pd.read_csv(loc)

#Filling the NAN with 0 for DepTime and ArrTime columns
data['DepTime'].fillna(0,inplace=True)
data['ArrTime'].fillna(0,inplace=True)

#Convert the columns to int
data.DepTime=data.DepTime.astype(int)
data.ArrTime=data.ArrTime.astype(int)
data=data[['Origin','Dest','UniqueCarrier','FlightNum','Distance']]

#Groupby based on carrier
data=data.groupby(['Origin','UniqueCarrier','Dest','FlightNum','Distance']).size().reset_index()
carrier_data=carrier_data.groupby(['CARRIER_NAME','YEAR','QUARTER','CARRIER']).sum().reset_index()

#Function to calculate profits
def per_of_assets(v):
    tot_assets=v[4]+v[5]+v[6]
    tot_liabilities=v[7]+v[8]+v[9]
    if tot_assets!=0:
        per_of_profits=((tot_assets-tot_liabilities)/tot_assets)*100
        return per_of_profits
    else:
        return 0

#calling the function to calculate percent profits
carrier_data['Percent_profits']=carrier_data.apply(per_of_assets,axis=1)
carrier_data=carrier_data.sort(['Percent_profits'], ascending=[False] )
p=carrier_data.head(1)
x= p['CARRIER_NAME']
#print(x)
fina=carrier_data[carrier_data['CARRIER_NAME']=='Southern Air Inc.']
final=fina[fina['YEAR']==2015]
#print(final)

#Plot pie chart
plt.figure(figsize=(16,8))
 #plot chart
ax1 = plt.subplot(121, aspect='equal')
final.plot(kind='pie', y = 'Percent_profits', ax=ax1, autopct='%1.1f%%',
 startangle=90, shadow=False, labels=final['QUARTER'], legend = False, fontsize=14)
plt.title('Percentage quarterly profits for the carrier with highest profit : Southern Air Inc. ')
plt.savefig('/Users/Sneha/Downloads/Plot_Analysis_4.png')
plt.show()

#Merge with another csv file to get name of carrier
m= pd.merge(data,carrier_data,left_on='UniqueCarrier',right_on='CARRIER')
m=m[['Origin','UniqueCarrier','Dest','Distance','CARRIER_NAME','YEAR','QUARTER','Percent_profits']]
print(m.head())

#Writing to csv file
m.to_csv("output_Analysis_4.csv",index = False)

