#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
plt.switch_backend('Agg')
####
def label(m):
    if m==1 or m==2:
       L=np.array([0,1])  #moving
    else:
       L=np.array([1,0])     #pinning
    return L
####
def sketch_and_label(path,num,NUM_array,m):
    name_tem='%s/%i-%i.npz'%(path,m,num)
    data_tem=np.load(name_tem)
    history=data_tem['history']
    L =label(m)
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
        name_tem='%s/%i-%i_fig%i.png'%(path,m,num,np.int(index[0]))
        plt.savefig(name_tem)
        #name_tem='%s/%i_fig%i.npz'%(path,num,np.int(index[0]))
        #np.savez(name_tem,L=L)
        #np.savetxt(name_tem1,L,fmt="%d", delimiter=",")
        plt.close()

####
#main
NUM_array=[25,26,27,28,29,30,31,32,33,34]
ALL=1450;
path1='/WORK/bnu_kxia_1/wdwang/MC';path2='/WORK/bnu_kxia_1/wdwang/ML';
path3='/WORK/bnu_kxia_1/wdwang/PC';path4='/WORK/bnu_kxia_1/wdwang/PG';
path=path4;m=4;
for i in range(ALL):
    sketch_and_label(path,i,NUM_array,m)
                   
