import urwid

class Menu(urwid.WidgetPlaceholder):
	def __init__(self, widgets):
		super(Menu, self).__init__(urwid.SolidFill(' '))
		self.widgets = widgets
		self.current = widgets[0]
		self.original_widget = self.current

	def next(self):
		self.original_widget = self.widgets[self.widgets.index(self.current)+1]
		self.current = self.original_widget

	def keypress(self, size, key):
		if key == 'esc':
			if self.widgets.index(self.current) > 0:
				self.original_widget = self.widgets[self.widgets.index(self.current)-1]
				self.current = self.original_widget
			else:
				raise urwid.ExitMainLoop()
		else:
			return super(Menu, self).keypress(size, key)

class Window(urwid.WidgetPlaceholder):
	def __init__(self, widget):
		super(App, self).__init__(urwid.SolidFill(' '))
		self.open(widget)

	def open(self, widget):
		self.original_widget = widget