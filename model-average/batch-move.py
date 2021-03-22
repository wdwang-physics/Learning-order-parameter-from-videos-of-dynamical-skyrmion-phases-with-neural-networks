# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:30:24 2020

@author: Administrator
"""

import sys
import numpy as np
import scipy.io as sio
import shutil,os
name_tem='./average.mat'
data_tem=sio.loadmat(name_tem)
L=data_tem['L'];

name_tem='./labe1.mat'
data_tem=sio.loadmat(name_tem)
L1=data_tem['L1'];

name_tem='./labe2.mat'
data_tem=sio.loadmat(name_tem)
L2=data_tem['L2'];

name_tem='./labe3.mat'
data_tem=sio.loadmat(name_tem)
L3=data_tem['L3'];

name_tem='./labe4.mat'
data_tem=sio.loadmat(name_tem)
L4=data_tem['L4'];

name_tem='./labe5.mat'
data_tem=sio.loadmat(name_tem)
L5=data_tem['L5'];

name_tem='./labe6.mat'
data_tem=sio.loadmat(name_tem)
L6=data_tem['L6'];

name_tem='./labe7.mat'
data_tem=sio.loadmat(name_tem)
L7=data_tem['L7'];

name_tem='./labe8.mat'
data_tem=sio.loadmat(name_tem)
L8=data_tem['L8'];

name_tem='./labe9.mat'
data_tem=sio.loadmat(name_tem)
L9=data_tem['L9'];

name_tem='./labe10.mat'
data_tem=sio.loadmat(name_tem)
L10=data_tem['L10'];

name_tem='/WORK/bnu_kxia_1/wdwang/batch0'
if os.path.exists(name_tem)==0:
   os.mkdir(name_tem)


for i in range(L.shape[0]):
    if all(L1[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch1/batch1_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch1/batch1_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L2[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch2/batch2_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch2/batch2_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L3[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch3/batch3_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch3/batch3_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L4[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch4/batch4_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch4/batch4_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L5[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch5/batch5_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch5/batch5_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L6[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch6/batch6_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch6/batch6_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L7[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch7/batch7_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch7/batch7_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L8[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch8/batch8_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch8/batch8_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L9[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch9/batch9_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch9/batch9_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I
    elif all(L10[i,:]==L[i,:]):
        name_tem='/WORK/bnu_kxia_1/wdwang/batch10/batch10_%i.npz'%(i)
        data_tem=np.load(name_tem)
        history=data_tem['history'];
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i.npz'%(i)
        np.savez(name_tem,history=history) #save history
        name_tem='/WORK/bnu_kxia_1/wdwang/batch10/batch10_%i_I.npz'%(i)
        data_tem=np.load(name_tem)
        I=data_tem['I'];k=data_tem['k']
        name_tem='/WORK/bnu_kxia_1/wdwang/batch0/batch0_%i_I.npz'%(i)
        np.savez(name_tem,I=I,k=k) #save I



        
        
        
        
        
        
        
        
        
        
        
        
        
