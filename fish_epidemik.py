import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Epidemik")

# Create a surface for the water area
water_surface = pygame.Surface((WIDTH, HEIGHT // 2), pygame.SRCALPHA)
water_surface.fill((0, 0, 255, 128))  # Fill the water surface with semi-transparent dark blue
#create deck area surface
deck_surface = pygame.Surface((365, 50), pygame.SRCALPHA)
deck_surface.fill((184,134,11))


# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add more event types here as needed

    # Update game state
    # Example: Move character, check collisions, etc.

    # Render game state
    screen.fill((70, 130, 180))  # Fill the screen with black color
    screen.blit(water_surface, (0, HEIGHT // 2))  # Blit the water surface onto the main screen
    screen.blit(deck_surface, (0, 200))  # Blit the water surface onto the main screen
    # Draw game elements here

    # Flip the display
    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

