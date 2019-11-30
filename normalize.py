import numpy as np
import pandas as pd
import os
import datetime
import base64

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

df=pd.read_csv("./data.csv")

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

df.to_csv('dep.csv')
