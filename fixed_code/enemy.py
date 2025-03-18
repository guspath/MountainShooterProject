#!/usr/bin/python
# -*- coding: utf-8 -*-
from fixed_code.enemyShot import EnemyShot
from fixed_code.entity import Entity1
from fixed_code.const import ENTITY_SPEED, ENTITY_SHOT_DELAY


class Enemy(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
