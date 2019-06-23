from random import choice
import json
import os

def get_random_word():
    """
        Returns a random word from the list in the
        data/words.json file
    """
    with open('src/data/words.json', 'r') as wf:
        words = json.loads(wf.read())
        return choice(words).upper()

def register_scores(scores):
    """
        Writes the list of scores entered in the parameters
        to the datas/scores.json file
    """
    with open('src/data/scores.json', 'w') as sf:
        sf.write(json.dumps(scores))

def init_scores():
    """
        Initializes the scores dictionnary, the username
        entered by the user and his score in the datas/scores.json file

        scores = {username: score, ...}
    """
    scores = {}
    if os.path.isfile('src/data/scores.json'):
        with open('src/data/scores.json', 'r') as sf:
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
    """
        Returns the list of all the drawings
        for the Hangman game located in the datas/drawings.json file
    """
    with open('src/data/drawings.json', 'r') as df:
        drawings = json.loads(df.read())
        return drawings
