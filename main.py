from cgitb import text
import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from gamestate import GameState
from player import Player
from shot import Shot


def main():
    pygame.font.init()
    my_font = pygame.font.SysFont("Arial", 30)
    text_surface = my_font.render("Hello World", False, (255, 255, 255))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    gs = GameState()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        screen.fill("black")
        game_score = my_font.render(f"{gs.score}", False, (255, 255, 255))
        screen.blit(game_score, (10, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
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

        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
