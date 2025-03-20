from fixed_code.const import ENTITY_SPEED
from fixed_code.entity import Entity1

class PlayerShot(Entity1):
        def __init__(self, name: str, position: tuple):
            super().__init__(name, position)

        def move(self, ):
            self.rect.centerx += ENTITY_SPEED[self.name]