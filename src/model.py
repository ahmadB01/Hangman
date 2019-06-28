import urwid
import json
import os
import random
import utils

class Menu(urwid.WidgetPlaceholder):
    def __init__(self, widgets):
        super(Menu, self).__init__(urwid.SolidFill(' '))
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
            return super(Menu, self).keypress(size, key)
        if self.widget_index == 0:
            raise urwid.ExitMainLoop()

        self.original_widget = self.widgets[self.widget_index-1]

class Window(urwid.WidgetPlaceholder):
    def __init__(self, widget):
        super(Window, self).__init__(urwid.SolidFill(' '))
        self.open(widget)

    def open(self, widget):
        self.original_widget = widget

class Game(object):
    def __init__(self):
        self.scores = {}
        self.word = ''
        self.lives = len(utils.drawings())-1
        self.wrongs = []
        self.display = ''

    @property
    def drawing(self):
        return '\n'.join(utils.drawings()[::-1][self.lives])

    def update_display(self, letter):
        for i, k in enumerate(self.word):
            if k == letter:
                self.display = self.display[:i] + letter + self.display[i+1:]

    def init_score(self, player):
        path = 'src/data/scores.json'

        if not os.path.isfile(path):
            self.register_score(player)
        else:
            with open(path, 'r') as sf:
                self.scores = json.loads(sf.read())

        if player.username in self.scores.keys():
            player.score = self.scores[player.username]

    def register_score(self, player):
        path = 'src/data/scores.json'

        self.scores[player.username] = player.score
        with open(path, 'w') as sf:
            sf.write(json.dumps(self.scores))

    def won(self):
        return self.word == self.display

class Player(object):
    def __init__(self):
        self.username = ''
        self.score = 0

    def new(self):
        path = 'src/data/scores.json'
        scores = {}
        with open(path, 'r') as sf:
            scores = json.loads(sf.read())

        return not self.username in scores.keys()

game = Game()
player = Player()