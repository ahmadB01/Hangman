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
            header=urwid.Text(', '.join(wrongs), align='center')))

    button_ok = urwid.Filler(
        urwid.AttrMap(b_game_ok, None, focus_map='reversed'),
        valign='bottom')

    input_letter = urwid.LineBox(
        urwid.Pile([
            ('pack', e_word),
            ('weight', 1, button_ok)]))

    word = urwid.Filler(
        urwid.Pile([
            ('pack', urwid.Divider()),
            ('pack', urwid.Text(('ask', 'Word:\n'), align='center')),
            ('pack', urwid.Text(display, align='center'))]),
        height=('relative', 100), min_height=50)

    box_word = urwid.LineBox(word)

    piles_left = urwid.Pile([
        ('weight', 2, box_word),
        ('weight', 1, input_letter)])

    piles_right = urwid.Pile([
        ('weight', 1, scores),
        ('weight', 5, current)])

    columns = urwid.Columns([
        ('weight', 2, piles_left),
        ('weight', 1, piles_right)])

    padding = urwid.Padding(columns, align='center')

    return urwid.Overlay(
        urwid.LineBox(padding, title='Game'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50),
        min_width=100, min_height=25)

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
        valign='middle', height=('relative', 50),
        min_width=100, min_height=25)

b_enter = urwid.Button('Enter')
e_username = urwid.Edit(('ask', 'Enter your name:\n> '))

def m_login():
    button = urwid.AttrMap(b_enter, None, focus_map='reversed')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('weight', 5, title),
        ('pack', e_username),
        ('pack', urwid.Divider()),
        ('pack', button)])

    return urwid.Overlay(
        urwid.LineBox(pile, title='Sign in'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50),
        min_width=100, min_height=25)

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
        ('weight', 5, title),
        ('weight', 1, buttons)])

    return urwid.Overlay(
        urwid.LineBox(pile, title='Welcome'),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50),
        min_width=100, min_height=25)

body = Window([m_welcome(), m_login()])