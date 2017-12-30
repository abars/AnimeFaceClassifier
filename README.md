# Anime Face Classifier

Classification Japanese Anime Character.

![Miku Detected](https://github.com/abars/AnimeFaceClassifier/blob/master/pretrain/result.png "Miku Detected")

Hatsune Miku / Crypton Future Media inc. / CC BY-NC

Detectable Character List : <https://github.com/abars/AnimeFaceClassifier/blob/master/animeface_tag.txt>

# Pretrained model

Download pretrained model and rename to animeface.hdf5.

<http://www.abars.biz/keras/animeface_small_cnn.hdf5> (946MB)

Small CNN model. Train 2days using Mac Pro 2013.

loss: 0.6173 - acc: 0.8140 - val_loss: 1.2487 - val_acc: 0.7019

TBD

VGG16 fine tuning model. Train 3days using Mac Pro 2013.

# Predict

Predict from face image.

`python predict.py face.png`

# Recognize

Recognize from several image.

`python recognize.py sample.png`

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
