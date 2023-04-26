# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
# 左右方向键选中字符
import curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
message = "🀀 🀁 🀂 🀃 🀄 🀅 🀆 🀇 🀈 🀉 🀊 🀋 🀌 🀍 🀎 🀏 🀐 🀑 🀒 🀓 🀔 🀕 🀖 🀗 🀘 🀙 🀚 🀛 🀜 🀝 🀞 🀟 🀠 🀡 🀢 🀣 🀤 🀥 🀦 🀧 🀨 🀩 🀪 🀫
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
    elif key == curses.KEY_LEFT:
        position -= 1
    # Handle out of bounds
    if position < 0:
        position = 0
    if position > len(message) - 1:
        position = len(message) - 1
    if key == 10:  # Enter key
        break
curses.endwin()
