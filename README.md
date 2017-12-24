# Anime Face Classifier

KerasとAnime Face Datasetを使用してアニメキャラ分類器を作成します。

# 準備

animeface-character-datasetをダウンロードし、predict.pyと同じフォルダに置いて下さい。

http://www.nurs.or.jp/~nagadomi/animeface-character-dataset/README.html

# データセット作成

以下のコマンドでtrainフォルダとvalidationフォルダを作成します。

`perl sperate.pl`

# 学習

以下のコマンドで学習します。

`python train.py`

学習済みモデルはanimeface.hdf5に格納されます。

# 推論

以下のコマンドで推論します。

`python predict.py`

# 謝辞

スクリプトは以下のサイトを参考にさせて頂きました。

少ない画像から画像分類を学習させる方法
https://spjai.com/keras-fine-tuning/
