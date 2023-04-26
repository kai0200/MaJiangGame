# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

# 打印mj 的所有pai

s = "U+1F000"

start = int(s.replace("U+", ""), 16)

for i in range(44):
    print(chr(start), end=" ")
    start += 1
