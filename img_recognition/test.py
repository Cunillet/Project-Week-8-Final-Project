from os import listdir, remove
from os.path import isfile, join
from PIL import Image
import numpy as np
import pandas as pd
import os
import cv2

def read_folders(path):
    elems = {}
    for file_name in listdir(path):
        file_path = join(path, file_name)
        if not isfile(file_path):
            print(f'... {file_name} ...')
            elems[file_name] = read_paths_cv2(file_path)
    return elems

def read_paths_cv2(path):
    new_size = (150, 150)
    animals = []
    limit = 0
    for file_name in listdir(path):
        file_path = join(path, file_name)
        if limit > 10:
            break
        if not isfile(file_path):
            print(f'WARN - ignoring {file_name}')
            continue

        try:
            img = img = cv2.imread(file_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_resized = cv2.resize(gray, new_size, interpolation=cv2.INTER_AREA)
            animals.append(gray_resized)
        except:
            print(f'ERROR - {file_path}')
        limit += 1

    return animals
    
print('start reading imgs....')
elems = read_paths_cv2('img_recognition/data/img/cat')
print('end reading imgs')
print('data transformed!')
#cv2.imshow("image", elems[5])
#cv2.waitKey()
#print(elems[5].shape)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(150, 150)),
    keras.layers.Dense(22500, activation='relu'),
    keras.layers.Dense(11250, activation='relu'),
    keras.layers.Dense(5625, activation='relu'),
    keras.layers.Dense(2812, activation='relu'),
    keras.layers.Dense(1406, activation='relu'),
    keras.layers.Dense(700, activation='relu'),
    keras.layers.Dense(350, activation='relu'),
    keras.layers.Dense(175, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
