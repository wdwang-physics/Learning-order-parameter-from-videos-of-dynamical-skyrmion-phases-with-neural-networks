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

####
#main

name='batch27'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X2=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y2=np.zeros((n,4))
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


name='batch28'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X3=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y3=np.zeros((n,4))
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


name='batch29'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X4=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y4=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X4[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y4[num_tem1,:]=L


name='batch26'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X5=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y5=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X5[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y5[num_tem1,:]=L

name='batch31'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X6=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y6=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X6[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y6[num_tem1,:]=L

name='batch32'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X7=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y7=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X7[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y7[num_tem1,:]=L

name='batch33'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X8=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y8=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X8[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y8[num_tem1,:]=L

name='batch34'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X9=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y9=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X9[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y9[num_tem1,:]=L

name='batch35'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X10=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y10=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X10[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y10[num_tem1,:]=L

name='batch16'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X11=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y11=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X11[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y11[num_tem1,:]=L

name='batch17'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X12=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y12=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X12[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y12[num_tem1,:]=L

name='batch18'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X13=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y13=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X13[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y13[num_tem1,:]=L

name='batch19'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X14=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y14=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X14[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y14[num_tem1,:]=L

name='batch20'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X15=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y15=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X15[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y15[num_tem1,:]=L

name='batch21'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X16=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y16=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X16[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y16[num_tem1,:]=L

name='batch22'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X17=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y17=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X17[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y17[num_tem1,:]=L

name='batch23'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X18=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y18=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X18[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y18[num_tem1,:]=L

name='batch24'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X19=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y19=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X19[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y19[num_tem1,:]=L

name='batch25'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X20=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y20=np.zeros((n,4))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=np.mod(i,num_array)
    name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X20[num_tem1,num_tem2,:,:]=data
    name_tem='./%s_dataset/%s_%i_fig.npz'%(name,name,num_tem1)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y20[num_tem1,:]=L

a=np.append(X20,X2,axis=0)
b=np.append(a,X3,axis=0)
c=np.append(b,X4,axis=0)
d=np.append(c,X5,axis=0)
e=np.append(d,X6,axis=0)
f=np.append(e,X7,axis=0)
g=np.append(f,X8,axis=0)
h=np.append(g,X9,axis=0)
i=np.append(h,X10,axis=0)
j=np.append(i,X11,axis=0)
k=np.append(j,X12,axis=0)
l=np.append(k,X13,axis=0)
m=np.append(l,X14,axis=0)
n=np.append(m,X15,axis=0)
o=np.append(n,X16,axis=0)
p=np.append(o,X17,axis=0)
q=np.append(p,X18,axis=0)
X=np.append(q,X19,axis=0)

a=np.append(Y20,Y2,axis=0)
b=np.append(a,Y3,axis=0)
c=np.append(b,Y4,axis=0)
d=np.append(c,Y5,axis=0)
e=np.append(d,Y6,axis=0)
f=np.append(e,Y7,axis=0)
g=np.append(f,Y8,axis=0)
h=np.append(g,Y9,axis=0)
i=np.append(h,Y10,axis=0)
j=np.append(i,Y11,axis=0)
k=np.append(j,Y12,axis=0)
l=np.append(k,Y13,axis=0)
m=np.append(l,Y14,axis=0)
n=np.append(m,Y15,axis=0)
o=np.append(n,Y16,axis=0)
p=np.append(o,Y17,axis=0)
q=np.append(p,Y18,axis=0)
Y=np.append(q,Y19,axis=0)

name_tem='./DATA3dcnn6.npz'
np.savez(name_tem,X=X,Y=Y)

