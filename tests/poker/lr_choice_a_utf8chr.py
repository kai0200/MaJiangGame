# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
# 读取utf8字符展示在终端里
import curses
import os

os.environ['NCURSES_NO_UTF8_ACS'] = '1'

curses.setupterm()
screen = curses.initscr()

# enable UTF-8 encoding
curses.start_color()
curses.use_default_colors()
screen.keypad(True)
curses.curs_set(0)
curses.cbreak()
curses.noecho()

message = '🀡🀢🀣🀤🀥🀦🀧🀨🀩🀪🀫'

position = 0
while True:
    for i, char in enumerate(message):
        if i == position:
            screen.addch(0, i, char, curses.A_REVERSE)
        else:
            screen.addch(0, i, char)
    screen.refresh()
    key = screen.getch()
    if key == curses.KEY_RIGHT:
        position += 1
        #  screen.refresh()
    elif key == curses.KEY_LEFT:
        position -= 1
        #  screen.refresh()
    # Handle out of bounds
    if position < 0:
        position = 0
        #  screen.refresh()
    if position > len(message) - 1:
        position = len(message) - 1
        #  screen.refresh()
    if key == 10:  # Enter key
        break
curses.endwin()

print(position)
