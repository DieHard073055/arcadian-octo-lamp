#!usr/bin/python2.7

def main():
	import pygtk
	pygtk.require('2.0')
	import gtk
	clipboard = gtk.clipboard_get()
	text = clipboard.wait_for_text()
	print '..setting our text to your clibpboard'
	clipboard.set_text('I am in your clipboard')
	clipboard.store()
	print '..clipboard text sotored!'

def clipboard(clip_text):
	import pygtk
	pygtk.require('2.0')
	import gtk
	clipboard = gtk.clipboard_get()
	text = clipboard.wait_for_text()
	clipboard.set_text(clip_text)
	clipboard.store()

if __name__ == '__main__':
	main()


