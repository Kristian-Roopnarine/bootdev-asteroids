import pygame
from constants import PLAYER_SHOOT_SPEED
from shot import Shot


class TripleShot:
    def create_shot(self, x, y, rotation):
        shot1 = Shot(x, y)
        shot1.velocity = pygame.Vector2(0, 1).rotate(rotation + 5) * PLAYER_SHOOT_SPEED
        shot2 = Shot(x, y)
        shot2.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        shot3 = Shot(x, y)
        shot3.velocity = pygame.Vector2(0, 1).rotate(rotation - 5) * PLAYER_SHOOT_SPEED
