#!/WORK/app/anaconda/4.2.0/bin/python
import numpy as np
import mpmath as mp
import time as tm
from numba import jit
import sys
import scipy.io as sio
####
@jit('Tuple((float64[:],float64[:],float64[:],float64[:,:,:,:],float64[:,:]))(float64[:],float64[:])',nopython=True)
def initialize(F0,Epsilon):
    #parament:F0,Epsilon;size(F0)=[n,4]:J_x0,J_y0,J_d0,F_s0;size(Epsilon)=[n,2]:Epsilon_d,Epsilon_s;
    #unit of force and current
    f0=1e3;j0=1e3
    #Space
    L_0=36;J_x=F0[0]*j0;J_y=F0[1]*j0
    Space=np.array([L_0,J_x,J_y])
    #Pin_constant
    N_p=np.floor(0.3*np.power(Space[0],2))
    D_p=0;J_d=F0[2]*f0;Epsilon_d=Epsilon[0]
    Pin_constant=np.array([N_p,D_p,J_d,Epsilon_d])
    #Sky_constant
    N_s=np.floor(0.1*np.power(Space[0],2))
    D_s=0;F_ss=F0[3]*f0;Epsilon_s=Epsilon[1];Alpha_md=9.962
    Sky_constant=np.array([N_s,D_s,F_ss,Epsilon_s,Alpha_md])
    #Pin_plus
    Range=np.array([0,np.int(Space[0])])
    Pin=Range[0]+np.random.rand(np.int(Pin_constant[0]),2)*(Range[1]-Range[0])
    Pin_plus=np.zeros((3,3,np.int(Pin_constant[0]),2))
    for i in range(3):
        for j in range(3):
            Pin_plus[i,j,:,:]=Pin
            Pin_plus[i,j,:,0]=Pin_plus[i,j,:,0]+np.array(i-1)*Space[0]
            Pin_plus[i,j,:,1]=Pin_plus[i,j,:,1]+np.array(j-1)*Space[0]
    #Sky
    Sky=Range[0]+np.random.rand(np.int(Sky_constant[0]),2)*(Range[1]-Range[0])
    #print('initialization is done')
    return Space,Pin_constant,Sky_constant,Pin_plus,Sky
####
@jit('Tuple((float64[:,:],float64[:,:]))(float64[:,:,:,:])',nopython=True)
def index(r_plus):
    distance_plus=np.power((np.power(r_plus[:,:,:,0],2)+np.power(r_plus[:,:,:,1],2)),0.5);
    #print(numba.typeof(distance_plus))
    distance=np.zeros((r_plus.shape[2],1))
    direction=np.zeros((r_plus.shape[2],2))
    ri=np.ones(9)
    for i in range(r_plus.shape[2]):
        for j in range(3):
            ri[j*3:j*3+3]=distance_plus[j,:,i]
        index_tem=np.argmin(ri)
        index_tem1=np.int(index_tem/3);index_tem2=np.mod(index_tem,3)
        distance[i]=distance_plus[index_tem1,index_tem2,i];
        direction[i,:]=r_plus[index_tem1,index_tem2,i,:]/distance[i];
    return distance,direction
####
@jit('float64[:,:](float64[:,:])',nopython=True)
def mybesselk(x):
    term1=np.zeros((x.shape[0],1));
    term2=1/x;
    term3=np.zeros((x.shape[0],1));
    #serias expansion
    argu1=np.array([0.500000000000000,0.0625000000000000,0.00260416666666667,5.42534722222222e-05,6.78168402777778e-07,5.65140335648148e-09,3.36393056933422e-11,1.50175471845277e-13,5.21442610573880e-16,1.44845169603856e-18,3.29193567281490e-21])
    argu3=np.array([0.0386078324507660,-0.0420490209436540,-0.00283711198376300,-7.49304290598850e-05,-1.08921825387356e-06,-1.01129093976346e-08,-6.54019722956043e-11,-3.12085877013226e-13,-1.14519071448867e-15,-3.33397744149483e-18,-7.89145168125694e-21])
    for i in range(11):
        term1=term1+np.log(x/2)*x**(2*i+1)*argu1[i]
        term3=term3+x**(2*i+1)*argu3[i]
    y=term1+term2+term3
    for i in range(x.shape[0]):
        if x[i,0]>7:
           y[i,0]=0
    return y
