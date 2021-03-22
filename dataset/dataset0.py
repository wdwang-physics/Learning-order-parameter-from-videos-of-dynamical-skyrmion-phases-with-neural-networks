#!/home/wdwang/anaconda3/bin/python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
plt.switch_backend('Agg')
####
def label(name,num,i):
    name_tem='./%s/%s_%i_I.npz'%(name,name,num)
    data_tem=np.load(name_tem)
    k=data_tem['k'];I=data_tem['I'];std=I[:,0];
    L=np.ones((1,2))
    if (std<0.4):
       L=np.array([1,0]) #amorphous
    else:
       L=np.array([0,1])
    return L
####
def sketch_and_label(name,num,NUM_array):
    name_tem='./%s/%s_%i.npz'%(name,name,num)
    data_tem=np.load(name_tem)
    history=data_tem['history']
    for i in NUM_array:
        Sky=history[i,:,:]
        x=Sky[:,0];y=Sky[:,1]
        width=360;height=360
        fig=plt.figure(1,facecolor=None, edgecolor=None, frameon=False)
        fig.set_size_inches(width/100.0,height/100.0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace =0, wspace =0)
        plt.scatter(x,y,cmap='gray')
        plt.margins(0,0)
        plt.axis('off')
        index=np.argwhere(np.array(NUM_array)==i)
        name_tem='./%s_dataset1/%s_%i_fig%i.png'%(name,name,num,np.int(index[0]))
        plt.savefig(name_tem)
        L=label(name,num,i)
        name_tem='./%s_dataset1/%s_%i_fig%i.npz'%(name,name,num,np.int(index[0]))
        np.savez(name_tem,L=L)
        plt.close()

####
#main
NUM_array=[99]
name_tem='/WORK/bnu_kxia_1/wdwang/batch1/batch1_Para.npz'
data_tem=np.load(name_tem)
F0=data_tem['F0'];ALL=F0.shape[0];
name_tem='./%s_dataset1'%(sys.argv[1])
if os.path.exists(name_tem)==0:
   os.mkdir(name_tem)
for i in range(F0.shape[0]):
    name_tem='./%s/%s_%i.npz'%(sys.argv[1],sys.argv[1],i)
    if os.path.exists(name_tem)==0:
       continue
    sketch_and_label(sys.argv[1],i,NUM_array)
