import urwid

class Menu(urwid.WidgetPlaceholder):
    def __init__(self, widgets):
        super(Menu, self).__init__(urwid.SolidFill(' '))
        self.widgets = widgets
        self.original_widget = self.widgets[0]

    def append(self, widget):
        self.widgets.append(widget)

    def next(self):
        self.original_widget = self.widgets[self.widgets.index(self.original_widget)+1]

    def keypress(self, size, key):
        if key == 'esc':
            if self.widgets.index(self.original_widget) > 0:
                self.original_widget = self.widgets[self.widgets.index(self.original_widget)-1]
            else:
                raise urwid.ExitMainLoop()
        else:
            return super(Menu, self).keypress(size, key)

class Window(urwid.WidgetPlaceholder):
    def __init__(self, widget):
        super(App, self).__init__(urwid.SolidFill(' '))
        self.open(widget)

    def open(self, widget):
        self.original_widget = widget

class Game(object):
    def __init__(self):
        pass

    def init_scores(self):
        pass

    def register_scores(self):
        pass

    def random_word(self):
        pass