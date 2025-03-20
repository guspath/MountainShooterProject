#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from fixed_code.const import WIN_WIDTH, WIN_HEIGHT
from fixed_code.background import Background
from fixed_code.enemy import Enemy
from fixed_code.player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(7): # level1bg images
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2bg':
                list_bg = []
                for i in range(5): #level2bg images
                    list_bg.append(Background(f'Level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))