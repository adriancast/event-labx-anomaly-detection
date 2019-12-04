import numpy as np
import pandas as pd
import os
import datetime
import base64
import normalize
from sklearn import preprocessing
import gc


## Módulo para generar datasets 



def join_columns(s1,s2):
    return s1+' '+s2

def generate_dataframes(dataframe,datasets,fixedColumns, variableColumns,joinedcolumns,dropColumns):
    
    dataframe=dataframe.drop(columns=dropColumns)

    gc.collect()

    print(dataframe.head())

    print("start joining")
    for col in range(len(joinedcolumns)) :
        if("joined" not in  dataframe.columns ):
            dataframe["joined"]=dataframe.filter(items=[joinedcolumns[col]])
            dataframe=dataframe.drop(columns=[joinedcolumns[col]])
            gc.collect()
        else:
            dataframe["joined"]=dataframe["joined"].map(str) +' '+ dataframe[joinedcolumns[col]].map(str)
            dataframe=dataframe.drop(columns=[joinedcolumns[col]])
            gc.collect()
    
    joinedColumnsName="+".join(joinedcolumns)
   
    dataframe=dataframe.rename(columns={"joined":joinedColumnsName})
    print(dataframe.head())
    gc.collect()
    
    
    
    #Contadores para el combinador multivariable
    counters=[]
    n=len(variableColumns) 
    for counter in range(n):
        counters.append(0)
        
    datarange_count=0
    #si no hay variaciones, almenos damos un resultado
    if(2**n==0):
        datarange_count=2**n
    else: 
        datarange_count=1

    for iter in range(datarange_count) :
        sets=[]

        for l in range(len(datasets)) :
            sets.append([datasets[l]]) #as list
            print("creating dataset: "+datasets[l] )

        

        #add variable columns
        for counter in range(n):
            if counters[counter]==0 :
                for l in range(len(datasets)):
                    sets[l].append( variableColumns[counter])
                
        # add fixedColumns at the end 
        for l in range(len(datasets)):
            for c in range(len(fixedColumns)):
                sets[l].append(fixedColumns[c])

        # add joinedColumn at the end 
        for l in range(len(datasets)):
            sets[l].append(joinedColumnsName)

        for l in range(len(datasets)) :
            print("dataset "+datasets[l]+" configured: "+(' '.join(sets[l])) )
            
        for l in range(len(datasets)):
            print("started creating dataset "+datasets[l])
            dataset_filtered=dataframe.filter(items=sets[l])
            dataset_filtered.to_csv( datasets[l]+'.'+'-'.join(sets[l])+'.dataframe.csv')
            print("finished creating dataset "+datasets[l])

        #print(counters)
        for i in range(n):
            if( (counters[i]+1)%2!=0):
                counters[i]=counters[i]+1
                for j in range(i):
                    counters[j]=0
                break

def save_distincts(dataframe, filepath):
    dataframe.drop_duplicates().to_csv( filepath)

