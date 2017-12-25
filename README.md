# Anime Face Classifier

KerasとAnime Face Datasetを使用してアニメキャラ分類器を作成します。

# 準備

animeface-character-datasetをダウンロードし、predict.pyと同じフォルダに置いて下さい。

http://www.nurs.or.jp/~nagadomi/animeface-character-dataset/README.html

# データセット作成

以下のコマンドでtrainフォルダとvalidationフォルダを作成します。

`perl separate.pl`

# 学習

以下のコマンドで学習します。

`python train.py`

学習済みモデルはanimeface.hdf5に格納されます。

# 推論

以下のコマンドで推論します。

`python predict.py`

# 認識

lbpcascade_animeface.xmlをダウンロードし、recognize.pyと同じフォルダに置いて下さい。

https://github.com/nagadomi/lbpcascade_animeface

OpenCVで顔を検出した後、CNNでラベルを表示します。

`python recognize.py sample.png`

# 認識精度

Mac Pro 2013で2日程度で学習が完了します。

32x32を入力する3段の浅いモデルで、認識精度は70%程度です。

loss: 0.6173 - acc: 0.8140 - val_loss: 1.2487 - val_acc: 0.7019

# 謝辞

スクリプトは以下のサイトを参考にさせて頂きました。

少ない画像から画像分類を学習させる方法
https://spjai.com/keras-fine-tuning/
