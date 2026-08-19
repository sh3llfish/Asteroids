from typing import override
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius = SHOT_RADIUS) -> None:
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
