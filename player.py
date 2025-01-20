import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_INVINCIBILITY_CD,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot
from weapons.default import DefaultWeapon


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.global_cooldown = 0
        self.invicibility_cooldown = 0
        self.is_invincible = False
        self.weapon = DefaultWeapon()
        self.shield = 5
        self.lives = 1

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update_lives(self, val):
        if val < 0:
            self.invicibility_cooldown = PLAYER_INVINCIBILITY_CD
            self.is_invincible = True
        self.lives += val

    def update_shield(self, val):
        if val < 0:
            self.invicibility_cooldown = PLAYER_INVINCIBILITY_CD
            self.is_invincible = True
        self.shield += val

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.global_cooldown -= dt
        if self.is_invincible:
            self.invicibility_cooldown -= dt

        if self.invicibility_cooldown < 0:
            self.is_invincible = False
            self.invicibility_cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-1 * dt)

        if keys[pygame.K_SPACE]:
            if self.global_cooldown > 0:
                return
            self.shoot()
            self.global_cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.weapon.create_shot(self.position.x, self.position.y, self.rotation)

    def apply_buff(self, buff):
        if buff.type == "weapon":
            self.weapon = buff
        if buff.type == "shield":
            self.shield += buff.modify_stats()
