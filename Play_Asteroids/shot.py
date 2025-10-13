import pygame
from circleshape import *
from constants import *

class Shoot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", pygame.Vector2(self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt