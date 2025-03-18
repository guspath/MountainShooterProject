#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from fixed_code.const import C_WHITE, WIN_HEIGHT, MENU_OPTION, TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP, \
    EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN
from fixed_code.enemy import Enemy
from fixed_code.entity import Entity1
from fixed_code.entityFactory import EntityFactory
from fixed_code.entityMediator import EntityMediator
from fixed_code.player import Player



class Level:
    def __init__(self, window, name, game_mode):

        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode  # MODO DE JOGO
        self.entity_list: list[Entity1] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        player = EntityFactory.get_entity('Player1')
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # 100ms

    def run(self):
        pygame.mixer.music.load(f'./assets/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player 1 - Health:{ent.health} | Score: {ent.score}', C_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player 2 - Health:{ent.health} | Score: {ent.score}', C_CYAN, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # VERIFYING COLLISIONS

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
