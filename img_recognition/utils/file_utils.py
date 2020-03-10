from os import listdir, remove
from os.path import isfile, join
from PIL import Image
import numpy as np
import os
import cv2

def imresize(img,sz):
  return array(img.resize(sz))

def read_paths(path):
    elems = {}
    for file_name in listdir(path):
        file_path = join(path, file_name)
        if not isfile(file_path):
            elems[file_name] = read_paths(file_path)

        try:
            img = np.array(Image.open(file_path))
            name = os.path.basename(path)
            if not name in elems:
                elems[name] = [img]
            else:
                elems[name].append(img)
        except IOError:
            pass

    return elems

def read_paths_2(path):
    elems = {}
    sz = (150, 150)
    limit = 0
    for file_name in listdir(path):
        file_path = join(path, file_name)
        if limit > 100:
            break
        elif not isfile(file_path):
            elems[file_name] = read_paths(file_path)

        try:
            # using convert to translate to gray scale
            img = Image.open(file_path).convert('L')
            name = os.path.basename(path)
            if not name in elems:
                elems[name] = [array(img.resize(sz))]
            else:
                elems[name].append(array(img.resize(sz)))
        except IOError:
            pass

        limit += 1

    return elems