####
@jit('float64[:,:](float64[:],float64[:],float64[:],float64[:,:,:,:],float64[:,:],float64)',nopython=True)
def interaction(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt):
    #Sky_plus
    Sky_plus=np.zeros((3,3,np.int(Sky_constant[0]),2));
    Sky_plus_tem=np.zeros((3,3,np.int(Sky_constant[0]-1),2));
    for i in [0,1,2]:
        for j in [0,1,2]:
            Sky_plus[i,j,:,:]=Sky
            Sky_plus[i,j,:,0]=Sky_plus[i,j,:,0]+np.array(i-1)*Space[0]
            Sky_plus[i,j,:,1]=Sky_plus[i,j,:,1]+np.array(j-1)*Space[0]
    #F_sp
    F_sp=np.zeros((np.int(Sky_constant[0]),2));
    F_spi=np.zeros((np.int(Pin_constant[0]),2))
    for i in range(np.int(Sky_constant[0])):
        Skyi=Sky_plus[1,1,i,:];
        r_plus=Pin_plus-Skyi;
        distance,direction=index(r_plus)
        F_spi=Pin_constant[2]*np.exp(-1*distance/Pin_constant[3])*direction
        F_sp[i,:]=F_spi.sum(0); 
        #print("F_sp %d is done"%i)
    #F_ss
    F_ss=np.zeros((np.int(Sky_constant[0]),2))
    F_ssi=np.zeros((np.int(Sky_constant[0])-1,2))
    #besselk_array=np.frompyfunc(mp.besselk,2,1)
    for i in range(np.int(Sky_constant[0])):
        Skyi=Sky_plus[1,1,i,:]
        Sky_plus_tem[:,:,0:i,:]=Sky_plus[:,:,0:i,:]
        Sky_plus_tem[:,:,i:,:]=Sky_plus[:,:,i+1:,:]
        r_plus=-Sky_plus_tem+Skyi;
        distance,direction=index(r_plus)
        F_ssi=Sky_constant[2]*mybesselk(1*distance/Sky_constant[3])*direction;
        #F_ssi=Sky_constant[2]*besselk_array(1,distance/Sky_constant[3])*direction;
        F_ss[i,:]=F_ssi.sum(0);
        #print("F_ss %d is done"%i) 
#F_D
    F_D=np.array([Space[2],-Space[1]])
#F
    F=F_ss+F_sp+F_D;
    Alpha=Sky_constant[4]
    Alpha2=np.power(Alpha,2);
    V_y=(np.sqrt(1+Alpha2)*F[:,0]+Alpha*np.sqrt(1+Alpha2)*F[:,1])/np.square(Alpha2-1);
    V_x=(np.sqrt(1+Alpha2)*F[:,1]+Alpha*np.sqrt(1+Alpha2)*F[:,0])/np.square(Alpha2-1);
    dSky=np.zeros((np.int(Sky_constant[0]),2))
    dSky[:,0]=dt*V_x;dSky[:,1]=dt*V_y;
    return dSky
####
@jit('float64[:,:](float64[:],float64[:],float64[:],float64[:,:,:,:],float64[:,:],float64)',nopython=True)
def runge(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt):
    dSky1=interaction(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt);
    dSky2=interaction(Space,Pin_constant,Sky_constant,Pin_plus,Sky+0.5*dSky1,dt);
    return dSky2
