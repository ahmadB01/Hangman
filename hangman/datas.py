from random import choice
import json
import os

def get_random_word():
    """
        Returns a random word from the list in the
        datas/words.json file
    """
    with open('hangman/datas/words.json', 'r') as wf:
        words = json.loads(wf.read())
        return choice(words).upper()

def register_scores(scores):
    """
        Writes the list of scores entered in the parameters
        to the datas/scores.json file
    """
    with open('hangman/datas/scores.json', 'w') as sf:
        sf.write(json.dumps(scores))

def init_scores():
    """
        Initializes the scores dictionnary, the username
        entered by the user and his score in the datas/scores.json file

        scores = {username: score, ...}
    """
    scores = {}
    if os.path.isfile('hangman/datas/scores.json'):
        with open('hangman/datas/scores.json', 'r') as sf:
            scores = json.loads(sf.read())

    username = ' '
    score = 0

    while ' ' in username:
        username = input('Enter your username : ')
        if ' ' in username:
            print('You can not put a space in your username')

    if username in scores.keys():
        score = scores[username]
        print('Welcome back {}'.format(username))
    else:
        print('Welcome {}'.format(username))

    return (username, score, scores)

def get_drawings():
    """
        Returns the list of all the drawings
        for the Hangman game located in the datas/drawings.json file
    """
    with open('hangman/datas/drawings.json', 'r') as df:
        drawings = json.loads(df.read())
        return drawings