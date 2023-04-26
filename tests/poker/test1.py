# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import curses

screen = curses.initscr()
curses.start_color()
curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
large_format = curses.A_BOLD | curses.A_ITALIC | curses.A_UNDERLINE

message = 'Hello World!'
enlarge_pos = 3
enlarge_y, enlarge_x = screen.getyx()

screen.addstr(enlarge_y, enlarge_x, message[enlarge_pos], large_format)

while True:
    event = screen.getch()
    if event == curses.KEY_MOUSE:
        _, mx, my, _, _ = curses.getmouse()
        if mx == enlarge_x and my == enlarge_y:
            screen.addstr(enlarge_y, enlarge_x, message[enlarge_pos],
                          large_format)
