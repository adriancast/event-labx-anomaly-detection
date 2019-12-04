# -*- coding: utf-8 -*-
"""Example of using kNN for outlier detection
"""

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

#df = pd.read_csv("/Users/germanmartinezlopez/Downloads/data.csv")
#print(df.info())
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

def save_state(clf, filepath):
    # Creat json and save to file
     
    with open(filepath, 'wb') as file:
        pickle.dump(clf,file)
    
    # A method for loading data from JSON file
def load_state(filepath):
    return pickle.load(filepath)
    


def colors(n): 
    return abs(n-1) *10

def train(csv):
    df=None
    if( not os.path.exists(csv+".normalized") ):
        df=pd.read_csv(csv)
        df=df.drop(df.columns[0], axis=1)
        print(df.head())
        for col in df.columns:
            if(isinstance(df[col][0],str)):
                df[col]=normalize.load_update_encode_and_save(df[col],col)
            
        print(df.head())

        df.to_csv(csv+".normalized")
    else:
        df=pd.read_csv(csv+".normalized")
        df=df.drop(df.columns[0], axis=1)
    
    
    print(df.head())
    df_train=df#.truncate(after=df.shape[0]*80/100)
    #df_test=df.truncate(before=df.shape[0]*80/100)

    # train kNN detector
    
    clf = None
    if( not os.path.exists(os.path.splitext(os.path.splitext(csv)[0])[0]+'.knn') ):
        clf=KNN()
        clf.fit(df_train)

        # get the prediction labels and outlier scores of the training data
        y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
        y_train_scores = clf.decision_scores_  # raw outlier scores
        
        
        save_state(clf,os.path.splitext(os.path.splitext(csv)[0])[0]+'.knn')
    else:
        with open(os.path.splitext(os.path.splitext(csv)[0])[0]+'.knn', 'rb') as file:
            clf=pickle.load(file)
            print(df_train.head())

    # get the prediction on the test data
    y_test_pred = clf.predict(df_train)  # outlier labels (0 or 1)

    return df_train , y_test_pred