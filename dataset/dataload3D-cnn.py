#!/WORK/app/anaconda/5.3.1/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
from scipy import misc
import scipy.io as sio
####
def to_grayscale(im, weights = np.c_[0.2989, 0.5870, 0.1140]):
    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    gray=np.sum(tile * im, axis=2)
    return gray
####
#main
k=840;N=k*10;num_array=10;
rate=0.1;
X=np.zeros((k,10,np.int(360*rate),np.int(360*rate),1));Y=np.zeros((k,4))
name='batch5';a=np.zeros((k,2));
for i in range(k):
    num_tem1=np.int(i);
    for j in range(num_array):
        num_tem2=np.mod(j,num_array)
        name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
        if os.path.exists(name_tem)==0:
           continue
        im=mpimg.imread(name_tem);
        a[i,0]=num_tem1;a[i,1]=num_tem2;
        im_tem=misc.imresize(im,rate)
        im_tem=im_tem[:,:,:3]
        #print(im_tem.shape)
        img= to_grayscale(im_tem)
        X[i,j,:,:,0]=img
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y[i,:]=L

name_tem='./DATAfourphase.npz'
name_tem1='./fourphase.mat'
np.savez(name_tem,X=X)
#np.savetxt(name_tem1,Y,fmt="%d", delimiter=",")
sio.savemat(name_tem1, {'Y':Y})
name_tem2='./%s_dataset/check.txt'%(name)
np.savetxt(name_tem2,a,fmt="%d", delimiter=",")

