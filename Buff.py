import pygame
from circleshape import CircleShape


class Buff(CircleShape):
    def __init__(self, x, y, radius, buff_mod):
        super().__init__(x, y, radius)
        self.buff_mod = buff_mod
        self.font = pygame.font.SysFont(None, 12)

    def draw(self, screen):
        text_surface = self.font.render("TS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y))
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        pass

    def get_buff(self):
        return self.buff_mod
