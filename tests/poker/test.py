# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import curses

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

message = '♠♠♠♠♠♠♠♠♠♠♠♠'
screen.addstr(0, 0, message, curses.color_pair(1))
enlarge_pos = 3
enlarge_y, enlarge_x = screen.getyx()
enlarge_x += enlarge_pos
screen.addstr(enlarge_y, enlarge_x, message[enlarge_pos], curses.A_BOLD)

screen.refresh()
screen.getch()

curses.endwin()
