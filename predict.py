#Predict anime face

import os
import sys
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

#MODEL_HDF5='animeface_vgg16.hdf5'
MODEL_HDF5='animeface_small_cnn.hdf5'

if len(sys.argv) != 2:
    #print("usage: python predict.py [filename]")
    #sys.exit(1)
	filename = "images/miku_face.jpg"
else:
	filename = sys.argv[1]

print('input:', filename)

if(MODEL_HDF5 == 'animeface_vgg16.hdf5'):
	IMAGE_SIZE = 224
elif(MODEL_HDF5 == 'animeface_small_cnn.hdf5'):
	IMAGE_SIZE = 32
else:
	raise Exception('invalid model name')

input_tensor = Input(shape=(IMAGE_SIZE, IMAGE_SIZE, 3))

model = load_model(MODEL_HDF5)
model.summary()

img = image.load_img(filename, target_size=(IMAGE_SIZE, IMAGE_SIZE))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

x = x / 255.0

print(x)
print(x.shape)

pred = model.predict(x)[0]
print(pred)

prob = np.max(pred)
cls = pred.argmax()

lines=open('animeface_tag.txt').readlines()
print prob, cls, lines[cls]
