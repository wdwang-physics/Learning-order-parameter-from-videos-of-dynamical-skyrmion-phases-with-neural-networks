import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense,Activation,Convolution2D,Flatten,MaxPooling2D,BatchNormalization,Dropout
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.callbacks import ModelCheckpoint,EarlyStopping
from keras.models import Model
from tensorflow.keras import backend as K
import sys
import os
from scipy import misc
from PIL import Image
import scipy.io as sio
plt.switch_backend('Agg')
from tensorflow.python.keras.models import load_model
def ImageToMatrix(filename):
    im = Image.open(filename)
    width,height = im.size
    data = im.getdata()
    data = np.matrix(data,dtype='float')/255.0
    new_data = np.reshape(data,(height,width))
    return new_data

def changeImagesize(input_dir,out_dir):
    size_m = 72;size_n = 72
    I = Image.open(input_dir)
    I_size = I.resize((size_m, size_n),Image.ANTIALIAS)
    L = I_size.convert('L')
    L.save(out_dir)
    return L
def changesizeandcolor(name):
    name_tem = './input/%s.jpg'%(name)
    name_tem1 = './output/%s.jpg'%(name)
    L = changeImagesize(name_tem, name_tem1)
    data = ImageToMatrix(name_tem1)
    return data

model=load_model('weights5best.h5')
name='%s'%(sys.argv[1])
input_image0=changesizeandcolor(name)
input_image=np.zeros((1,72,72,1));
input_image[0,:,:,0]=input_image0;
           
n=0;str='conv1'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(32):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.subplot(4, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

for i in range(5):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s1.png'%(name,n,str)
plt.savefig(name1, format='png', dpi=300)
plt.close()
plt.show()

for i in range(6):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s2.png'%(name,n,str)
plt.savefig(name1, format='png', dpi=300)
plt.close()
plt.show()

for i in range(10):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s3.png'%(name,n,str)
plt.savefig(name1, format='png', dpi=300)
plt.close()
plt.show()

for i in range(27):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s4.png'%(name,n,str)
plt.savefig(name1, format='png', dpi=300)
plt.close()
plt.show()

for i in range(30):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s5.png'%(name,n,str)
plt.savefig(name1, format='png', dpi=300)
plt.close()
plt.show()


f1=f1.reshape(36,36,32);
name_tem1='./output/%s_f1.mat'%(name)
sio.savemat(name_tem1, {'f1':f1})
f14=f1[:, :, 4];
name_tem1='./output/%s_f14.mat'%(name)
sio.savemat(name_tem1, {'f14':f14})
f15=f1[:, :, 5];
name_tem1='./output/%s_f15.mat'%(name)
sio.savemat(name_tem1, {'f15':f15})
f19=f1[:, :, 9];
name_tem1='./output/%s_f19.mat'%(name)
sio.savemat(name_tem1, {'f19':f19})
f126=f1[:, :, 26];
name_tem1='./output/%s_f126.mat'%(name)
sio.savemat(name_tem1, {'f126':f126})
f127=f1[:, :, 27];
name_tem1='./output/%s_f127.mat'%(name)
sio.savemat(name_tem1, {'f127':f127})
f129=f1[:, :, 29];
name_tem1='./output/%s_f129.mat'%(name)
sio.savemat(name_tem1, {'f129':f129})


for i in range(14):#[0,7]
    layer_1 = K.function([model.layers[0].input], [model.layers[i].output])
    f1 = layer_1([input_image])[0]
    print(f1.shape)
print('This is the end !')
n=1;str='batchnorm1'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(32):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.subplot(4, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=2;str='act1'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(32):
            show_img = f1[:, :, :, i]
            show_img.shape = [36, 36]
            plt.subplot(4, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=3;str='pool1'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(32):
            show_img = f1[:, :, :, i]
            show_img.shape = [18, 18]
            plt.subplot(4, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=4;str='conv2'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(64):
            show_img = f1[:, :, :, i]
            show_img.shape = [18, 18]
            plt.subplot(8, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=5;str='batchnorm2'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(64):
            show_img = f1[:, :, :, i]
            show_img.shape = [18, 18]
            plt.subplot(8, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=6;str='act2'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(64):
            show_img = f1[:, :, :, i]
            show_img.shape = [18, 18]
            plt.subplot(8, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=7;str='pool2'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
for i in range(64):
            show_img = f1[:, :, :, i]
            show_img.shape = [9, 9]
            plt.subplot(8, 8, i + 1)
            plt.imshow(show_img, cmap='gray')
            plt.axis('off')
name1='./output/%s%s_%s.jpg'%(name,n,str)
plt.savefig(name1, format='jpg', dpi=300)
plt.close()
plt.show()

n=13;str='softmax'
layer_1 = K.function([model.layers[0].input], [model.layers[n].output])
f1 = layer_1([input_image])[0]
print(f1)
