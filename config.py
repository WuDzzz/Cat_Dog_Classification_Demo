import sys

# Config
BATCH_SIZE = 50
TRAIN_PATH = 'G:\dogs-vs-cats-redux-kernels-edition\\train'
VALID_PATH = 'G:\dogs-vs-cats-redux-kernels-edition\\test'
DATASET_PATH = 'G:\dogs-vs-cats-redux-kernels-edition'
EPOCH = 20
RECORD_EPOCH = 5
LR = 0.0001
NET = '16'
ONE_HOT = False
DEVICE = "kaggle"

# Dataset path for myself
if DEVICE == "my":
    if sys.platform.startswith('win'):
        TRAIN_PATH = 'G:\dogs-vs-cats-redux-kernels-edition\\train'
        VALID_PATH = 'G:\dogs-vs-cats-redux-kernels-edition\\test'
        DATASET_PATH = 'G:\dogs-vs-cats-redux-kernels-edition'
    elif sys.platform.startswith('linux'):
        TRAIN_PATH = '/home/danzer/PycharmProject/Dataset/dogs-vs-cats-redux-kernels-edition/train'
        VALID_PATH = '/home/danzer/PycharmProject/Dataset/dogs-vs-cats-redux-kernels-edition/test'
        DATASET_PATH = '/home/danzer/PycharmProject/Dataset/dogs-vs-cats-redux-kernels-edition'
elif DEVICE == "kaggle":
    TRAIN_PATH = './cat_dog_classification/train'
    VALID_PATH = './cat_dog_classification/test'
    DATASET_PATH = './cat_dog_classification'
elif DEVICE == "colab":
    pass