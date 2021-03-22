#!/WORK/app/anaconda/5.3.1/bin/python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import scipy.io as sio
plt.switch_backend('Agg')
N=840
I=np.ones((N,3))
for i in range(N):
    name_tem='./%s/%s_%i_I.npz'%(sys.argv[1],sys.argv[1],i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I']
speed=(I[:,1]**2+I[:,2]**2)**0.5
ruler_speed=10**(-4)
ruler_std=0.3
K=np.ones((N,4))
for i in range(I.shape[0]):  
    if (I[i,0]<ruler_std) and (speed[i]<ruler_speed):
       K[i,:]=np.array([1,0,0,0])         #PG+=1
    elif (I[i,0]>ruler_std) and (speed[i]<ruler_speed):
       K[i,:]=np.array([0,0,0,1])           #PC+=1
    elif (I[i,0]<ruler_std) and (speed[i]>ruler_speed):
       K[i,:]=np.array([0,1,0,0])            #ML+=1
    elif (I[i,0]>ruler_std) and (speed[i]>ruler_speed):
       K[i,:]=np.array([0,0,1,0])            #MC+=1
#name_tem1='./%s_dataset/%s_label.txt'%(sys.argv[1],sys.argv[1])
#np.savetxt(name_tem1,K,fmt="%d", delimiter=",")
name_tem1='./fourphase3.mat'
sio.savemat(name_tem1, {'Y':K})


