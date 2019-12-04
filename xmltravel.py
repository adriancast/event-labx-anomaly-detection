

# -*- coding: utf-8 -*-
"""Example of using kNN for outlier detection
"""
# Author: Yue Zhao <zhaoy@cmu.edu>
# License: BSD 2 clause

from __future__ import division
from __future__ import print_function

import gc
import os
import sys
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

# temporary solution for relative imports in case pyod is not installed
# if pyod is installed, no need to use the following line
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

from pyod.models.knn import KNN
from pyod.utils.data import generate_data
from pyod.utils.data import evaluate_print
from pyod.utils.example import visualize

import json
import numpy as np
import pandas as pd
import os
import datetime
import base64
from sklearn import preprocessing

import pickle 
import normalize
import datasets_generator
import trainer
import plotter



##############################################
############### Main #########################
if __name__ == "__main__":
    #coge los datos del dataset original
    #transforma la start_date, y recupers sólo la hora del día del evento
    #guarda el csv al fichero temp_data.csv para que si se vuelve a ejecutar, se ahorre tiempo
    dataset_name='data'
    if( not os.path.exists("./temp_"+dataset_name+".csv") ):
        print("start loading file ./"+dataset_name+".csv")
        df=pd.read_csv("./"+dataset_name+".csv")
        df['hour_in_day'] = df['start_time'].apply(normalize.parse_hour_in_day)
        df = df.drop('start_time', axis=1)
        df.to_csv("./temp_"+dataset_name+".csv")
        gc.collect()
    else:
        print("start loading file ./temp_"+dataset_name+".csv")
        df=pd.read_csv("./temp_"+dataset_name+".csv")
        df=df.drop(df.columns[0], axis=1)
        print(df.head())

    print("finished loading file ./"+dataset_name+".csv")

    #no tenemos datos suficientes para hacer esto - datasets=['day_in_year','day_in_month','day_in_week']
    datasets=['hour_in_day']
    # estas columnas las descartamos 
    drop_values=['hub_machine','hub_status_id']
    #ahora mismo no queremos generar datasets con combinaciones de columnas, sólo queremos un fichero de salida
    variable_values=[]
    #queremos juntarl estas variables independientes en otra independiente, para reducir la dimensión de los datos
    joined_values=['encryp_client','encryp_supplier','environment']
    #estos campo tienen que ir siempre ya que son las salidas a evaluar
    fixed_values=['error_code','Hits']
    #generamos el dataframe
    if( not os.path.exists('./hour_in_day.hour_in_day-error_code-Hits-encryp_client+encryp_supplier+environment.dataframe.csv')):
        datasets_generator.generate_dataframes(df,datasets,fixed_values,variable_values,joined_values, drop_values)
    #entrenamos la KNN
    df=pd.read_csv('./hour_in_day.hour_in_day-error_code-Hits-encryp_client+encryp_supplier+environment.dataframe.csv')
    df=df.drop(df.columns[0], axis=1)
    df.head(10000).to_csv('./hour_in_day.hour_in_day-error_code-Hits-encryp_client+encryp_supplier+environment.dataframe.training.csv')
    df.tail(10).to_csv('./hour_in_day.hour_in_day-error_code-Hits-encryp_client+encryp_supplier+environment.dataframe.verifying.csv')
    df_train,results=trainer.train('./hour_in_day.hour_in_day-error_code-Hits-encryp_client+encryp_supplier+environment.dataframe.verifying.csv')
    #mostramos los resultados
    plotter.show(df_train,results)


