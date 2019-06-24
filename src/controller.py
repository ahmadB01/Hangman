import urwid
import view

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

def login(_button):
	view.body.next()

def quit(_button):
	raise urwid.ExitMainLoop()

def enter(_button):
	pass