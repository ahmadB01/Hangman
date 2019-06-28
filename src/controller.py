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

def end():
    model.player.score += model.game.lives
    model.game.register_score(model.player)

    view.body.open(view.s_endgame(
        model.player,
        model.game.won(),
        model.game.lives,
        model.game.word))

def s_game():
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
    username = view.e_username.get_edit_text()
    if ' ' in username or username == '':
        return

    model.player.username = username
    model.game.init_score(model.player)

    view.body.open(view.m_home(
        model.player,
        model.player.new()))

@eventhandler(view.b_start)
def start(_button):
    model.game.word = utils.random_word()
    model.game.display = '*' * len(model.game.word)
    s_game()

@eventhandler(view.b_game_ok)
def update(_button):
    letter = view.e_letter.get_edit_text()

    if model.game.lives == 0 or model.game.won():
        end()
        return
    elif not letter.isalpha() or letter == '':
        return

    letter = letter[0].upper()
    view.e_letter.set_edit_text('')

    if letter in model.game.word:
        model.game.update_display(letter)
    elif letter not in model.game.wrongs:
        model.game.wrongs.append(letter)
        model.game.lives -= 1

    s_game()