# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import random

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def draw_cards():
    card1 = random.choice(suits) + random.choice(ranks)
    card2 = random.choice(suits) + random.choice(ranks)
    return card1, card2


def get_card_value(card):
    if card[1] in 'JQK':
        return 10
    elif card[1] == 'A':
        return 1
    else:
        return int(card[1])


def play():
    player_cards = []
    dealer_cards = []
    player_value = 0
    dealer_value = 0

    # 玩家和庄家各先拿两张牌
    for i in range(2):
        player_cards.append(draw_cards())
        dealer_cards.append(draw_cards())
    # 计算当前牌面值
    for card in player_cards:
        player_value += get_card_value(card[0])
    for card in dealer_cards[1:]:
        dealer_value += get_card_value(card[0])

    print('玩家牌:', *player_cards)
    print('庄家牌(隐藏一张):', dealer_cards[0], 'X')

    # 玩家是否要第3张牌
    while player_value < 21:
        draw = input('是否要牌(Y/N)?')
        if draw.upper() == 'Y':
            player_cards.append(draw_cards())
            player_value += get_card_value(player_cards[-1][0])
            print('玩家牌:', *player_cards)
            if player_value > 21:
                print('玩家爆牌,庄家胜!')
                return
        else:
            break

    # 庄家根据规则要牌
    while dealer_value < 17:
        dealer_cards.append(draw_cards())
        dealer_value += get_card_value(dealer_cards[-1][0])

    # 显示全部牌面和值,判断胜负
    print('玩家牌:', *player_cards, '=', player_value)
    print('庄家牌:', *dealer_cards, '=', dealer_value)

    if player_value > 21:
        print('玩家爆牌,庄家胜!')
    elif dealer_value > 21 or dealer_value < player_value:
        print('玩家胜!')
    elif player_value == dealer_value:
        print('平局!')
    else:
        print('庄家胜!')


play()
