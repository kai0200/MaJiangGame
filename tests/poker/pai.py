# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4
import random

cards = [
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'T1',
    'T2',
    'T3',
    'T4',
    'T5',
    'T6',
    'T7',
    'T8',
    'T9',
    'B1',
    'B2',
    'B3',
    'B4',
    'B5',
    'B6',
    'B7',
    'B8',
    'B9',
    'B1',
    'B2',
    'B3',
    'B4',
    'B5',
    'B6',
    'B7',
    'B8',
    'B9',
    'B1',
    'B2',
    'B3',
    'B4',
    'B5',
    'B6',
    'B7',
    'B8',
    'B9',
    'B1',
    'B2',
    'B3',
    'B4',
    'B5',
    'B6',
    'B7',
    'B8',
    'B9',
    'W1',
    'W2',
    'W3',
    'W4',
    'W5',
    'W6',
    'W7',
    'W8',
    'W9',
    'W1',
    'W2',
    'W3',
    'W4',
    'W5',
    'W6',
    'W7',
    'W8',
    'W9',
    'W1',
    'W2',
    'W3',
    'W4',
    'W5',
    'W6',
    'W7',
    'W8',
    'W9',
    'W1',
    'W2',
    'W3',
    'W4',
    'W5',
    'W6',
    'W7',
    'W8',
    'W9',
    ' Z',
    ' Z',
    ' Z',
    ' Z',
    ' F',
    ' F',
    ' F',
    ' F',
    ' B',
    ' B',
    ' B',
    ' B',
]

random.shuffle(cards)

user_e = []
user_w = []
user_n = []
user_s = []

for i in range(13):
    user_e.append(cards.pop(0))
    user_w.append(cards.pop(0))
    user_n.append(cards.pop(0))
    user_s.append(cards.pop(0))

user_e.append(cards.pop(0))
user_e.sort()
user_w.sort()
user_n.sort()
user_s.sort()

#  print(user_e)
#  print(user_w)
#  print(user_n)
#  print(user_s)

print(len(cards))
print(len(cards) / 4)

print('P' * 17)
print('P' * 17)
print('P' * 17)
print('P' * 16)
