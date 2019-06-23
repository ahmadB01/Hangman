import urwid
import view

def main():
	main_loop = urwid.MainLoop(view.body, view.palette)

	try:
		main_loop.run()
	except KeyboardInterrupt:
		pass