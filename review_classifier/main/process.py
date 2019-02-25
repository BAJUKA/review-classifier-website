import numpy as np 
import tensorflow as tf 
import keras as K
from keras.models import load_model

import tensorflowjs as tfjs
import os

def predict(review):
	
	max_words = 20000
	max_rew_len = 80
	d = K.datasets.imdb.get_word_index()
	words = review.split()
	rev=[]
	K.backend.clear_session()
	model = load_model('/model/model.h5')
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