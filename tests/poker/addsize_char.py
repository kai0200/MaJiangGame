# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import curses

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

screen.addstr(0, 0, 'Hello World!', curses.color_pair(1))
screen.addstr(3, 3, 'r', curses.A_BOLD)

screen.refresh()
screen.getch()

curses.endwin()
