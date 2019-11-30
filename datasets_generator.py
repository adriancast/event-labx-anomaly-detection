import numpy as np
import pandas as pd
import os
import datetime
import base64
from sklearn import preprocessing

## Módulo para generar datasets de combinaciones de columnas del dataset original, para año, mes semana y día


#coge los datos del dataset original
dataset='full'
df=pd.read_csv("./normalized_"+dataset+".csv")

#Queremos combinaciones de las siguientes columnas del dataset original
values = ['encryp_client','encryp_supplier','environment','hub_machine','hub_status_id','error_code','Hits']


#Contadores para el combinador multivariable
counters=[]
n=len(values) 
for counter in range(n):
    counters.append(0)

for iter in range(2**n):
    current_columns_day_in_year=[]
    current_columns_day_in_month=[]
    current_columns_day_in_week=[]
    current_columns_hour_in_day=[]

    current_columns_day_in_year.append('day_in_year')
    current_columns_day_in_month.append('day_in_month')
    current_columns_day_in_week.append('day_in_week')
    current_columns_hour_in_day.append('hour_in_day')

    #print("**************")
    for counter in range(n):
        if counters[counter]==0 :
            current_columns_day_in_year.append(values[counter])
            current_columns_day_in_month.append(values[counter])
            current_columns_day_in_week.append(values[counter])
            current_columns_hour_in_day.append(values[counter])
            
    
    #print(current_columns_day_in_year)
    df.filter(items=current_columns_day_in_year).to_csv(dataset+'_'+'-'.join(current_columns_day_in_year)+'.csv')
    df.filter(items=current_columns_day_in_month).to_csv(dataset+'_'+'-'.join(current_columns_day_in_month)+'.csv')
    df.filter(items=current_columns_day_in_week).to_csv(dataset+'_'+'-'.join(current_columns_day_in_week)+'.csv')
    df.filter(items=current_columns_hour_in_day).to_csv(dataset+'_'+'-'.join(current_columns_hour_in_day)+'.csv')

    

    #print(counters)
    for i in range(n):
        if( (counters[i]+1)%2!=0):
            counters[i]=counters[i]+1
            for j in range(i):
                counters[j]=0
            break


