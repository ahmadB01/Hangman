import urwid
import view
import model
import utils

def eventhandler(button):
    def bind(func):
        urwid.connect_signal(button, 'click', func)
        return func
    return bind

def main():
    main_loop = urwid.MainLoop(view.body, view.palette)
    try:
        main_loop.run()
    except KeyboardInterrupt:
        pass

def display():
    view.body.open(view.s_game(
        model.game.display,
        model.player,
        model.game.drawing,
        model.game.wrongs))

@eventhandler(view.b_game)
def login(_button):
    view.menu.next()

@eventhandler(view.b_quit)
def quit(_button):
    raise urwid.ExitMainLoop()

@eventhandler(view.b_enter)
def enter(_button):
    model.player.username = view.e_username.get_edit_text()
    model.game.init_score(model.player)

    view.body.open(view.m_home(
        model.player,
        model.player.new()))

@eventhandler(view.b_start)
def start(_button):
    model.game.word = utils.random_word()
    model.game.display = '*' * len(model.game.word)
    display()

@eventhandler(view.b_game_ok)
def update(_button):
    letter = view.e_letter.get_edit_text()[0].upper()
    view.e_letter.set_edit_text('')

    if letter in model.game.word:
        model.game.update_display(letter)
    else:
        model.game.wrongs.append(letter)
        model.game.lives -= 1

    display()