import urwid
import utils
from model import Menu

palette = [
    ('reversed', 'standout', ''),
    ('ask', 'default,bold', 'default', 'bold')]

title = urwid.Filler(urwid.Text(utils.random_style(), align='center'))

t_username = urwid.Text('')
b_start = urwid.Button('Start!')

m_newuser = urwid.Overlay(
    urwid.LineBox(
        urwid.Pile([
            ('pack', urwid.Divider()),
            ('pack', urwid.Text(('ask', 'Welcome.'), align='center')),
            ('weight', 5, urwid.Filler(
                urwid.Text('Looks like you are new here.\nYour score has been initialized at 0.'))),
            ('weight', 2, urwid.Filler(
                urwid.AttrMap(b_start, None, focus_map='reversed'),
                valign='bottom'))]),
        title='Hi!'),
    urwid.SolidFill(' '),
    align='center', width=('relative', 50),
    valign='middle', height=('relative', 50))

b_enter = urwid.Button('Enter')
e_username = urwid.Edit(('ask', 'Enter your name:\n> '))

m_login = urwid.Overlay(
    urwid.LineBox(
        urwid.Pile([
            ('pack', urwid.Divider()),
            ('weight', 15, title),
            ('pack', e_username),
            ('pack', urwid.Divider()),
            ('pack', urwid.AttrMap(b_enter, None, focus_map='reversed'))]),
        title='Sign in'),
    urwid.SolidFill(' '),
    align='center', width=('relative', 50),
    valign='middle', height=('relative', 50))

b_game = urwid.Button('Enter Game')
b_quit = urwid.Button('Quit')

m_welcome = urwid.Overlay(
    urwid.LineBox(
        urwid.Pile([
            ('pack', urwid.Divider()),
            ('weight', 15, title),
            ('weight', 4,
                urwid.Filler(urwid.BoxAdapter(
                    urwid.ListBox(urwid.SimpleFocusListWalker([
                        urwid.AttrMap(b_game, None, focus_map='reversed'),
                        urwid.AttrMap(b_quit, None, focus_map='reversed')])), 2),
                valign='bottom'))]),
        title='Welcome'),
    urwid.SolidFill(' '),
    align='center', width=('relative', 50),
    valign='middle', height=('relative', 50))

body = Menu([m_welcome, m_login])