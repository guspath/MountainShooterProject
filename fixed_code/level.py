#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from fixed_code.const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, TIMEOUT_LEVEL, EVENT_TIMEOUT, TIMEOUT_STEP, \
    EVENT_ENEMY, SPAWN_TIME
from fixed_code.entity import Entity1
from fixed_code.entityFactory import EntityFactory


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE,(10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
