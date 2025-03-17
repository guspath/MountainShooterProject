from fixed_code import entity
from fixed_code.enemy import Enemy
from fixed_code.entity import Entity1


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity1):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity1]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)