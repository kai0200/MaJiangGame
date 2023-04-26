# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4

import random

# 麻将牌定义
mahjong_tiles = {
    '条子': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    '筒子': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    '万子': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    '东': [1, 2, 3, 4],
    '南': [1, 2, 3, 4],
    '西': [1, 2, 3, 4],
    '北': [1, 2, 3, 4],
    '红中': [1],
    '发财': [1],
    '白板': [1]
}


# 随机抽取麻将牌
def draw_tile():
    tile_type = random.choice(list(mahjong_tiles.keys()))
    return random.choice(mahjong_tiles[tile_type])


# 打印麻将
def print_tile(tile):
    if tile in mahjong_tiles['条子']:
        print(f'条子{tile}')
    elif tile in mahjong_tiles['筒子']:
        print(f'筒子{tile}')
    elif tile in mahjong_tiles['万子']:
        print(f'万子{tile}')
    elif tile in mahjong_tiles['东']:
        print(f'东风{tile}')
    elif tile in mahjong_tiles['南']:
        print(f'南风{tile}')
    elif tile in mahjong_tiles['西']:
        print(f'西风{tile}')
    elif tile in mahjong_tiles['北']:
        print(f'北风{tile}')
    elif tile in mahjong_tiles['红中']:
        print(f'红中')
    elif tile in mahjong_tiles['发财']:
        print(f'发财')
    elif tile in mahjong_tiles['白板']:
        print(f'白板')


# 玩家和庄家手牌
player_tiles = []
dealer_tiles = []

# 玩家从墙墙开始抽牌
for i in range(13):
    player_tiles.append(draw_tile())
    print_tile(player_tiles[-1])

# 庄家从墙墙开始抽牌
for i in range(13):
    dealer_tiles.append(draw_tile())

print('庄家:', *dealer_tiles)  # 显示庄家手牌
print('玩家:', *player_tiles)  # 显示玩家手牌
