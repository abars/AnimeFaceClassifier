# Anime Face Classifier using Keras

Classification Japanese Anime Character.

![Miku Detected](https://github.com/abars/AnimeFaceClassifier/blob/master/pretrain/result.png "Miku Detected")

Hatsune Miku / Crypton Future Media inc. / CC BY-NC

Detectable Character List : <https://github.com/abars/AnimeFaceClassifier/blob/master/animeface_tag.txt>

# Requirements

Keras2

Python 2.7

OpenCV3

Plaidml (Train)

# Pretrained model

Download pretrained model.


Recommended : <http://www.abars.biz/keras/animeface_small_cnn.hdf5> (946MB)

Small CNN model. Train 2days using Mac Pro 2013.

loss: 0.6173 - acc: 0.8140 - val_loss: 1.2487 - val_acc: 0.7019


Experimental : <http://www.abars.biz/keras/animeface_vgg16.hdf5> (93MB)

VGG16 fine tuning model. Train 3days using Mac Pro 2013.

loss: 0.0557 - acc: 0.9836 - val_loss: 1.0058 - val_acc: 0.8178

# Predict

Predict from face image.

`python predict.py images/miku_face.jpg`

# Recognize

Recognize from several image.

`python recognize.py images/miku.png`

# Download dataset

Download animeface-character-dataset and put in the same folder.

http://www.nurs.or.jp/~nagadomi/animeface-character-dataset/README.html

Create train folder and validation folder.

`perl separate.pl`

# Train

`python train.py`

Output is animeface.hdf5.

# Acknowledgement

https://github.com/nagadomi/lbpcascade_animeface

https://spjai.com/keras-fine-tuning/
