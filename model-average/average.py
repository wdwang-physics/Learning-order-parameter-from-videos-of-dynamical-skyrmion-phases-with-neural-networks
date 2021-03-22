#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.io as sio
I=np.zeros((840,3))
ruler_speed=10**(-2.85)
ruler_std=0.4
color=np.zeros((I.shape[0],3))
label=np.zeros((I.shape[0],4))
k=np.ones((I.shape[0],100))

name='batch1'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L1=label

name='batch2'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L2=label

name='batch3'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L3=label

name='batch4'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L4=label

name='batch5'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L5=label

name='batch6'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L6=label

name='batch7'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L7=label

name='batch8'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L8=label

name='batch9'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L9=label

name='batch10'
label=np.zeros((I.shape[0],4))
for i in range(I.shape[0]):
    name_tem='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I[i,:]=data_tem['I'];m=data_tem['k'];m=m.reshape(100);k[i,:]=m
speed=(I[:,1]**2+I[:,2]**2)**0.5
n=k.sum(axis=1);R=n/100
for i in range(I.shape[0]):
    if (R[i]==0) and (I[i,1]==0):
       color[i,:]=np.array([255,255,255])/255
       label[i,:]=np.array([100,100,100,100])
    elif (R[i]<ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([255,166,195])/255
       label[i,:]=np.array([1,0,0,0])
       #PG+=1
    elif (R[i]>ruler_std) and (speed[i]<ruler_speed):
       color[i,:]=np.array([130,255,213])/255
       label[i,:]=np.array([0,1,0,0])
       #PC+=1
    elif (R[i]<ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([138,233,255])/255
       label[i,:]=np.array([0,0,1,0])
       #ML+=1
    elif (R[i]>ruler_std) and (speed[i]>ruler_speed):
       color[i,:]=np.array([255,255,200])/255
       label[i,:]=np.array([0,0,0,1])
       #MC+=1
L10=label


name='./labe1.mat'
sio.savemat(name,{'L1':L1,})
name='./labe2.mat'
sio.savemat(name,{'L2':L2,})
name='./labe3.mat'
sio.savemat(name,{'L3':L3,})
name='./labe4.mat'
sio.savemat(name,{'L4':L4,})
name='./labe5.mat'
sio.savemat(name,{'L5':L5,})
name='./labe6.mat'
sio.savemat(name,{'L6':L6,})
name='./labe7.mat'
sio.savemat(name,{'L7':L7,})
name='./labe8.mat'
sio.savemat(name,{'L8':L8,})
name='./labe9.mat'
sio.savemat(name,{'L9':L9,})
name='./labe10.mat'
sio.savemat(name,{'L10':L10,})


n=10.0
L0=(L1+L2+L3+L4+L5+L6+L7+L8+L9+L10)/n;L=np.round(L0)
name='./average0.mat'
sio.savemat(name,{'L0':L0,})
name='./average.mat'
sio.savemat(name,{'L':L,})



