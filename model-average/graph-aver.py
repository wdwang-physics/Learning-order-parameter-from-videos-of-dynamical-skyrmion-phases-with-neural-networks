#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
plt.switch_backend('Agg')
import scipy.io as sio
name='batch1'
name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_Para.npz'%(name,name)
data_tem=np.load(name_tem)
F0=data_tem['F0'];Epsilon=data_tem['Epsilon']
name_tem='./average.mat'
data_tem=sio.loadmat(name_tem)
I=data_tem['L'];
X=F0[:,2];
Y=F0[:,0];
color=np.zeros((I.shape[0],3))
MC=0;ML=0;PC=0;PG=0;ERRO=0;
for i in range(I.shape[0]):
    if all(I[i,:]==np.array([1,0,0,0])):
       color[i,:]=np.array([255,166,195])/255
       PG+=1
    elif all(I[i,:]==np.array([0,1,0,0])):
       color[i,:]=np.array([130,255,213])/255
       PC+=1
    elif all(I[i,:]==np.array([0,0,1,0])):
       color[i,:]=np.array([138,233,255])/255
       ML+=1
    elif all(I[i,:]==np.array([0,0,0,1])):
       color[i,:]=np.array([255,255,200])/255
       MC+=1
X=np.log10(X);Y=np.log10(Y);
sz=50
plt.xlim((-2.1, 0))
plt.ylim((-4.1, 0.1))
plt.scatter(X,Y,sz,c=color)
plt.xlabel('F_p')
plt.ylabel('FD')
name_tem='./Graph1'
plt.savefig(name_tem)
