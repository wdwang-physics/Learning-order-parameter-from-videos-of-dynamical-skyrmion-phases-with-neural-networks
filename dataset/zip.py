#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import shutil,os
ruler_speed=10**(-4)
ruler_std=0.3
MC=0;ML=0;PC=0;PG=0
path1='/WORK/bnu_kxia_1/wdwang/four_phases/MC';path2='/WORK/bnu_kxia_1/wdwang/four_phases/ML';
path3='/WORK/bnu_kxia_1/wdwang/four_phases/PC';path4='/WORK/bnu_kxia_1/wdwang/four_phases/PG';
pathk1='/WORK/bnu_kxia_1/wdwang/MC';pathk2='/WORK/bnu_kxia_1/wdwang/ML';
pathk3='/WORK/bnu_kxia_1/wdwang/PC';pathk4='/WORK/bnu_kxia_1/wdwang/PG';
if os.path.exists(path1)==0:
   os.mkdir(path1);
if os.path.exists(path2)==0:
   os.mkdir(path2);
if os.path.exists(path3)==0:
   os.mkdir(path3);
if os.path.exists(path4)==0:
   os.mkdir(path4);

num=30 
path=pathk1;m=1;
for i in range(num):
    name_tem='%s/%i-%i.npz'%(path,m,i)
    shutil.copy(name_tem,path1);

path=pathk2;m=2;
for i in range(num):
    name_tem='%s/%i-%i.npz'%(path,m,i)
    shutil.copy(name_tem,path2);

path=pathk3;m=3;
for i in range(num):
    name_tem='%s/%i-%i.npz'%(path,m,i)
    shutil.copy(name_tem,path3);

path=pathk4;m=4;
for i in range(num):
    name_tem='%s/%i-%i.npz'%(path,m,i)
    shutil.copy(name_tem,path4);