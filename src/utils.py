import random
import json
import os

def random_style():
    path = '/home/ahmad/workspace/Hangman/src/titles/'
    n = random.randint(0, len(os.listdir(path))-1)
    with open(path+str(n), 'r') as tf:
        return tf.read()

def get_random_word():
    with open('data/words.json', 'r') as wf:
        words = json.loads(wf.read())
        return random.choice(words).upper()

def register_scores(scores):
    with open('data/scores.json', 'w') as sf:
        sf.write(json.dumps(scores))

def init_scores():
    scores = {}
    if os.path.isfile('data/scores.json'):
        with open('data/scores.json', 'r') as sf:
            scores = json.loads(sf.read())

    username = ' '
    score = 0

    while ' ' in username:
        username = input('Enter your username : ')
        if ' ' in username:
            print('You can not put a space in your username')

    if username in scores.keys():
        score = scores[username]
        print(f'Welcome back {username}')
    else:
        print(f'Welcome {username}')

    return (username, score, scores)

def get_drawings():
    with open('data/drawings.json', 'r') as df:
        drawings = json.loads(df.read())
        return drawings
