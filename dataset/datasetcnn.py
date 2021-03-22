#!/WORK/app/anaconda/5.3.1/bin/python
import numpy as np
import matplotlib.pyplot as plt
import sys
import shutil,os
plt.switch_backend('Agg')
####
def label(name,num):
    name_tem='./%s/%s_%i_I.npz'%(name,name,num)
    data_tem=np.load(name_tem)
    I=data_tem['I'];std=I[0,0]
    L=np.ones((1,2))
    if (std<0.4):
       L=np.array([1,0])  #amorphous
    else:
       L=np.array([0,1])  #crystal
    return L
####
def sketch_and_label(name,num,NUM_array):
    name_tem='./%s/%s_%i.npz'%(name,name,num)
    data_tem=np.load(name_tem)
    history=data_tem['history']
    L=label(name,num)
    name_tem1='./%s_dataset/%s_%i_fig.npz'%(name,name,num)
    np.savez(name_tem1,L=L)
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
        name_tem='./%s_dataset/%s_%i_fig%i.png'%(name,name,num,np.int(index[0]))
        plt.savefig(name_tem)
        plt.close()
####
#main
NUM_array=[98]
n=840
name_tem='./%s_dataset'%(sys.argv[1])
if os.path.exists(name_tem)==0:
   os.mkdir(name_tem)
for i in range(n):
    name_tem='./%s/%s_%i.npz'%(sys.argv[1],sys.argv[1],i)
    if os.path.exists(name_tem)==0:
       name_H='/WORK/bnu_kxia_1/wdwang/%s/%s_%i.npz'%(sys.argv[1],sys.argv[1],i-1)
       name_H1='/WORK/bnu_kxia_1/wdwang/%s/%s_%i_I.npz'%(sys.argv[1],sys.argv[1],i-1)
       path='/WORK/bnu_kxia_1/wdwang'
       shutil.copy(name_H,path);shutil.copy(name_H1,path);
       name_H='/WORK/bnu_kxia_1/wdwang/%s_%i.npz'%(sys.argv[1],i-1)
       name_H1='/WORK/bnu_kxia_1/wdwang/%s_%i_I.npz'%(sys.argv[1],i-1)
       name_H2='/WORK/bnu_kxia_1/wdwang/%s_%i.npz'%(sys.argv[1],i)
       name_H3='/WORK/bnu_kxia_1/wdwang/%s_%i_I.npz'%(sys.argv[1],i)
       os.rename(name_H,name_H2);os.rename(name_H1,name_H3)
       path='/WORK/bnu_kxia_1/wdwang/%s'%(sys.argv[1])
       shutil.move(name_H2,path);shutil.move(name_H3,path);
    sketch_and_label(sys.argv[1],i,NUM_array)
