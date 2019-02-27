import numpy as np 
import tensorflow as tf 
import keras as K
import tensorflowjs as tfjs
import os

# Data Loading
print("Loading data")
max_words = 20000
max_rew_len = 80
(train_x,train_y),(test_x,test_y) = K.datasets.imdb.load_data(seed=1,num_words=max_words)

train_x = K.preprocessing.sequence.pad_sequences(train_x,truncating='pre',
	padding="pre",maxlen=max_rew_len)
test_x = K.preprocessing.sequence.pad_sequences(test_x,truncating='pre',
	padding="pre",maxlen=max_rew_len)


# Model Creation
print("\n\nCreating model")
e_init = K.initializers.RandomUniform(-0.01,0.01,seed=1)
init = K.initializers.glorot_uniform(seed=1)
optim = K.optimizers.Adam()
embed_len = 32

model = K.models.Sequential()
model.add(K.layers.embeddings.Embedding(input_dim=max_words,
	output_dim=embed_len,embeddings_initializer=e_init,mask_zero=True))
model.add(K.layers.LSTM(units=100,kernel_initializer=init,dropout=0.2,recurrent_dropout=0.2))
model.add(K.layers.Dense(units=1,kernel_initializer=init,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer=optim,metrics=['acc'])
print(model.summary())


# Training model
batch_size = 32
max_epochs = 3
print("\n\nStrated Training")
model.fit(train_x,train_y,epochs=max_epochs,batch_size=batch_size,
	shuffle=True,verbose=1)
print("training complete\n\n")


# Evaluation
print("Evaluating.....")
loss_acc = model.evaluate(test_x,test_y,verbose=0)
print("Test data: loss = %0.6f accuracy = %0.2f%%"%(loss_acc[0],loss_acc[1]*100))


# Saving
print("Saving model to disk")
path = './model.h5'
path_tfjs = './tfjs_model'
model.save(path)
tfjs.converters.save_keras_model(model,path_tfjs)
print("Completed Saving")


