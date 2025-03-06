#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from fixed_code.entity import Entity1
from fixed_code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode # MODO DE JOGO
        self.entity_list: list[Entity1] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))


    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
