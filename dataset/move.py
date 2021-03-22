#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import shutil,os
ruler_speed=10**(-2.85)
ruler_std=0.4
MC=0;ML=0;PC=0;PG=0
path1='/WORK/bnu_kxia_1/wdwang/MC';path2='/WORK/bnu_kxia_1/wdwang/ML';
path3='/WORK/bnu_kxia_1/wdwang/PC';path4='/WORK/bnu_kxia_1/wdwang/PG';
if os.path.exists(path1)==0:
   os.mkdir(path1);
if os.path.exists(path2)==0:
   os.mkdir(path2);
if os.path.exists(path3)==0:
   os.mkdir(path3);
if os.path.exists(path4)==0:
   os.mkdir(path4);
num=840 

name='%s'%(sys.argv[1])
for i in range(num):
    name_tem='./%s/%s_%i_I.npz'%(name,name,i)
    name_H='./%s/%s_%i.npz'%(name,name,i)
    if os.path.exists(name_tem)==0:
       continue
    data_tem=np.load(name_tem)
    I=data_tem['I']
    speed=(I[:,1]**2+I[:,2]**2)**0.5
    if (I[:,0]<ruler_std) and (speed<ruler_speed):
       PG+=1
       shutil.copy(name_H,path4);
    elif (I[:,0]>ruler_std) and (speed<ruler_speed):
       PC+=1
       shutil.copy(name_H,path3);
    elif (I[:,0]<ruler_std) and (speed>ruler_speed):
       ML+=1
       shutil.copy(name_H,path2);
    elif (I[:,0]>ruler_std) and (speed>ruler_speed):
       MC+=1
       shutil.copy(name_H,path1);
