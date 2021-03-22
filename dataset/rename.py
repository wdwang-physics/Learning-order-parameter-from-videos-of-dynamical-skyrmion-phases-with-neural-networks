#!/HOME/bnu_kxia_1/program/Anaconda2-gcc4.4.7/bin/python
import sys
import numpy as np
import shutil,os
path1='/WORK/bnu_kxia_1/wdwang/MC';path2='/WORK/bnu_kxia_1/wdwang/ML';
path3='/WORK/bnu_kxia_1/wdwang/PC';path4='/WORK/bnu_kxia_1/wdwang/PG';
count =0
path=path1
filelist = os.listdir(path) 
for file in filelist: 
    Olddir = os.path.join(path,file)
    filename = os.path.splitext(file)[0] 
    filetop = "%i-"%(1)
    filetype = ".npz"
    Newdir = os.path.join(path,filetop+str(count)+filetype)
    os.rename(Olddir,Newdir) 
    count += 1

count =0
path=path2
filelist = os.listdir(path) 
for file in filelist: 
    Olddir = os.path.join(path,file)
    filename = os.path.splitext(file)[0] 
    filetop = "%i-"%(2)
    filetype = ".npz"
    Newdir = os.path.join(path,filetop+str(count)+filetype)
    os.rename(Olddir,Newdir) 
    count += 1

count =0
path=path3
filelist = os.listdir(path) 
for file in filelist: 
    Olddir = os.path.join(path,file)
    filename = os.path.splitext(file)[0] 
    filetop = "%i-"%(3)
    filetype = ".npz"
    Newdir = os.path.join(path,filetop+str(count)+filetype)
    os.rename(Olddir,Newdir) 
    count += 1

count =0
path=path4
filelist = os.listdir(path) 
for file in filelist: 
    Olddir = os.path.join(path,file)
    filename = os.path.splitext(file)[0] 
    filetop = "%i-"%(4)
    filetype = ".npz"
    Newdir = os.path.join(path,filetop+str(count)+filetype)
    os.rename(Olddir,Newdir) 
    count += 1
