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
    size_m = 36;size_n = 36
    I = Image.open(input_dir)
    I_size = I.resize((size_m, size_n),Image.ANTIALIAS)
    L = I_size.convert('L')
    L.save(out_dir)
    return L

####
#main
name='batch1'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X1=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((n,4));Z1=np.zeros((n,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X1[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y1[num_tem1,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z1[num_tem1,0]=I[:,0];Z1[num_tem1,1]=(I[:,1]**2+I[:,2]**2)**0.5        

name='batch2'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X2=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y2=np.zeros((n,4));Z2=np.zeros((n,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X2[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y2[num_tem1,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z2[num_tem1,0]=I[:,0];Z2[num_tem1,1]=(I[:,1]**2+I[:,2]**2)**0.5

name='batch3'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X3=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y3=np.zeros((n,4));Z3=np.zeros((n,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X3[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y3[num_tem1,:]=L
    name_tem='./%s/%s_%i_I.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    I=data_tem['I'];Z3[num_tem1,0]=I[:,0];Z3[num_tem1,1]=(I[:,1]**2+I[:,2]**2)**0.5


a=np.append(X1,X2,axis=0)
X=np.append(a,X3,axis=0)

a=np.append(Y1,Y2,axis=0)
Y=np.append(a,Y3,axis=0)

a=np.append(Z1,Z2,axis=0)
Z=np.append(a,Z3,axis=0)

name_tem='./DATA-3dvis.npz'
np.savez(name_tem,X=X,Y=Y,Z=Z)

