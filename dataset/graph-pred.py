#!/home/wdwang/anaconda3/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
plt.switch_backend('Agg')
ruler_speed=10**(-2.85);ruler_std=0.4;sz=50;
name='batch1'
name_tem='./%s/%s_Para.npz'%(name,name)
data_tem=np.load(name_tem)
F0=data_tem['F0'];Epsilon=data_tem['Epsilon']
X=F0[:,2];Y=F0[:,0];
I=np.ones((F0.shape[0],3));

name='batch0'
for i in range(F0.shape[0]):
    name_tem='./%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I']
speed=(I[:,1]**2+I[:,2]**2)**0.5
color=np.zeros((I.shape[0],3))



