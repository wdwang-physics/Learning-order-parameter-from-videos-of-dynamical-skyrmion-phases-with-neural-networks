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
name='batch0'
n=840                      
num_array=10
NUM=n*num_array
rate=0.1;
X1=np.zeros((n,10,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((n,4))
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
X=X1;Y=Y1;
name_tem='./DATA3dcnn8.npz'
np.savez(name_tem,X=X)
name_tem1='./3dcnnlabel2.mat'
sio.savemat(name_tem1, {'Y':Y})

