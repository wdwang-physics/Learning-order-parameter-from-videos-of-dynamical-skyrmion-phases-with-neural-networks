import numpy as np
from tensorflow import keras
import tensorflow as tf 
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import Dense,Activation,Convolution2D,Flatten,MaxPooling2D,BatchNormalization,Dropout
from keras.callbacks import ModelCheckpoint,EarlyStopping,ReduceLROnPlateau
import sys
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
####
# load the Skyrmion data
name_tem = 'DATA3dcnn6.npz'
data_tem = np.load(name_tem)
X = data_tem['X'];
Y = data_tem['Y']
index = np.arange(X.shape[0])
print(X.shape)
print(Y.shape)
np.random.shuffle(index)
X = X[index, :, :, :]
Y = Y[index, :]
X = X.reshape(X.shape[0],10,36,36,1)
#edge=1000;X=X[:edge,:,:,:,:];Y=Y[:edge,:]
print(X.shape)
print(Y.shape)
# build CNN
model = keras.models.Sequential()
model.add(keras.layers.TimeDistributed(keras.layers.Conv2D(filters=16, kernel_size=3, strides=2,padding='same',activation='relu'),input_shape=(10,36,36,1)))
model.add(keras.layers.TimeDistributed(keras.layers.BatchNormalization()))
model.add(keras.layers.TimeDistributed(keras.layers.MaxPooling2D(pool_size=3, strides=1, padding='same')))
model.add(keras.layers.TimeDistributed(keras.layers.Conv2D(32, 3, strides=2, padding='same',activation='relu')))
model.add(keras.layers.TimeDistributed(keras.layers.BatchNormalization()))
model.add(keras.layers.TimeDistributed(keras.layers.MaxPooling2D(3, 1, 'same')))
model.add(keras.layers.TimeDistributed(keras.layers.Flatten()))
model.add(keras.layers.TimeDistributed(keras.layers.Dense(64)))
model.add(keras.layers.TimeDistributed(keras.layers.Dropout(0.5)))
model.add(keras.layers.TimeDistributed(keras.layers.Dense(2)))
# build LSTM
model.add(keras.layers.LSTM(50))
model.add(keras.layers.Dense(4,activation='softmax'))
adam = keras.optimizers.Adam(lr=8e-5)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
filepath = "weights2best.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True,
                            mode='max')
earlyStopping=EarlyStopping(monitor='val_acc', patience=8, verbose=1, mode='max')
callbacks_list = [checkpoint,earlyStopping]
history = model.fit(X,Y, validation_split=0.2, epochs=120, batch_size=30, callbacks=callbacks_list,verbose=2)

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='lower right')
plt.savefig('cnnLSTM2-1.eps', format='eps', dpi=100)
plt.close()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.savefig('cnnLSTM2-2.eps', format='eps', dpi=100)
plt.close()
##################
name_tem=sys.argv[0]
print (model.summary())
#plot_model(model, to_file='model.png')
import pickle
with open('trainHistoryDict2.txt', 'wb') as file_pi:
    pickle.dump(history.history, file_pi)


