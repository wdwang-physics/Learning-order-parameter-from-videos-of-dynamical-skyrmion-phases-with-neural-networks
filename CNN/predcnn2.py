import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import plot_model
import scipy.io as sio
from tensorflow.python.keras.models import load_model
#load X data
name_tem='DATA-test13.npz'
data_tem=np.load(name_tem)
X=data_tem['X'];
print(X.shape)
X1=X.reshape(X.shape[0],X.shape[2],X.shape[3]);
X2=X1.reshape(X.shape[0],X.shape[2],X.shape[3],1);
X=X2;
print(X.shape)

my_model=load_model('weights2best.h5')
y = my_model.predict(X)
print('Created model and loaded weights from hdf5 file')
print(y.shape)
name_tem='./predcnn2.mat'
#sio.savemat(name_tem, {'y':y})
name_tem='./cnnlabel5.mat'
data_tem=sio.loadmat(name_tem)
Y=data_tem['Y'];
L=np.zeros((Y.shape[0],1))
for i in range(Y.shape[0]):
    A = Y[i, :];
    a = np.argmax(A);
    L[i] = a;

L1 = np.zeros((Y.shape[0], 1))
for i in range(Y.shape[0]):
    A = y[i, :];
    a = np.argmax(A);
    L1[i] = a;

X=L-L1;
x=np.abs(X)
a=x.sum(axis=1)
b=np.nonzero(a);b=np.array(b,dtype=float);
c=np.size(b);
accuracy=1-c/840.0
print(accuracy)