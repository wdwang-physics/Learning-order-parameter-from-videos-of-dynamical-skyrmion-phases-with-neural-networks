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

for i in range(F0.shape[0]):
    name_tem='./%s/%s_%i_I.npz'%(sys.argv[1],sys.argv[1],i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I']
speed=(I[:,1]**2+I[:,2]**2)**0.5
color=np.zeros((I.shape[0],3))
for i in range(I.shape[0]):  
    if (I[i,0]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       #PG+=1
    elif (I[i,0]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       #PC+=1
    elif (I[i,0]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
      # ML+=1
    elif (I[i,0]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
      # MC+=1
index=np.argwhere(I[:,0]==1)
color[index,:]=np.array([1,1,1])
fig=plt.figure(1,dpi=300,facecolor=None, edgecolor=None, frameon=False)
plt.axes(xscale = "log",yscale = "log")
plt.xlim((10**(-2.03), 10**(-0.05)))
plt.ylim((10**(-4.1), 10**(0.1)))
plt.scatter(X,Y,sz,c=color)
plt.xlabel('$F_p$')
plt.ylabel('$F_D$')
name_tem='./%s/%s_Graph1.eps'%(sys.argv[1],sys.argv[1])
plt.savefig(name_tem)



