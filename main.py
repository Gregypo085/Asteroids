# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # Create a screen surface (the game window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Groups to hold updateable and drawable objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = updateable, drawable # set the containers for Player class

    # Create a player instance at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        updateable.update(dt) #update player with delta time before drawing

        # Fill the screen with black
        screen.fill("black")
        
        for entity in drawable: # draw all drawable entities
            entity.draw(screen)
        

        # Update the display
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 FPS and get delta time in seconds


if __name__ == "__main__":
    main()
