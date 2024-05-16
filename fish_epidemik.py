import pygame
import sys
import random

#import cloud image
cloud_image = pygame.image.load('C:\\Users\\Smg21\\OneDrive\\Desktop\\Pixel_Jam_Fish_Epidemik\\sprite_level_one\\cloud_sprite.png')
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

#List to hold them clouds
clouds = []
maxClouds = 10 #Max clouds in sky
minDistanceBetweenClouds = 150 #min distance between any two clouds
#Function to create the cloud objects 

#some more cloud logics
def is_valid_position(new_cloud, existing_clouds):
    for cloud in existing_clouds:
        if abs(new_cloud['x'] - cloud['x']) < minDistanceBetweenClouds:
            return False
    return True 
    
def create_cloud(existing_clouds):
    base_x = random.randint(WIDTH, WIDTH * 2) #base x coordinates starts them off screen
    y = random.randint(HEIGHT // 2, HEIGHT - 100) #random y that is above the deck
    #offset = random.randint(-100, 100) #random offsets between -100 and 100 px
    #x = base_x + offset #final x coordinate w offset applied
    return {'image': cloud_image, 'x': base_x, 'y': y} #0?

#some clouds logic no more cloud snake 


# Game loop
running = True
while running:

    #we gotta remove them clouds that went off
    clouds[:] = [cloud for cloud in clouds if cloud['x'] > -cloud_image.get_width()]

    #Create the new clouds
    if len(clouds) < maxClouds:
        new_cloud = create_cloud(clouds)
        if is_valid_position(new_cloud, clouds):
            clouds.append(new_cloud)
            print(f"New cloud added at {new_cloud['x']}, {new_cloud['y']}")

    #update the cloud positions
    for cloud in clouds:
        cloud['x'] -= 5



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

    #rendering them clouds
    for cloud in clouds:
        screen.blit(cloud['image'], (cloud['x'], cloud['y']))

    # Flip the display
    pygame.display.flip()

    # Limit frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()






#THIS PERFECT FOR THE FISH AS THE CLOUDS IS BUT NOT FOR THEM CLOUDS SAVING FOR WHEN I MAKE FISH THO

# import pygame
# import sys
# import random

# #import cloud image
# cloud_image = pygame.image.load('C:\\Users\\Smg21\\OneDrive\\Desktop\\Pixel_Jam_Fish_Epidemik\\sprite_level_one\\cloud_sprite.png')
# # Initialize Pygame
# pygame.init()

# # Set up some constants
# WIDTH, HEIGHT = 640, 480
# FPS = 60

# # Create the game window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Fish Epidemik")

# # Create a surface for the water area
# water_surface = pygame.Surface((WIDTH, HEIGHT // 2), pygame.SRCALPHA)
# water_surface.fill((0, 0, 255, 128))  # Fill the water surface with semi-transparent dark blue
# #create deck area surface
# deck_surface = pygame.Surface((365, 50), pygame.SRCALPHA)
# deck_surface.fill((184,134,11))

# #List to hold them clouds
# clouds = []
# maxClouds = 10 #Max clouds in sky
# minDistanceBetweenClouds = 150 #min distance between any two clouds
# #Function to create the cloud objects 

# #some more cloud logics
# def is_valid_position(new_cloud, existing_clouds):
#     for cloud in existing_clouds:
#         if abs(new_cloud['x'] - cloud['x']) < minDistanceBetweenClouds:
#             return False
#     return True 
    
# def create_cloud(existing_clouds):
#     base_x = random.randint(WIDTH, WIDTH * 2) #base x coordinates starts them off screen
#     y = random.randint(HEIGHT // 2, HEIGHT - 100) #random y that is above the deck
#     #offset = random.randint(-100, 100) #random offsets between -100 and 100 px
#     #x = base_x + offset #final x coordinate w offset applied
#     return {'image': cloud_image, 'x': base_x, 'y': y} #0?

# #some clouds logic no more cloud snake 


# # Game loop
# running = True
# while running:

#     #we gotta remove them clouds that went off
#     clouds[:] = [cloud for cloud in clouds if cloud['x'] > -cloud_image.get_width()]

#     #Create the new clouds
#     if len(clouds) < maxClouds:
#         new_cloud = create_cloud(clouds)
#         if is_valid_position(new_cloud, clouds):
#             clouds.append(new_cloud)
#             print(f"New cloud added at {new_cloud['x']}, {new_cloud['y']}")

#     #update the cloud positions
#     for cloud in clouds:
#         cloud['x'] -= 5



#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # Add more event types here as needed

#     # Update game state
#     # Example: Move character, check collisions, etc.

    
#     # Render game state
#     screen.fill((70, 130, 180))  # Fill the screen with black color
#     screen.blit(water_surface, (0, HEIGHT // 2))  # Blit the water surface onto the main screen
#     screen.blit(deck_surface, (0, 200))  # Blit the water surface onto the main screen
#     # Draw game elements here

#     #rendering them clouds
#     for cloud in clouds:
#         screen.blit(cloud['image'], (cloud['x'], cloud['y']))

#     # Flip the display
#     pygame.display.flip()

#     # Limit frame rate
#     pygame.time.Clock().tick(FPS)

# # Quit Pygame
# pygame.quit()
# sys.exit()