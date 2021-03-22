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
name='batch16'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X1=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((NUM,2))
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

name='batch17'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X2=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y2=np.zeros((NUM,2))
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

name='batch18'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X3=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y3=np.zeros((NUM,2))
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

name='batch19'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X4=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y4=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X4[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y4[i,:]=L

name='batch20'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X5=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y5=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X5[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y5[i,:]=L

name='batch21'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X6=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y6=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X6[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y6[i,:]=L

name='batch22'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X7=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y7=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X7[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y7[i,:]=L

name='batch23'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X8=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y8=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X8[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y8[i,:]=L

name='batch24'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X9=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y9=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X9[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y9[i,:]=L

name='batch25'
n=840                      
num_array=2
NUM=n*num_array
rate=0.2;
X10=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y10=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X10[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y10[i,:]=L




a=np.append(X1,X2,axis=0)
b=np.append(a,X3,axis=0)
c=np.append(b,X4,axis=0)
d=np.append(c,X5,axis=0)
e=np.append(d,X6,axis=0)
f=np.append(e,X7,axis=0)
g=np.append(f,X8,axis=0)
h=np.append(g,X9,axis=0)
X=np.append(h,X10,axis=0)

a=np.append(Y1,Y2,axis=0)
b=np.append(a,Y3,axis=0)
c=np.append(b,Y4,axis=0)
d=np.append(c,Y5,axis=0)
e=np.append(d,Y6,axis=0)
f=np.append(e,Y7,axis=0)
g=np.append(f,Y8,axis=0)
h=np.append(g,Y9,axis=0)
Y=np.append(h,Y10,axis=0)

name_tem='./DATA-test12.npz'
np.savez(name_tem,X=X,Y=Y)

