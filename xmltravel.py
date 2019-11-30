

# -*- coding: utf-8 -*-
"""Example of using kNN for outlier detection
"""
# Author: Yue Zhao <zhaoy@cmu.edu>
# License: BSD 2 clause

from __future__ import division
from __future__ import print_function

import os
import sys

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

import numpy as np
import pandas as pd
import os
import datetime
import base64
from sklearn import preprocessing
def parse_day_in_year(start_time):
	start_time = start_time.replace(" UTC", "")
	return str(datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timetuple().tm_yday)
def parse_day_in_month(start_time):
	start_time = start_time.replace(" UTC", "")
	return str(datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timetuple().tm_mday)
def parse_hour_in_day(start_time):
	start_time = start_time.replace(" UTC", "")
	return str(datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').hour)
def parse_day_in_week(start_time):
	start_time = start_time.replace(" UTC", "")
	return str(datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S').timetuple().tm_wday)
def stro_to_int(inp):
	return int.from_bytes(base64.b64encode(inp.encode()), 'big')
df=pd.read_csv("./mini.csv")
df['day_in_month'] = df['start_time'].apply(parse_day_in_month)
df['day_in_year'] = df['start_time'].apply(parse_day_in_year)
df['day_in_week'] = df['start_time'].apply(parse_day_in_week)
df['hour_in_day'] = df['start_time'].apply(parse_hour_in_day)
df['encryp_client'] = df['encryp_client'].apply(stro_to_int)
df['encryp_supplier'] = df['encryp_supplier'].apply(stro_to_int)
df['environment'] = df['environment'].apply(stro_to_int)
df['hub_machine'] = df['hub_machine'].apply(stro_to_int)
df = df.drop('start_time', axis=1)
print(df.head())

if __name__ == "__main__":
    contamination = 0.1  # percentage of outliers
    n_train = 200  # number of training points
    n_test = 100  # number of testing points

    # train kNN detector
    clf_name = 'KNN'
    clf = KNN()
    clf.fit(df)

    # get the prediction labels and outlier scores of the training data
    y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
    y_train_scores = clf.decision_scores_  # raw outlier scores
	
    import pdb; pdb.set_trace()
   
    # get the prediction on the test data
    #y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
    #y_test_scores = clf.decision_function(X_test)  # outlier scores

    # evaluate and print the results
    #print("\nOn Training Data:")
    #evaluate_print(clf_name, y_train, y_train_scores)
    #print("\nOn Test Data:")
    #evaluate_print(clf_name, y_test, y_test_scores)

    # visualize the results
    #visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
              #y_test_pred, show_figure=True, save_figure=True)
