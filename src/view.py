import urwid
import utils
import model

palette = [
    ('reversed', 'standout', ''),
    ('ask', 'default,bold', 'default', 'bold')]

title = urwid.Filler(urwid.Text(utils.random_style(), align='center'))

b_quit = urwid.Button('Quit')

def s_endgame(player, won, lives, word):
    title = 'You won!' if won else 'You lost!'
    raw = ''
    if won:
        raw = f'Congratulations, you won with {lives} trie(s) left!'
    else:
        raw = f'Sorry, but you lost!'
    raw += f'\nTherefore, {player.username}\'s current score is: {player.score}'
    raw += f'\nThe word was indeed: {word}'

    text = urwid.Filler(urwid.Text(raw, align='center'))
    button = urwid.Filler(
        urwid.AttrMap(b_quit, None, focus_map='reversed'),
        valign='bottom')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('weight', 5, text),
        ('weight', 1, button)])

    return urwid.Overlay(
        urwid.LineBox(pile, title=title),
        urwid.SolidFill(' '),
        align='center', width=('relative', 50),
        valign='middle', height=('relative', 50),
        min_width=100, min_height=25)

b_game_ok = urwid.Button('OK')
e_letter = urwid.Edit(('ask', 'Enter a letter:\n> '))

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
            ('pack', e_letter),
            ('weight', 1, button_ok)]))

    word = urwid.Filler(
        urwid.Pile([
            ('pack', urwid.Divider()),
            ('pack', urwid.Text(('ask', 'Word:\n'), align='center')),
            ('pack', urwid.Text(display, align='center'))]),
        height=('relative', 100), min_height=50)

    box_word = urwid.LineBox(word)

    piles_left = urwid.Pile([
        ('weight', 1, box_word),
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

def m_home(player, new):
    raw = ''
    if new == True:
        raw = 'Looks like you are new here.'
    else:
        raw = 'Well, you already played this game, welcome back!'
    raw += f'\nTherefore, your current score is : {player.score}'

    title = urwid.Text(('ask', f'Welcome, {player.username}.'), align='center')
    text = urwid.Filler(urwid.Text(raw, align='center'))
    button = urwid.Filler(
        urwid.AttrMap(b_start, None, focus_map='reversed'),
        valign='bottom')

    pile = urwid.Pile([
        ('pack', urwid.Divider()),
        ('pack', title),
        ('weight', 5, text),
        ('weight', 1, button)])

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

menu = model.Menu([m_welcome(), m_login()])
body = model.Window(menu)