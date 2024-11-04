import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        roid_1 = self.velocity.rotate(angle)
        roid_2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = roid_1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = roid_2 * 1.2

