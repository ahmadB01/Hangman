import urwid
import json
import os
import random
import utils

class Window(urwid.WidgetPlaceholder):
    def __init__(self, widgets):
        super(Window, self).__init__(urwid.SolidFill(' '))
        self.widgets = widgets
        self.original_widget = self.widgets[0]

    @property
    def widget_index(self):
        return self.widgets.index(self.original_widget)
    
    def append(self, widget):
        self.widgets.append(widget)

    def next(self):
        self.original_widget = self.widgets[self.widget_index+1]

    def keypress(self, size, key):
        if key != 'esc':
            return super(Window, self).keypress(size, key)
        if self.widget_index == 0:
            raise urwid.ExitMainLoop()

        self.original_widget = self.widgets[self.widget_index-1]

class Game(object):
    def __init__(self):
        self.scores = {}
        self.word = ''
        self.lives = len(utils.drawings())-1

    @property
    def display(self):
        return '*' * len(self.word)

    @property
    def wrongs(self):
        letters = []
        for i, k in enumerate(self.display):
            if k == self.word[i]:
                letters.append(self.word[i])

        return letters

    @property
    def drawing(self):
        return '\n'.join(utils.drawings()[::-1][self.lives])

    def update_display(self, letter):
        for i, k in enumerate(self.word):
            if k == letter:
                self.display = self.display[:i] + letter + self.display[i+1:]

    def init_score(self, player):
        path = '/home/ahmad/workspace/Hangman/src/data/scores.json'
        if os.path.isfile(path):
            with open(path, 'r') as sf:
                self.scores = json.loads(sf.read())
        else:
            self.register_score(player)

        if player.username in self.scores.keys():
            player.score = self.scores[player.username]

    def register_score(self, player):
        self.scores[player.username] = player.score
        with open(path, 'w') as sf:
            sf.write(json.dumps(self.scores))

class Player(object):
    def __init__(self):
        self.username = ''
        self.score = 0

    def new(self):
        path = '/home/ahmad/workspace/Hangman/src/data/scores.json'
        scores = {}
        with open(path, 'r') as sf:
            scores = json.loads(sf.read())

        return not self.username in scores.keys()

game = Game()
player = Player()