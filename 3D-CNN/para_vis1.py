#!/WORK/bnu_kxia_1/wdwang/neural-network/anaconda3/envs/test2/bin/python
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense,Activation,Convolution2D,Flatten,MaxPooling2D,BatchNormalization,Dropout
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.callbacks import ModelCheckpoint,EarlyStopping
from keras.models import Model
from tensorflow.keras import backend as K
import sys
import os
from scipy import misc
from PIL import Image
import scipy.io as sio
plt.switch_backend('Agg')
from tensorflow.python.keras.models import load_model

model=load_model('weights1best.h5')
name_tem='/WORK/bnu_kxia_1/wdwang/neural-network/3D-CNN/DATA-3dvis.npz'
data_tem=np.load(name_tem)
X=data_tem['X'];Y=data_tem['Y'];Z=data_tem['Z'];
print(X.shape,Y.shape,Z.shape)
X=X.reshape(X.shape[0],10,36,36,1)
print(X.shape)

input_image=np.zeros((1,10,36,36,1));
input_image[0,:,:,:,:]=X[0,:,:,:,:];
for i in range(14):#[0,7]
    layer_1 = K.function([model.layers[0].input], [model.layers[i].output])
    f1 = layer_1([input_image])[0]
    print(f1.shape)
print('This is the end !')

a=np.zeros((X.shape[0],10));b=np.zeros((X.shape[0],4));
for i in range(X.shape[0]):
    input_image=np.zeros((1,10,36,36,1));
    input_image[0,:,:,:,:]=X[i,:,:,:,:];
    n=11;str='Dense2'
    layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
    f1 = layer_1([input_image])[0]
    a[i,:]=f1;
    n=13;str='softmax'
    layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
    f1 = layer_1([input_image])[0]
    b[i,:]=f1;

name_tem='3dlabel1.mat'
sio.savemat(name_tem, {'Y':Y,'Z':Z})
name_tem='3dpara1.mat'
sio.savemat(name_tem, {'a':a,'b':b})

           



