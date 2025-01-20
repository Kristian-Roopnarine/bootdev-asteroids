import pygame
from constants import PLAYER_SHOOT_SPEED
from shot import Shot


class TripleShot:
    can_spawn = True
    max_spawn = 1
    current_spawn = 0

    def __init__(self):
        self.buff_display_name = "..."
        self.type = "weapon"
        self.width = 0
        self.color = "red"

    def create_shot(self, x, y, rotation):
        shot1 = Shot(x, y)
        shot1.velocity = pygame.Vector2(0, 1).rotate(rotation + 5) * PLAYER_SHOOT_SPEED
        shot2 = Shot(x, y)
        shot2.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        shot3 = Shot(x, y)
        shot3.velocity = pygame.Vector2(0, 1).rotate(rotation - 5) * PLAYER_SHOOT_SPEED

    def inc_current_spawn(self, val):
        TripleShot.current_spawn += val
        if TripleShot.current_spawn >= TripleShot.max_spawn:
            self.update_can_spawn(False)

    def update_can_spawn(self, val):
        TripleShot.can_spawn = val

    def is_spawnable():
        return TripleShot.can_spawn
