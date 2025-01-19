from cgitb import text
import sys
import pygame
from Buff import Buff
from BuffField import BuffField
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from gamestate import GameState
from player import Player
from shot import Shot

"""
1. Explosion Effect for asterids
2. Create different weapon types
3. Make asteroids lumpy instead of perfectly round
    3.1 - will I have to update hit detection for this?
4. Add shield power up
5. Add speed power up
6. Bombs that can be dropped
"""


def main():
    pygame.font.init()
    pygame.display.set_caption("Kristian's Asteroids")
    my_font = pygame.font.SysFont("Arial", 30)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    gs = GameState()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    buffs = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    BuffField.containers = (updatable,)
    Buff.containers = (buffs, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    buff_field = BuffField()
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    gs.PAUSED = not gs.PAUSED
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        if not gs.PAUSED:
            for u in updatable:
                u.update(dt)

            for a in asteroids:
                if a.has_collided(player):
                    print("Game over!")
                    sys.exit(0)

                for s in shots:
                    if a.has_collided(s):
                        gs.update_score(a.radius)
                        a.split()
                        s.kill()

            for b in buffs:
                for s in shots:
                    if b.has_collided(s):
                        buff = b.get_buff()
                        b.kill()
                        s.kill()
                        player.apply_buff(buff)

        for d in drawable:
            d.draw(screen)

        game_score = my_font.render(gs.get_score(), False, (255, 255, 255))
        screen.blit(game_score, (10, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
