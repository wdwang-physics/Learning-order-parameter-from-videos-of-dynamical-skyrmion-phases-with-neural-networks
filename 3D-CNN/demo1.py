import numpy as np
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras.layers import Dense,Activation,Convolution3D,Flatten,MaxPooling3D,Dropout,BatchNormalization
from keras.callbacks import ModelCheckpoint,EarlyStopping
import matplotlib.pyplot as plt
import sys
plt.switch_backend('Agg')
#load the Skyrmion data
name_tem='/WORK/bnu_kxia_1/wdwang/neural-network/3D-CNN/DATA3dcnn6.npz'
data_tem=np.load(name_tem)
X=data_tem['X'];Y=data_tem['Y']
index=np.arange(X.shape[0])
np.random.shuffle(index)
X=X[index,:,:,:];Y=Y[index,:]
X=X.reshape(X.shape[0],10,36,36,1)
print(X.shape,Y.shape)
#X=X[:1000,:,:,:,:];Y=Y[:1000,:];print(X.shape,Y.shape)
#builf CNN
model=keras.Sequential()
#Conv layer1 output shape (32,10,36,36)
model.add(Convolution3D(batch_input_shape=(None,10,36,36,1),filters=32,kernel_size=(6,6,6),strides=2,padding='same',data_format="channels_last"))
model.add(BatchNormalization())
model.add(Activation('relu'))
#Pooling layer 1(max pooling) output shape(32,3,6,6)
model.add(MaxPooling3D(pool_size=(2,6,6),strides=2,padding='same',data_format='channels_last'))
model.add(Convolution3D(filters=16,kernel_size=(6,6,6),strides=2,padding='same',data_format="channels_last"))
model.add(BatchNormalization())
model.add(Activation('relu'))
#Pooling layer 1(max pooling) output shape(32,3,6,6)
model.add(MaxPooling3D(pool_size=(2,6,6),strides=2,padding='same',data_format='channels_last'))
model.add(Flatten())
model.add(Dense(128))
model.add(Dropout(0.5))
model.add(Dense(4))
model.add(Activation('softmax'))
#define optimizer
adam=keras.optimizers.Adam(lr=5e-5)
model.compile(optimizer=adam,loss='categorical_crossentropy',metrics=['accuracy'])
filepath = "weights1best.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True,
                            mode='max')
earlyStopping=EarlyStopping(monitor='accuracy', patience=8, verbose=1, mode='max')
callbacks_list = [checkpoint,earlyStopping]
history = model.fit(X,Y, validation_split=0.2,epochs=60,batch_size=20,callbacks=callbacks_list,verbose=2)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('3dcnn1-1.png')
plt.close()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('3dcnn1-2.png')
plt.close()
##################
name_tem=sys.argv[0]
print (model.summary())