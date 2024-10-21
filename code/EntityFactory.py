#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy, Enemy3
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        if entity_name == 'Level1Bg':
            list_bg = []
            for i in range(7):  # Número de imagens do Level 1
                list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
            return list_bg
        elif entity_name == 'Level2Bg':
            list_bg = []
            for i in range(5):  # Número de imagens do Level 2
                list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
            return list_bg
        elif entity_name == 'Level3Bg':
            list_bg = []
            for i in range(4):  # Número de imagens do Level 3
                list_bg.append(Background(f'Level3Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level3Bg{i}', (WIN_WIDTH, 0)))
            return list_bg
        elif entity_name == 'Player1':
            return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
        elif entity_name == 'Player2':
            return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
        elif entity_name == 'Enemy1':
            return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        elif entity_name == 'Enemy2':
            return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
        elif entity_name == 'Enemy3':
            return Enemy3('Enemy3', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))  # Para o Level 3
        else:
            return None  # Captura casos não tratados
