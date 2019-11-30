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

df=pd.read_csv("./mini.csv")

df['day_in_month'] = df['start_time'].apply(parse_day_in_month)
df['day_in_year'] = df['start_time'].apply(parse_day_in_year)
df['day_in_week'] = df['start_time'].apply(parse_day_in_week)
df['hour_in_day'] = df['start_time'].apply(parse_hour_in_day)
df = df.drop('start_time', axis=1)

le_encryp_client = preprocessing.LabelEncoder()
le_encryp_client.fit(df['encryp_client'])
df['encryp_client'] = le_encryp_client.transform(df['encryp_client'])

le_encryp_supplier = preprocessing.LabelEncoder()
le_encryp_supplier.fit(df['encryp_supplier'])
df['encryp_supplier'] = le_encryp_supplier.transform(df['encryp_supplier'])

le_environment = preprocessing.LabelEncoder()
le_environment.fit(df['environment'])
df['environment'] = le_environment.transform(df['environment'])

le_hub_machine = preprocessing.LabelEncoder()
le_hub_machine.fit(df['hub_machine'])
df['hub_machine'] = le_hub_machine.transform(df['hub_machine'])

df.to_csv('dep.csv')