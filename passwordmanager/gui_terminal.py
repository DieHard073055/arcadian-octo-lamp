import curses
from urllib2 import urlopen
from HTMLParser import HTMLParser
from simplejson import loads

def get_new_joke():
	joke_json = loads(urlopen('http://api.icndb.com/jokes/random').read())
	return HTMLParser().unescape(joke_json['value']['joke'].encode('utf-8'))
	

def init_screen(stdscr):
	
	
	#Get the terminal ready for the curses
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
	
	#Check if the terminal supports colors
	if curses.has_colors():
		curses.start_color()
	
	#To enable keyboard input from keys like F1 F2 Home End 
	#stdscr.keypad(1)
	
	#initialize the color combination to use
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)







def begin_drawing(stdscr):
	window_size_h = 8
	#Draw the title of the program
	stdscr.addstr(0, 4, "  RANDOM QUOTES  ", curses.A_REVERSE)
	#stdscr.chgat(-1, curses.A_REVERSE)
	
	#Write the instructions at the bottom of the screen
	stdscr.addstr(window_size_h, 0, "Press 'R' to get a new joke, 'Q' to quit")
	
	#Change the color of R to Green
	stdscr.chgat(window_size_h, 7, 1, curses.A_BOLD | curses.color_pair(2))
	#Change the color of Q to Red
	stdscr.chgat(window_size_h, 35, 1, curses.A_BOLD | curses.color_pair(1))
	
	#Creating a window to hold the text box
	joke_window = curses.newwin(window_size_h-1, curses.COLS, 1, 0)
	
	#Creating the text box to hold the random jokes
	joke_text_box = joke_window.subwin(window_size_h-5, curses.COLS-4, 3, 2)
	
	#Add some text to your textbox.
	joke_text_box.addstr("Press 'R' to get your first joke!")
	
	#Draw a border on the main window
	joke_window.box()
	
	#Updating the screen with the changes made above.
	#Notice the order in which the windows are being refreshed.
	#First the most outer one then the inner one.
	stdscr.noutrefresh()
	joke_window.noutrefresh()
	
	#After refreshing the screen, Make the updates
	curses.doupdate()
	
	return(joke_window, joke_text_box)





def main_loop(stdscr, joke_window, joke_text_box):
	while True:
		#Get user input
		user_input = joke_window.getch()
		
		#User wants a new joke
		if user_input == ord('r') or user_input == ord('R'):
			joke_text_box.clear()
			joke_text_box.addstr("Downloading new joke... Please wait... ", curses.color_pair(3))
			
			joke_text_box.refresh()
			joke_text_box.clear()
			joke_text_box.addstr(get_new_joke(), curses.A_BOLD | curses.color_pair(2))
			
		elif user_input == ord('q') or user_input == ord('C'):
			break
			
		
		#To avoid flikering
		#Refresh the window from bottom up
		stdscr.noutrefresh()
		joke_window.noutrefresh()
		joke_text_box.noutrefresh()
		curses.doupdate()
		
	
def end_program(stdscr):
	#To end the program, reset the terminal to how it was before
	curses.nocbreak()
	#stdscr.keypad(0)
	curses.echo()
	curses.curs_set(1)
	
	#Restore the terminal to how its old self
	curses.endwin()
	
	
def main():
	#Initialization of the screen object
	stdscr = curses.initscr()
	
	init_screen(stdscr)
	joke_window, joke_text_box = begin_drawing(stdscr)
	main_loop(stdscr, joke_window, joke_text_box)
	end_program(stdscr)
	
	
	
if __name__ == '__main__':
	main()
