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
    size_m = 72;size_n = 72
    I = Image.open(input_dir)
    I_size = I.resize((size_m, size_n),Image.ANTIALIAS)
    L = I_size.convert('L')
    L.save(out_dir)
    return L

####
#main
name='batch0'
n=840                      
num_array=1
NUM=n*num_array
rate=0.2;
X1=np.zeros((NUM,1,np.int(360*rate),np.int(360*rate)));Y1=np.zeros((NUM,2))
for i in range(NUM):
    num_tem1=np.int(i/num_array);num_tem2=0
    name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    name_tem1='./%s/%s_%i_fig%i.png'%(name,name,num_tem1,num_tem2)
    L=changeImagesize(name_tem,name_tem1)
    data=ImageToMatrix(name_tem1)
    X1[i,0,:,:]=data
    name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num_tem1,num_tem2)
    data_tem=np.load(name_tem)
    L=data_tem['L']
    Y1[i,:]=L
X=X1;Y=Y1;
name_tem='./DATA-test13.npz'
np.savez(name_tem,X=X)
name_tem1='./cnnlabel5.mat'
sio.savemat(name_tem1, {'Y':Y})

