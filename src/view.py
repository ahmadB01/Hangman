import urwid
import utils
from model import Window

palette = [
    ('reversed', 'standout', ''),
    ('ask', 'default,bold', 'default', 'bold')]

title = urwid.Filler(urwid.Text(utils.random_style(), align='center'))

b_game_ok = urwid.Button('OK')
e_word = urwid.Edit(('ask', 'Enter a letter:\n> '))

def s_game(display, player, drawing, wrongs):
    scores = urwid.LineBox(
        urwid.Pile([
            ('pack', urwid.Text(f'Username: {player.username}.')),
            ('pack', urwid.Text(f'Score: {player.score}.'))]),
        title='Player')

    current = urwid.LineBox(
        urwid.Frame(
            urwid.Filler(urwid.Text(drawing, align='center')),
            urwid.Text(', '.join(wrongs))))

    input_letter = urwid.LineBox(
        urwid.Pile([
            ('pack', e_word),
            ('pack', b_game_ok)]))

    word = urwid.Filler(
        urwid.Pile([
            ('pack', urwid.Text(('ask', 'Word:\n'))),
            ('pack', urwid.Text(display))]))

    piles_left = urwid.Pile([
        (36, word),
        ('weight', 36, input_letter)])

    piles_right = urwid.Pile([
        (20, scores),
        (50, current)])

    columns = urwid.Columns([
        (35, piles_left),
        (35, piles_right)])

    return urwid.Overlay(columns, urwid.SolidFill(' '),
        align='center', width=('relative', 75),
        valign='middle', height=('relative', 75))

b_start = urwid.Button('Start!')

def m_home(username, score, new):
    raw = ''
    if new == True:
        raw = 'Looks like you are new here.'
    else:
        raw = 'Well, you already played this game, welcome back!'
    raw += f'\nTherefore, your current score is : {score}'

    title = urwid.Text(('ask', f'Welcome, {username}.'), align='center')
    text = urwid.Filler(urwid.Text(raw))
    button = urwid.Filler(
        urwid.AttrMap(b_start, None, focus_map='reversed'),
        valign='bottom')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('pack', title),
        ('weight', 5, text),
        ('weight', 2, button)])

    return urwid.Overlay(
        urwid.LineBox(pile, title='Hi!'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50))

b_enter = urwid.Button('Enter')
e_username = urwid.Edit(('ask', 'Enter your name:\n> '))

def m_login():
    button = urwid.AttrMap(b_enter, None, focus_map='reversed')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('weight', 15, title),
        ('pack', e_username),
        ('pack', urwid.Divider()),
        ('pack', button)])

    return urwid.Overlay(
        urwid.LineBox(pile, title='Sign in'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50))

b_game = urwid.Button('Enter Game')
b_quit = urwid.Button('Quit')

def m_welcome():
    button_game = urwid.AttrMap(b_game, None, focus_map='reversed')
    button_quit = urwid.AttrMap(b_quit, None, focus_map='reversed')

    buttons_list = urwid.ListBox(urwid.SimpleFocusListWalker([
        button_game,
        button_quit]))

    buttons_flow = urwid.BoxAdapter(buttons_list, 2)

    buttons = urwid.Filler(buttons_flow, valign='bottom')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('weight', 15, title),
        ('weight', 4, buttons)])

    return urwid.Overlay(
        urwid.LineBox(pile, title='Welcome'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50))

body = Window([m_welcome(), m_login()])