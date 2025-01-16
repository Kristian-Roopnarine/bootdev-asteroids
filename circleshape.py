import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def has_collided(self, obj):
        return self.position.distance_to(obj.position) <= (self.radius + obj.radius)

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
