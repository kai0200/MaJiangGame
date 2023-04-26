# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for suit in suits:
    for rank in ranks:
        print(suit, rank, ord(suit), ord(rank))
