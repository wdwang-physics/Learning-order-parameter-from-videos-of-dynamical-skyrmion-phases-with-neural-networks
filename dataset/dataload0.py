#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
from scipy import misc
from PIL import Image
####
def ImageToMatrix(filename):
    im = Image.open(filename)  
    width,height = im.size 
    data = im.getdata()
    data = np.matrix(data,dtype='float')/255.0
    new_data = np.reshape(data,(height,width))
    return new_data

def changeImagesize(input_dir,out_dir):
    size_m = 72;size_n = 72
    I = Image.open(input_dir)
    I_size = I.resize((size_m, size_n),Image.ANTIALIAS)
    L = I_size.convert('L')
    L.save(out_dir)
    return L

####
#main
name='batch1'
n=840                      
num_array=1
NUM=n*num_array
rate=0.2;
X1=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((NUM,2));Z1=np.zeros((NUM,1))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X1[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y1[i,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z1[i,:]=I[:,0];
        


name='batch2'
n=840                      
num_array=1
NUM=n*num_array
rate=0.2;
X2=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y2=np.zeros((NUM,2));Z2=np.zeros((NUM,1))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X2[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y2[i,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z2[i,:]=I[:,0];

name='batch3'
n=840                      
num_array=1
NUM=n*num_array
rate=0.2;
X3=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y3=np.zeros((NUM,2));Z3=np.zeros((NUM,1))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X3[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y3[i,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z3[i,:]=I[:,0];

a=np.append(X1,X2,axis=0)
X=np.append(a,X3,axis=0)

a=np.append(Y1,Y2,axis=0)
Y=np.append(a,Y3,axis=0)

a=np.append(Z1,Z2,axis=0)
Z=np.append(a,Z3,axis=0)

name_tem='./DATA-vis.npz'
np.savez(name_tem,X=X,Y=Y,Z=Z)

