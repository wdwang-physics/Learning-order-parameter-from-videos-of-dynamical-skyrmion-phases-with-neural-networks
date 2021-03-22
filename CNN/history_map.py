import numpy as np
import tensorflow as tf
import keras
from tensorflow.python.keras.models import load_model
import scipy.io as sio
import matplotlib.pyplot as plt
import sys
#load X data
import pickle
with open('trainHistoryDict.txt','rb') as file_pi:
    history=pickle.load(file_pi)
plt.plot(history['acc'])
plt.plot(history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('tcnn2-1.png')
plt.close()

plt.plot(history['loss'])
plt.plot(history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig('tcnn2-2.png')
plt.close()
##################




