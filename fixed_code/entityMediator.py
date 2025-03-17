from xml.dom.minidom import Entity

from fixed_code import entity
from fixed_code.const import WIN_WIDTH
from fixed_code.enemy import Enemy
from fixed_code.enemyShot import EnemyShot
from fixed_code.entity import Entity1
from fixed_code.player import Player
from fixed_code.playerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity1):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
            if isinstance(ent, PlayerShot):
                if ent.rect.left >= WIN_WIDTH:
                    ent.health = 0
            if isinstance(ent, EnemyShot):
                if ent.rect.right <= 0:
                    ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interation == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score


    @staticmethod
    def verify_collision(entity_list: list[Entity1]):
        for i in range(len(entity_list)):
            entity_one = entity_list[i]
            EntityMediator.__verify_collision_window(entity_one)
            for j in range(i + 1, len(entity_list)):
                entity_two = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_one, entity_two)

    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)


