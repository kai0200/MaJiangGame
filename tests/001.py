# -*- coding: utf-8 -*-
# vim: expandtab softtabstop=4 shiftwidth=4


class MahjongTile:

    def __init__(self, tile_type, value):
        self.tile_type = tile_type  # 牌面类型:条、筒、万、字牌
        self.value = value  # 点值,1-9
        self.flower = False  # 是否花牌
        self.direction = None  # 字牌的方向,东南西北中发白

    def __repr__(self):
        if self.tile_type == '条':
            tile_type = 'T'
        elif self.tile_type == '筒':
            tile_type = 'C'
        elif self.tile_type == '万':
            tile_type = 'W'
        elif self.tile_type in ['东', '南', '西', '北']:
            tile_type = self.tile_type[0]
            self.direction = self.tile_type
        else:
            tile_type = self.tile_type[0]
            self.flower = True

        return '%s%s' % (tile_type, self.value)


class MahjongHand:

    def __init__(self, tiles):
        self.tiles = tiles  # 手牌,包含MahjongTile对象列表
        self.flower_tiles = []  # 花牌


class MahjongPlayer:

    def __init__(self, hand):
        self.hand = hand  # 玩家手牌,MahjongHand对象
