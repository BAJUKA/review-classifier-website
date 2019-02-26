import numpy as np 
import tensorflow as tf 
import keras as K
from keras.models import load_model
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

a = os.path.join(BASE_DIR, 'main')
model_path = os.path.join(a, 'model.h5')

import tensorflowjs as tfjs
import os

def predict(review):
	
	max_words = 20000
	max_rew_len = 80
	d = K.datasets.imdb.get_word_index()
	words = review.split()
	rev=[]
	K.backend.clear_session()
	model = load_model(model_path)
	for word in words:
		if word not in d:
			rev.append(2)
		else:
			rev.append(d[word]+3)
	rev = K.preprocessing.sequence.pad_sequences([rev], truncating='pre',
		padding='pre', maxlen=max_rew_len)
	prediction = model.predict(rev)
	print(prediction[0][0])
	return prediction[0][0]
