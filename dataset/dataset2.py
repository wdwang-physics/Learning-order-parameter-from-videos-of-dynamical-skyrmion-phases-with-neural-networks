#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
plt.switch_backend('Agg')
####
def sketch_and_label(path,num,NUM_array,m):
    name_tem='./%s/%i-%i.npz'%(path,m,num)
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
        name_tem1='./%s_dataset'%(path)
        if os.path.exists(name_tem1)==0:
           os.mkdir(name_tem1)
        name_tem='./%s/%i-%i_fig%i.png'%(name_tem1,m,num,np.int(index[0]))
        plt.savefig(name_tem)
        plt.close()

####
#main
NUM_array=range(0,100,10)
n1=4000;n2=4000;n3=4000;n4=4000;
path1='MC';path2='ML';
path3='PC';path4='PG';
path=path1;m=1;
for i in range(n1):
    sketch_and_label(path,i,NUM_array,m)

path=path2;m=2;
for i in range(n2):
    sketch_and_label(path,i,NUM_array,m)
    
path=path3;m=3;
for i in range(n3):
    sketch_and_label(path,i,NUM_array,m)

path=path4;m=4;
for i in range(n4):
    sketch_and_label(path,i,NUM_array,m)
