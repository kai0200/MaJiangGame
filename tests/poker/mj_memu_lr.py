# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
import curses

menu_items = ["New", "Open", "Save", "Exit"]
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
max_width = max(len(item) for item in menu_items)
start_x = (screen.getmaxyx()[1] - max_width * len(menu_items)) // 2
selected = 0
while True:
    for i, item in enumerate(menu_items):
        if i == selected:
            color = curses.A_REVERSE
        else:
            color = curses.A_NORMAL
        screen.addstr(i, start_x + i * max_width, item.ljust(max_width), color)
    screen.refresh()
    key = screen.getch()
    if key in [curses.KEY_RIGHT, ord(' ')]:
        selected += 1
    elif key in [curses.KEY_LEFT]:
        selected -= 1
    if selected >= len(menu_items):
        selected = 0
    elif selected < 0:
        selected = len(menu_items) - 1
    if key == 10:  # Enter key
        screen.addstr(5, 0, f"You selected {menu_items[selected]}")
        screen.getch()
        break
curses.endwin()  # Deinitialize the screen
