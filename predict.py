#Predict anime face

import os
import sys
from keras.applications.vgg16 import VGG16
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

if len(sys.argv) != 2:
    #print("usage: python predict.py [filename]")
    #sys.exit(1)
	filename = "animeface-character-dataset/thumb/000_hatsune_miku/face_93_104_36.png"
else:
	filename = sys.argv[1]

print('input:', filename)

IMAGE_SIZE = 32
input_tensor = Input(shape=(IMAGE_SIZE, IMAGE_SIZE, 3))

model = load_model('animeface.hdf5')
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

lines=open('animeface-character-dataset/tools/tag.txt').readlines()
print prob, cls, lines[cls]
