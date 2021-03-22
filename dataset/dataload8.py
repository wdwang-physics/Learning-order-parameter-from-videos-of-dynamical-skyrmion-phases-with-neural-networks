#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
from scipy import misc
from PIL import Image
import scipy.io as sio
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

n=1500;
path1='MC';path2='ML';
path3='PC';path4='PG';
L1=np.array([0,0,0,1]);  #MC
L2=np.array([0,0,1,0]);  #ML
L3=np.array([0,1,0,0]);  #PC
L4=np.array([1,0,0,0]);  #PG
num_array=10
NUM=n*num_array
rate=0.1;

name=path1;m=1;
X1=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%i-%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    name_tem1='./%s/%i_%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X1[num_tem1,num_tem2,:,:]=data
    Y1[num_tem1,:]=L1

name=path2;m=2;
X2=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y2=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%i-%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    name_tem1='./%s/%i_%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X2[num_tem1,num_tem2,:,:]=data
    Y2[num_tem1,:]=L2

name=path3;m=3;
X3=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y3=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%i-%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    name_tem1='./%s/%i_%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X3[num_tem1,num_tem2,:,:]=data
    Y3[num_tem1,:]=L3

name=path4;m=4;
X4=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y4=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%i-%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    name_tem1='./%s/%i_%i_fig%i.png'%(name,m,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X4[num_tem1,num_tem2,:,:]=data
    Y4[num_tem1,:]=L4

a=np.append(X1,X2,axis=0)
b=np.append(a,X3,axis=0)
X=np.append(b,X4,axis=0)
a=np.append(Y1,Y2,axis=0)
b=np.append(a,Y3,axis=0)
Y=np.append(b,Y4,axis=0)

name_tem='./DATA3dcnn6000.npz'
np.savez(name_tem,X=X,Y=Y)


