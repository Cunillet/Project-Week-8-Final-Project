from os import listdir, remove
from os.path import isfile, join
import json

def obtain_links(filepath):
    with open(filepath) as f:
        json_file = json.load(f)
        links = json_file[0]['product_link']
    #remove(filepath)
    return links

def read_paths(path):
    links = []
    for f in listdir(path):
        filepath = join(path, f)
        if not isfile(filepath):
            continue

        with open(filepath) as f:
            json_file = json.load(f)
            links = json_file['product_link']
        remove(path)
    return links