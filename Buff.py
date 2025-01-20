import pygame
from circleshape import CircleShape


class Buff(CircleShape):
    def __init__(self, x, y, radius, buff_mod):
        super().__init__(x, y, radius)
        self.buff_mod = buff_mod
        self.font = pygame.font.SysFont(None, 12)

    def draw(self, screen):
        text_surface = self.font.render(
            self.buff_mod.buff_display_name, True, (255, 255, 255)
        )
        text_rect = text_surface.get_rect(center=(self.position.x, self.position.y))
        pygame.draw.circle(
            screen, self.buff_mod.color, self.position, self.radius, self.buff_mod.width
        )
        screen.blit(text_surface, text_rect)

    def update(self, dt):
        pass

    def get_buff(self):
        return self.buff_mod
