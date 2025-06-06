#!/usr/bin/python
# -*- coding: utf-8 -*-
from fixed_code.const import ENTITY_SPEED, WIN_WIDTH
from fixed_code.entity import Entity1


class Background(Entity1):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH