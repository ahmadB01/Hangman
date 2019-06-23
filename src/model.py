import urwid

class App(urwid.WidgetPlaceholder):
	def __init__(self, widget):
		super(App, self).__init__(urwid.SolidFill(' '))
		self.open(widget)

	def open(self, widget):
		self.original_widget = widget