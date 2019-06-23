import urwid
import view

def change_screen(screen):
	view.body.open(screen)

def main():
	register_events()
	
	main_loop = urwid.MainLoop(view.body, view.palette)
	try:
		main_loop.run()
	except KeyboardInterrupt:
		pass

def register_events():
	pass