####
##@jit('Tuple((float64[:,:,:],float64[:]))(float64[:],float64[:],float64[:],float64[:,:,:,:],float64[:,:],float64,float64)',nopython=True)
def evolve(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt,time):
    #print('evolution is begun')
    #for velocity_mean num
    num=100
    history=np.zeros((np.int(time),Sky.shape[0],Sky.shape[1]));
    velocity=np.ones((np.int(num),Sky.shape[0],Sky.shape[1]));
    for i in range(time):
        dSky=runge(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt);
        Sky=Sky+dSky;
        Sky=np.mod(Sky,Space[0]);
        history[i,:,:]=Sky;
        if i>time-num-1:
           velocity[np.int(i-time+num),:,:]=dSky
        #print('evolution for time %i is done'%i)
    velocity_mean=np.sum(velocity,0)/(num)
    velocity_mean=np.sum(velocity_mean,0)/(Sky.shape[0])
    return history,velocity_mean
####
@jit('Tuple((float64[:,:],float64[:,:],float64[:,:]))(float64[:,:,:],float64[:],int64)',nopython=True)
def classify(history,velocity_mean,num):
    L_0=36
    inter=0.1;
    Sky=history[num,:,:]
    Sky_plus=np.zeros((3,3,history.shape[1],2));
    for i in [0,1,2]:
        for j in [0,1,2]:
            Sky_plus[i,j,:,:]=Sky
            Sky_plus[i,j,:,0]=Sky_plus[i,j,:,0]+np.array(i-1)*L_0
            Sky_plus[i,j,:,1]=Sky_plus[i,j,:,1]+np.array(j-1)*L_0
    radius_sta=np.zeros((history.shape[1]*(history.shape[1]-1),2));
    distance_sta=np.zeros((history.shape[1]*(history.shape[1]-1),1));
    for i in range(history.shape[1]):
        Skyi=Sky_plus[1,1,i,:]
        Sky_plus_tem=np.zeros((3,3,(history.shape[1]-1),2))       
        Sky_plus_tem[:,:,0:i,:]=Sky_plus[:,:,0:i,:]
        Sky_plus_tem[:,:,i:,:]=Sky_plus[:,:,i+1:,:]
        r_plus=-Sky_plus_tem+Skyi
        distance,direction=index(r_plus)
        r=direction*distance
        for j in range(history.shape[1]-1):
            distance_sta[j+i*(history.shape[1]-1),:]=distance[j,:]
            radius_sta[j+i*(history.shape[1]-1),:]=r[j,:]
    X=np.arange(0,L_0/2,inter);Y=np.arange(0,L_0/2,inter)
    P=np.ones((X.shape[0],Y.shape[0]));
    D=np.ones((X.shape[0],1))
    for i in range(X.shape[0]):
        index_D=np.where((np.abs(distance_sta[:,0]-X[i])<(inter/2)))
        D[i,0]=np.sum(1/distance_sta[index_D[0],:]/np.pi/2)
        for j in range(Y.shape[0]):
            x_tem=np.abs(radius_sta[:,0]-X[i]);
            y_tem=np.abs(radius_sta[:,1]-Y[j]);
            r_tem=(x_tem**2+y_tem**2)**0.5
            index_P=np.where(r_tem<(inter/2))
            P[i,j]=index_P[0].shape[0];
    I=np.ones((1,3))
    I[0,0]=np.std(D[100:]);I[0,1:]=velocity_mean
    #I means the type of the motion,1=PG,2=PC,3=MG,ML,4=MC
    #m=np.max(P);n=np.min(P)
    #p=m-n;I=0
    #if p>30:
       #I=I+2
    #else:
       #I=I+1
    #Sky_i=history[num,:,:];Sky_k=history[num+1,:,:]
    #dSky=Sky_k-Sky_i;
    #v=(dSky[:,0]**2+dSky[:,1]**2)**0.5;
    #V=np.sum(v)/history.shape[1]
    #if V>(L_0/8000):
       #I=I+2
    #else:
       #I=I+0    
    return P,D,I
####
#main
#parament:F0,Epsilon,dt;size(F0)=[n,4]:J_x0,J_y0,J_d0,F_s0;size(Epsilon)=[n,2]:Epsilon_d,Epsilon_s;
J_x=10**np.linspace(-4.5,0,30)
J_d=10**np.linspace(-3,0,28)
num=(J_x.shape[0]*J_d.shape[0])
F0=np.zeros((num,4));Epsilon=np.zeros((num,2))
Epsilon[:,:]=[0.3,4];F0[:,:]=[0.0001,0,0.1,1];
for i in range(J_x.shape[0]):
    for j in range(J_d.shape[0]):
        F0[(i*J_d.shape[0]+j),0]=J_x[i]
        F0[(i*J_d.shape[0]+j),2]=J_d[j]
