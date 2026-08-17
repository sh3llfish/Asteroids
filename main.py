import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    _ = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0        # Delta time
    while True:
        log_state() # Log for bootdev check

        # Placeholder for game events handling.
        for event in pygame.event.get():
            pass
        _ = screen.fill((0, 0, 0))  # fill screen with pure black
        pygame.display.flip()       # refresh screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
