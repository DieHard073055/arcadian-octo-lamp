#!usr/bin/python27

import curses



def init_screen(stdscr):
	
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	
	if curses.has_colors():
		curses.start_color()
	
	#TODO : set the colors
	curses.init_pair()

def draw_menu(stdscr):
	pass

def menu_update(stdscr, menu_window, menu_status_box):
	pass


def end_program(stdscr):
	#To end the program, reset the terminal to how it was before
	curses.nocbreak()
	#stdscr.keypad(0)
	curses.echo()
	curses.curs_set(1)
	
	#Restore the terminal to how its old self
	curses.endwin()


def main():
	pass


if __name__ == '__main__':
	main()
