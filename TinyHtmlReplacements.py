import sublime, sublime_plugin

def escape(s):
		import cgi
		return cgi.escape(s)

actions = {
	'a':  ('<a href="#">', '</a>'), 
	'b':  ('<strong>', '</strong>'), 
	'li': ('<li>', '</li>'),
	'p': ('<p>', '</p>'),
	'h2_sh': ('<h2 class="sectionHeading">', '</h2>'),
	'h3': ('<h3>', '</h3>'),
	'escape_html': escape,
}

class TinyHtmlReplacementsCommand(sublime_plugin.TextCommand):
	def run(self, edit, c = None, start = None, end = None):
		if c in actions:
			try:
				start, end = actions[c]
				self.surround(edit, start, end)
			except:
				f = actions[c]
				self.replace(edit, f)
		elif not (start and end):
			print 'Please, select a command! Try a, p or h1.'
			return

	def surround(self, edit, start, end):
		for region in self.view.sel():
				a = min(region.a, region.b)
				b = max(region.a, region.b) + len(start)
				self.view.insert(edit, a, start)
				self.view.insert(edit, b, end)

	def replace(self, edit, func):
		for region in self.view.sel():
			self.view.replace(edit, region, func(self.view.substr(region)))