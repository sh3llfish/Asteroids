from typing_extensions import override
import random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=LINE_WIDTH
        )

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        frag_velocity_1 = self.velocity.rotate(angle)
        frag_velocity_2 = self.velocity.rotate(-1 * angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        frag_1 = Asteroid(self.position[0], self.position[1], new_radius)
        frag_2 = Asteroid(self.position[0], self.position[1], new_radius)
        frag_1.velocity = frag_velocity_1 * 1.2
        frag_2.velocity = frag_velocity_2 * 1.2
        return
