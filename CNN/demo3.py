import numpy as np
np.random.seed(1337)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import plot_model
from tensorflow.keras.layers import Dense,Activation,Convolution2D,Flatten,MaxPooling2D,BatchNormalization,Dropout
import sys
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import load_model
plt.switch_backend('Agg')
#load the Skyrmion data
#X_shape (-1, 1,360, 360), y_shape (-1,2 )
name_tem='DATA-test12.npz'
data_tem=np.load(name_tem)
X=data_tem['X'];Y=data_tem['Y']
print(X.shape,Y.shape)
index=np.arange(X.shape[0])
np.random.shuffle(index)
X=X[index,:,:,:];Y=Y[index,:]
#data pre-processing
X1=X.reshape(X.shape[0],X.shape[2],X.shape[3]);
X2=X1.reshape(X.shape[0],X.shape[2],X.shape[3],1);
X=X2;
print(X.shape,Y.shape)
#builf CNN
model=keras.Sequential()
#Conv layer1 output shape (32,36,36)
model.add(Convolution2D(batch_input_shape=(None,72,72,1),filters=32,kernel_size=5,strides=2,padding='same',data_format='channels_last'))
model.add(BatchNormalization())
model.add(Activation('relu'))
#Pooling layer 1(max pooling) output shape(32,18,18)
model.add(MaxPooling2D(pool_size=2,strides=2,padding='same',data_format='channels_last'))
#Conv layer 2 output shape (64,18,18)
model.add(Convolution2D(64,5,strides=1,padding='same',data_format='channels_last'))
model.add(BatchNormalization())
model.add(Activation('relu'))
#Pooling layer 2 (max pooling) output shape (64,9,9)
model.add(MaxPooling2D(2,2,'same',data_format='channels_last'))
#Fully connected layer 1 input shape (64*9*9)=6336, output shape (1024)
model.add(Flatten())
model.add(Dense(1024))
#model.add(Activation('relu'))
##############
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Dense(2))
model.add(Activation('softmax'))
#define optimizer
adam=keras.optimizers.Adam(lr=7e-5)
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])
filepath = "weights3best.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True,
                            mode='max')
earlyStopping=EarlyStopping(monitor='accuracy', patience=8, verbose=1, mode='max')
callbacks_list = [checkpoint,earlyStopping]
history = model.fit(X,Y, validation_split=0.2, epochs=60, batch_size=50, callbacks=callbacks_list,verbose=2)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='lower right')
plt.savefig('cnn3-1.eps', format='eps', dpi=100)
plt.close()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.savefig('cnn3-2.eps', format='eps', dpi=100)
plt.close()
##################
name_tem=sys.argv[0]
print (model.summary())
import pickle
with open('trainHistoryDict3.txt', 'wb') as file_pi:
    pickle.dump(history.history, file_pi)


