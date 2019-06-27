import urwid
import view
import model
import utils

def main():
    register_events()
    
    main_loop = urwid.MainLoop(view.body, view.palette)
    try:
        main_loop.run()
    except KeyboardInterrupt:
        pass

def register_events():
    urwid.connect_signal(view.b_game, 'click', login)
    urwid.connect_signal(view.b_quit, 'click', quit)
    urwid.connect_signal(view.b_enter, 'click', enter)
    urwid.connect_signal(view.b_start, 'click', start)

def login(_button):
    view.body.next()

def quit(_button):
    raise urwid.ExitMainLoop()

def enter(_button):
    model.player.username = view.e_username.get_edit_text()
    model.game.init_score(model.player)

    view.body.append(view.m_home(
        model.player.username,
        model.player.score,
        model.player.new()))

    view.body.next()

def start(_button):
    model.game.word = utils.random_word()

    view.body.append(view.s_game(
        model.game.display,
        model.player,
        model.game.drawing,
        model.game.wrongs))

    view.body.next()