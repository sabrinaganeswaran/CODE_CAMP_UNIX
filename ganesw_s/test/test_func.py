#!/usr/bin/python

import curses
import time
stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)


def main(): #{


	return 0;

#}

if (__name__ == "__main__"): #{
	main();
#}

finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()