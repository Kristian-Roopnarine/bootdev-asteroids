import pygame
from buff import Buff
import random

from constants import *
from shield import Shield
from weapons.triple_shot import TripleShot


"""
to control spawn of buffs
- track current number of buffs drawn
- use number of buffs along with max_buff_count to prevent too many buffs from rendering
"""


class BuffField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    all_buffs = [Shield, TripleShot]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position):
        random_buff_cls = random.choice(BuffField.all_buffs)
        random_buff = random_buff_cls()

        # TODO: cycle through until we get a buff that is spawnable
        if not random_buff_cls.is_spawnable():
            return

        random_buff.inc_current_spawn(1)
        b = Buff(position.x, position.y, radius, random_buff)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > BUFF_SPAWN_RATE:
            self.spawn_timer = 0

            y = random.randint(SCREEN_HEIGHT / 2, SCREEN_HEIGHT * 0.75)
            x = random.randint(SCREEN_WIDTH / 2, SCREEN_WIDTH * 0.75)
            position = pygame.Vector2(x, y)
            self.spawn(ASTEROID_MIN_RADIUS, position)
