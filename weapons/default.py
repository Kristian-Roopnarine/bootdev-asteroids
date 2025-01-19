import pygame
from constants import PLAYER_SHOOT_SPEED
from shot import Shot


class DefaultWeapon:
    def create_shot(self, x, y, rotation):
        shot = Shot(x, y)
        shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
