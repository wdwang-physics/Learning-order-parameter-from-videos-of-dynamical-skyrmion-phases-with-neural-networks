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
    #L =label(m)
    for i in NUM_array:
        Sky=history[i,:,:]
        x=Sky[:,0];y=Sky[:,1]##导入数据
        width=360;height=360##设置尺寸
		##数据画图及去白边
        fig=plt.figure(1,facecolor=None, edgecolor=None, frameon=False)
        fig.set_size_inches(width/100.0,height/100.0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace =0, wspace =0)
        plt.scatter(x,y,cmap='gray')#数据画图
        plt.margins(0,0)
        plt.axis('off')
        index=np.argwhere(np.array(NUM_array)==i)
        name_tem='%s/%i-%i_fig%i.png'%(path,m,num,np.int(index[0]))
        plt.savefig(name_tem)##图片保存
        #name_tem='%s/%i_fig%i.npz'%(path,num,np.int(index[0]))
        #np.savez(name_tem,L=L)
        #np.savetxt(name_tem1,L,fmt="%d", delimiter=",")
        plt.close()

####
#main
NUM_array=[97,98];
n1=1000;n2=600;n3=1000;n4=1400;
path1='/WORK/bnu_kxia_1/wdwang/MC';path2='/WORK/bnu_kxia_1/wdwang/ML';
path3='/WORK/bnu_kxia_1/wdwang/PC';path4='/WORK/bnu_kxia_1/wdwang/PG';
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



               
