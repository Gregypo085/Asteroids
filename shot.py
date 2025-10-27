import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        # seconds the shot will live for before being removed
        self.life = 1.5

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        # decrement lifetime and remove when expired
        self.life -= dt
        if self.life <= 0:
            self.kill()
            return

        # move
        self.position += self.velocity * dt

        # If the shot leaves the screen fully (including its radius), remove it.
        if (
            self.position.x < -self.radius
            or self.position.x > SCREEN_WIDTH + self.radius
            or self.position.y < -self.radius
            or self.position.y > SCREEN_HEIGHT + self.radius
        ):
            self.kill()
            return