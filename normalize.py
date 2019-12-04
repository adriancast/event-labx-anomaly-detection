import numpy as np
import pandas as pd
import os
import datetime
import base64
import pickle

from sklearn import preprocessing



##############################
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

#################################


def reset_saved_encoder(filepath):
	if(os.path.isfile(filepath)):
		os.remove(filepath+".encoder.obj")
		os.remove(filepath+".original.dat")

def init_encoder_with_full_dataframe(dataframe):
	encoder=preprocessing.LabelEncoder()
	encoder.fit(dataframe)
	return encoder


def encode(dataframe, encoder):
	return encoder.transform(dataframe)

#Loads a saved encoder and
def load_and_encode(dataframe, filepath):
	#load encoder if exists, or create new

	if(os.path.isfile(filepath)):
		#load params
		with open(filepath+'.encoder.obj', 'wb') as file:
			encoder=pickle.load(file)

			out = encode(dataframe, encoder)

			#return encoded
			return out

def decode(dataframe, filepath):
	df_decoded=None
	if(os.path.isfile(filepath+'.encoder.obj') and os.path.isfile(filepath+'.original.dat')):
		#load params
		with open(filepath+'.encoder.obj', 'rb') as file:
			encoder=pickle.load(file)
		#update original dataframe
		with open(filepath+'.original.dat', 'rb') as file:
			df_encoded=pickle.load(file)
		df_decoded=encoder.inverse_transform(dataframe)
		return df_decoded

def load_update_encode_and_save(dataframe, filepath):
	#load encoder if exists, or create new
	encoder = None
	df_encoded=None
	df_decoded=None

	if(os.path.isfile(filepath+'.encoder.obj') and os.path.isfile(filepath+'.original.dat')):
		#load params
		with open(filepath+'.encoder.obj', 'rb') as file:
			encoder=pickle.load(file)
		#update original dataframe
		with open(filepath+'.original.dat', 'rb') as file:
			df_encoded=pickle.load(file)
		df_decoded=encoder.inverse_transform(df_encoded)
		df_decoded.append(dataframe)
	else:
		encoder=preprocessing.LabelEncoder()
		df_decoded=dataframe

	encoder.fit(df_decoded)
	out = encoder.transform(df_decoded)
	#save params to file
	with open(filepath+'.encoder.obj', 'wb') as file:
			pickle.dump(encoder,file)
	with open(filepath+'.original.dat', 'wb') as file:
			pickle.dump(df_decoded,file)			
	#return updated or created encoder
	return out


