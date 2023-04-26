# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import curses

# initialize curses
curses.setupterm()

# create a window
stdscr = curses.initscr()

# enable UTF-8 encoding
curses.start_color()
curses.use_default_colors()
stdscr.keypad(True)
curses.curs_set(0)
curses.cbreak()
curses.noecho()

# print a UTF-8 character
stdscr.addstr(0, 0, "中")

# refresh the screen
stdscr.refresh()

# wait for user input
stdscr.getch()

# clean up
curses.endwin()
