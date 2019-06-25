import random
import json
import os

def random_style():
    path = '/home/ahmad/workspace/Hangman/src/titles/'
    n = random.randint(0, len(os.listdir(path))-1)
    with open(path+str(n), 'r') as tf:
        return tf.read()

def random_word():
    path = '/home/ahmad/workspace/Hangman/src/data/words.json'
    with open(path, 'r') as wf:
        words = json.loads(wf.read())
        return random.choice(words).upper()

def drawings():
    path = '/home/ahmad/workspace/Hangman/src/data/drawings.json'
    with open(path, 'r') as df:
        return json.loads(df.read())