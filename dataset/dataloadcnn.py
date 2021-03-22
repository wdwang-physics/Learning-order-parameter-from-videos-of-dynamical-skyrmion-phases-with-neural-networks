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
k=840;N=k*1;rate=0.1;
X=np.zeros((N,np.int(360*rate),np.int(360*rate)));Y=np.zeros((N,2))
name='batch1';num_tem2=0;
for i in range(k):
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,i,num_tem2)
    if os.path.exists(name_tem)==0:
       continue
    im=mpimg.imread(name_tem);
    im_tem=misc.imresize(im,rate)
    im_tem=im_tem[:,:,:3]
    #print(im_tem.shape)
    img= to_grayscale(im_tem)
    X[i,:,:]=img
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,i)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y[i,:]=L

name_tem='./DATApredcnn.npz'
name_tem1='./cnnlabel.mat'
np.savez(name_tem,X=X)
#np.savetxt(name_tem1,Y,fmt="%d", delimiter=",")
sio.savemat(name_tem1, {'Y':Y})