#save the Parameters
name='./%s/%s_Para'%(sys.argv[3],sys.argv[3])
name1='./%s_mat/%s_Para'%(sys.argv[3],sys.argv[3])
if np.int(sys.argv[1])==0:
   np.savez(name,F0=F0,Epsilon=Epsilon)
   #sio.savemat(name1,{'F0':F0,'Epsilon':Epsilon})
time=4000;dt=0.01;num=3950;cut=range(0,4000,10);
#limit=850
####
MINES=np.array([1])
ALL=np.int(sys.argv[2]);NUM=np.int(sys.argv[1])
inter=np.int(F0.shape[0]/(ALL-MINES.shape[0]))
sur=np.mod(F0.shape[0],ALL-MINES.shape[0])
CODES=np.arange(ALL)
for var1 in CODES:
    for var2 in MINES:
        if var1>var2:
           CODES[var1]=CODES[var1]-1
val=np.argwhere(MINES==NUM)
if CODES[NUM]<sur:
   inter=inter+1
   for i in range(inter): 
       #if (val.shape[0]>0):
          #tm.sleep(limit)
          #continue
       tt1=tm.time()
       name='./%s/%s_%i'%(sys.argv[3],sys.argv[3],CODES[NUM]*inter+i)
       name1='./%s_mat/%s_%i'%(sys.argv[3],sys.argv[3],CODES[NUM]*inter+i) 
       Space,Pin_constant,Sky_constant,Pin_plus,Sky=initialize(F0[CODES[NUM]*inter+i,:],Epsilon[CODES[NUM]*inter+i,:])
       history,velocity_mean=evolve(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt,time)
       P,D,I=classify(history,velocity_mean,num)
       #sio.savemat(name1,{'history':history,'velocity_mean':velocity_mean})
       history=history[cut]
       np.savez(name,history=history,velocity_mean=velocity_mean)
       name='./%s/%s_%i_I'%(sys.argv[3],sys.argv[3],CODES[NUM]*inter+i)
       np.savez(name,I=I)
       #sio.savemat(name, {'P':P,'D':D,'I':I})
       tt2=tm.time();
       #tm.sleep(np.abs(limit-(tt2-tt1)))
       #tt2=tm.time();
       print('the time used equals %f'%(tt2-tt1))

else:
   for i in range(inter):
       #if (val.shape[0]>0):
          #tm.sleep(limit)
          #continue
       tt1=tm.time()
       name='./%s/%s_%i'%(sys.argv[3],sys.argv[3],(sur+inter*CODES[NUM]+i))
       name1='./%s_mat/%s_%i'%(sys.argv[3],sys.argv[3],CODES[NUM]*inter+i)
       Space,Pin_constant,Sky_constant,Pin_plus,Sky=initialize(F0[sur+CODES[NUM]*inter+i,:],Epsilon[sur+CODES[NUM]*inter+i,:])
       history,velocity_mean=evolve(Space,Pin_constant,Sky_constant,Pin_plus,Sky,dt,time)
       P,D,I=classify(history,velocity_mean,num)
       history=history[cut]
       #sio.savemat(name1, {'history':history,'velocity_mean':velocity_mean})
       np.savez(name,history=history,velocity_mean=velocity_mean)
       name='./%s/%s_%i_I'%(sys.argv[3],sys.argv[3],(sur+inter*CODES[NUM]+i))
       np.savez(name,I=I)
       #sio.savemat(name, {'I':I})
       tt2=tm.time();
       #tm.sleep(np.abs(limit-(tt2-tt1)))
       #tt2=tm.time();
       print('the time used equals %f'%(tt2-tt1))
   #if sur>0:
      #tm.sleep(limit)
