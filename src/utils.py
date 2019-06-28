import random
import json
import os

def random_style():
    path = 'src/titles/'
    n = random.randint(0, len(os.listdir(path))-1)
    with open(path+str(n), 'r') as tf:
        return tf.read()

def random_word():
    path = 'src/data/words.json'
    with open(path, 'r') as wf:
        words = json.loads(wf.read())
        return random.choice(words).upper()

def drawings():
    path = 'src/data/drawings.json'
    with open(path, 'r') as df:
        return json.loads(df.read())