#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
import scipy.io as sio
from scipy import misc
####
def to_grayscale(im, weights = np.c_[0.2989, 0.5870, 0.1140]):
    
    tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
    gray=np.sum(tile * im, axis=2)
    return gray
####
#main
n1=20;n2=20;n3=20;n4=20
rate=0.1;num_array=10;
X=np.zeros((n1,10,np.int(360*rate),np.int(360*rate)));
for i in range(n1):
    num_tem1=np.int(i);
    for j in range(num_array):
        num_tem2=np.mod(j,num_array)
        name_tem='./MC/1-%i_fig%i.png'%(num_tem1,num_tem2)
        #a[num_array*i+j,0]=num_tem1;a[num_array*i+j,1]=num_tem2;
        if os.path.exists(name_tem)==0:
           continue
        im=mpimg.imread(name_tem);
        im_tem=misc.imresize(im,rate)
        im_tem=im_tem[:,:,:3]
        #print(im_tem.shape)
        img= to_grayscale(im_tem)
        X[i,j,:,:]=img
name_tem='./mc.npz'
np.savez(name_tem,X=X)

for i in range(n2):
    num_tem1=np.int(i);
    for j in range(num_array):
        num_tem2=np.mod(j,num_array)
        name_tem='./ML/2-%i_fig%i.png'%(num_tem1,num_tem2)
        #b[num_array*i+j,0]=num_tem1;b[num_array*i+j,1]=num_tem2;
        if os.path.exists(name_tem)==0:
           continue
        im=mpimg.imread(name_tem);
        im_tem=misc.imresize(im,rate)
        im_tem=im_tem[:,:,:3]
        #print(im_tem.shape)
        img= to_grayscale(im_tem)
        X[i,j,:,:]=img
        #L=np.array([1,0])  #moving
        #Y[n1+i,:]=L
name_tem='./ml.npz'
np.savez(name_tem,X=X)

for i in range(n3):
    num_tem1=np.int(i);
    for j in range(num_array):
        num_tem2=np.mod(j,num_array)
        name_tem='./PC/3-%i_fig%i.png'%(num_tem1,num_tem2)
        #c[num_array*i+j,0]=num_tem1;c[num_array*i+j,1]=num_tem2;
        if os.path.exists(name_tem)==0:
           continue
        im=mpimg.imread(name_tem);
        im_tem=misc.imresize(im,rate)
        im_tem=im_tem[:,:,:3]
        #print(im_tem.shape)
        img= to_grayscale(im_tem)
        X[i,j,:,:]=img
        #L=np.array([0,1])  #pinning
        #Y[n1+n2+i,:]=L

name_tem='./pc.npz'
np.savez(name_tem,X=X)

for i in range(n4):
    num_tem1=np.int(i);
    for j in range(num_array):
        num_tem2=np.mod(j,num_array)
        name_tem='./PG/4-%i_fig%i.png'%(num_tem1,num_tem2)
       # d[num_array*i+j,0]=num_tem1;d[num_array*i+j,1]=num_tem2;
        if os.path.exists(name_tem)==0:
           continue
        im=mpimg.imread(name_tem);
        im_tem=misc.imresize(im,rate)
        im_tem=im_tem[:,:,:3]
        #print(im_tem.shape)
        img= to_grayscale(im_tem)
        X[i,j,:,:]=img
        #L=np.array([0,1])  #pinning
        #Y[n1+n2+n3+i,:]=L
name_tem='./pg.npz'
np.savez(name_tem,X=X)






