# -*- coding: utf-8 -*-
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
import normalize

def colors(n): 
    return abs(n-1) *10

    
def show(df_train, y_test_pred):   
    # visualize the results
    print("***************** PREDICTIONS **********************")
    print(y_test_pred)
    
    y_df=df_train['encryp_client+encryp_supplier+environment'].drop_duplicates()

    decoded=normalize.decode(y_df,'./encryp_client+encryp_supplier+environment')

    fig = plt.figure()
    ax = plt.axes(projection="3d",yticklabels=decoded,yticks=y_df)

    
    

    z_points = df_train['hour_in_day'].values.tolist()
    y_points = df_train['encryp_client+encryp_supplier+environment']
    x_points = df_train['error_code'].values.tolist()
    c_points=list(map(colors, y_test_pred))
    
    ax.scatter3D(x_points, y_points, z_points, c=c_points,cmap='gray',depthshade=False )

    plt.show()
    