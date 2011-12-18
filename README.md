# Tiny HTML Replacements #

Tiny HTML Replacements is a small but useful HTML plugin for [Sublime Text 2][sublime] editor. If you like it you can [donate][donate] to the author via PayPal.

It allows you surround selected HTML code with the tag customized in the Key Bindings config file.

## Example ##

Suppose you have an HTML code and you want to insert a link (or make it bold). Select the text you want to link, press Ctrl+q (can be configured, see below) and your text now is surrounded by `<a href="#"></a>`! 

Now Tiny HTML Replacements supports following tags:

* `<a href="#">`
* `<strong>`
* <li>
* <p>
* <h2 class="sectionHeading">
* <h3>
* You can add custom command! Just put the following args to the Key Bindings file:
	"args": {
		"c": "custom", 
		"start": "<mySuperTag class=\"myCustomizedClass\" border=1>", 
		"end": "</mySuperTag>"
	}


## Updates ##

If you have and ideas how to make the plugin better, feel free to [create an issue][issues]!

* (18 Dec 2011) First commit, some simple tags supported!

## Installation ##

Go to your Sublime Text 2 Packages directory:

	Windows: %APPDATA%\Sublime Text 2\Packages\

	Mac: ~/Library/Application Support/Sublime Text 2/Packages/	

and clone the repository here:
	
	git clone git://github.com/rozboris/Tiny-Html-Replacements.git "Tiny HTML Replacements"

## How to setup ##

* Open `Preferences → Key Bindings — User` in Sublime Text 2 and add the following code:
	
	{ "keys": ["ctrl+q"], "command": "tiny_html_replacements", "args": {"c": "li"}},
	{ "keys": ["ctrl+1"], "command": "tiny_html_replacements", "args": {"c": "p"}},
	{ "keys": ["ctrl+2"], "command": "tiny_html_replacements", "args": {"c": "h2_sh"}},
	{ "keys": ["ctrl+3"], "command": "tiny_html_replacements", "args": {"c": "h3"}},
	{ "keys": ["ctrl+5"], "command": "tiny_html_replacements", "args": {"c": "custom", "start": "<ul class=\"menu\">", "end": "</ul>"}},
	{ "keys": ["ctrl+4"], "command": "tiny_html_replacements", "args": {"c": "b"}}

## Donate ##

If you like Tiny HTML Replacements plugin you can [donate][donate] to the author (via PayPal).

---------

[sublime]: http://www.sublimetext.com/2
[package_control]: http://wbond.net/sublime_packages/package_control
[donate]: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=TVLQ2XQGFDS6Y&lc=RU&item_name=Tiny%20HTML%20Replacements%20plugin%20for%20Sublime%20Text%202&item_number=Tiny%20HTML%20Replacements&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted
[issues]: https://github.com/rozboris/Tiny-Html-Replacements/issues/new