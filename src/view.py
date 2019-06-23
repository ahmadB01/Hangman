import urwid
import utils
from model import App

palette = [
	('reversed', 'standout', '')]

b_game = urwid.Button('Enter Game')
b_quit = urwid.Button('Quit')

s_welcome_container = urwid.LineBox(
	urwid.Pile([
		('pack', urwid.Divider()),
		('pack', urwid.Text(utils.random_style(), align='center')),
		('weight', 4, urwid.Filler(urwid.BoxAdapter(
			urwid.ListBox(urwid.SimpleFocusListWalker([
				urwid.AttrMap(b_game, None, focus_map='reversed'),
				urwid.AttrMap(b_quit, None, focus_map='reversed')])), 4)))]),
	title='Welcome')

s_welcome = urwid.Overlay(s_welcome_container, urwid.SolidFill(' '),
	align='center', width=('relative', 50),
	valign='middle', height=('relative', 50))

body = App(s_welcome)