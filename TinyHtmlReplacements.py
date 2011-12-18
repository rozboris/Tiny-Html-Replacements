import sublime, sublime_plugin

actions = {
	'a':  ('<a href="#">', '</a>'), 
	'b':  ('<strong>', '</strong>'), 
	'li': ('<li>', '</li>'),
	'p': ('<p>', '</p>'),
	'h2_sh': ('<h2 class="sectionHeading">', '</h2>'),
	'h3': ('<h3>', '</h3>'),
}

class TinyHtmlReplacementsCommand(sublime_plugin.TextCommand):
	def run(self, edit, c = None, start = None, end = None):
		if c in actions:
			start, end = actions[c]
		elif not (start and end):
			print 'Please, select a command! Try a, p or h1.'
			return

		for region in self.view.sel():
				a = min(region.a, region.b)
				b = max(region.a, region.b) + len(start)
				self.view.insert(edit, a, start)
				self.view.insert(edit, b, end)
