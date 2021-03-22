#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import time as tm
from numba import jit
import scipy.io as sio
####
@jit('Tuple((float64[:,:],float64[:,:]))(float64[:,:,:,:])',nopython=True)
def index(r_plus):
    distance_plus=np.power((np.power(r_plus[:,:,:,0],2)+np.power(r_plus[:,:,:,1],2)),0.5);
    #print(numba.typeof(distance_plus))
    distance=np.zeros((r_plus.shape[2],1))
    direction=np.zeros((r_plus.shape[2],2))
    ri=np.ones(9)
    for i in range(r_plus.shape[2]):
        for j in range(3):
            ri[j*3:j*3+3]=distance_plus[j,:,i]
        index_tem=np.argmin(ri)
        index_tem1=np.int(index_tem/3);index_tem2=np.mod(index_tem,3)
        distance[i]=distance_plus[index_tem1,index_tem2,i];
        direction[i,:]=r_plus[index_tem1,index_tem2,i,:]/distance[i];
    return distance,direction
####
@jit('Tuple((float64[:,:],float64[:,:],float64[:,:]))(float64[:,:,:],float64[:],int64)',nopython=True)
def classify(history,velocity_mean,num):
    L_0=36
    inter=0.1;
    Sky=history[num,:,:]
    Sky_plus=np.zeros((3,3,history.shape[1],2));
    for i in [0,1,2]:
        for j in [0,1,2]:
            Sky_plus[i,j,:,:]=Sky
            Sky_plus[i,j,:,0]=Sky_plus[i,j,:,0]+np.array(i-1)*L_0
            Sky_plus[i,j,:,1]=Sky_plus[i,j,:,1]+np.array(j-1)*L_0
    radius_sta=np.zeros((history.shape[1]*(history.shape[1]-1),2));
    distance_sta=np.zeros((history.shape[1]*(history.shape[1]-1),1));
    for i in range(history.shape[1]):
        Skyi=Sky_plus[1,1,i,:]
        Sky_plus_tem=np.zeros((3,3,(history.shape[1]-1),2))       
        Sky_plus_tem[:,:,0:i,:]=Sky_plus[:,:,0:i,:]
        Sky_plus_tem[:,:,i:,:]=Sky_plus[:,:,i+1:,:]
        r_plus=-Sky_plus_tem+Skyi
        distance,direction=index(r_plus)
        r=direction*distance
        for j in range(history.shape[1]-1):
            distance_sta[j+i*(history.shape[1]-1),:]=distance[j,:]
            radius_sta[j+i*(history.shape[1]-1),:]=r[j,:]
    X=np.arange(0,L_0/2,inter);Y=np.arange(0,L_0/2,inter)
    P=np.ones((X.shape[0],Y.shape[0]));
    D=np.ones((X.shape[0],1))
    for i in range(X.shape[0]):
        index_D=np.where((np.abs(distance_sta[:,0]-X[i])<(inter/2)))
        D[i,0]=np.sum(1/distance_sta[index_D[0],:]/np.pi/2)
        for j in range(Y.shape[0]):
            x_tem=np.abs(radius_sta[:,0]-X[i]);
            y_tem=np.abs(radius_sta[:,1]-Y[j]);
            r_tem=(x_tem**2+y_tem**2)**0.5
            index_P=np.where(r_tem<(inter/2))
            P[i,j]=index_P[0].shape[0];
    I=np.ones((1,3))
    I[0,0]=np.std(D[100:]);I[0,1:]=velocity_mean   
    return P,D,I
####
#main
ALL=np.int(sys.argv[2]);NUM=np.int(sys.argv[1])
name_tem='./%s/%s_Para.npz'%(sys.argv[3],sys.argv[3])
data_tem=np.load(name_tem)
F0=data_tem['F0'];
inter=np.int(F0.shape[0]/ALL)
sur=np.mod(F0.shape[0],ALL)
num=3950;limit=20;
if NUM<sur:
   for i in range(inter+1): 
       tt1=tm.time()
       name='./%s/%s_%i.npz'%(sys.argv[3],sys.argv[3],NUM*(inter+1)+i)
       if os.path.exists(name)==0:
          continue
       data_tem=np.load(name)
       history=data_tem['history'];velocity_mean=data_tem['velocity_mean']
       P,D,I=classify(history,velocity_mean,num)
       name='./%s/%s_%i_I'%(sys.argv[3],sys.argv[3],(NUM*(inter+1)+i))
       sio.savemat(name, {'I':I})
       np.savez(name,I=I)
       tt2=tm.time();
       #print('the time used equals %f'%(tt2-tt1))
       #tm.sleep(np.abs(limit-(tt2-tt1)))
else:
   for i in range(inter):
       tt1=tm.time()
       name='./%s/%s_%i.npz'%(sys.argv[3],sys.argv[3],(sur+inter*NUM+i))
       if os.path.exists(name)==0:
          continue
       data_tem=np.load(name)
       history=data_tem['history'];velocity_mean=data_tem['velocity_mean']
       P,D,I=classify(history,velocity_mean,num)
       name='./%s/%s_%i_I'%(sys.argv[3],sys.argv[3],(sur+inter*NUM+i))
       sio.savemat(name, {'I':I})
       np.savez(name,I=I)
       tt2=tm.time();
       #print('the time used equals %f'%(tt2-tt1))
       #tm.sleep(np.abs(limit-(tt2-tt1)))
   #tm.sleep(limit)


