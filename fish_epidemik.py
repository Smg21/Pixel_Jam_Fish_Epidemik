import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Load cloud image
cloud_image = pygame.image.load('C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/cloud_sprite.png')

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Epidemik")

# List to hold clouds
clouds = []
maxClouds = 20
minDistanceBetweenClouds = 90

# Load background frames
background_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE2.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE3.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE4.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE5.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE6.png')
]

# Background animation variables
frame_index = 0
frame_delay = 5  # Adjust the delay to control the speed of the animation
frame_timer = 0

# Function to create cloud objects
def create_cloud(existing_clouds):
    base_x = random.randint(WIDTH, WIDTH * 2)
    y = random.randint(HEIGHT // 14, HEIGHT - 390)
    return {'image': cloud_image, 'x': base_x, 'y': y}

# Function to check if a new cloud position is valid
def is_valid_position(new_cloud, existing_clouds):
    for cloud in existing_clouds:
        if abs(new_cloud['x'] - cloud['x']) < minDistanceBetweenClouds:
            return False
    return True

# Load custom font for title and buttons
custom_font = pygame.font.Font('C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/SuperPixel-m2L8j.ttf', 36)

# Define buttons globally so they can be accessed in the game loop
start_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 - 75, 400, 50)
exit_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 10, 400, 50)
htp_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 95, 400, 50)

# Function to draw the start menu
def draw_start_menu(screen):
    screen.fill((31, 81, 69))  # Clear the screen with a background color
    title_text = custom_font.render("Fish Epidemik", True, (240, 248, 255))
    title_rect = title_text.get_rect(center=(WIDTH / 2, HEIGHT / 4))
    screen.blit(title_text, title_rect)

    # Draw buttons with outlines
    pygame.draw.rect(screen, (240, 248, 255), start_button, width=4)  # Outline
    pygame.draw.rect(screen, (240, 248, 255), exit_button, width=4)  # Outline
    pygame.draw.rect(screen, (240, 248, 255), htp_button, width=4)  # Outline

    # Draw button texts using the custom font and adjust their positions
    start_text = custom_font.render("Start", True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=start_button.center)
    start_text_rect.x += start_button.width // 27  # Adjust horizontally to the left
    start_text_rect.y += start_button.height // 27  # Adjust vertically upwards
    screen.blit(start_text, start_text_rect.topleft)

    exit_text = custom_font.render("Exit", True, (255, 255, 255))
    exit_text_rect = exit_text.get_rect(center=exit_button.center)
    exit_text_rect.x += exit_button.width // 24  # Adjust horizontally to the left
    exit_text_rect.y += exit_button.height // 24  # Adjust vertically upwards
    screen.blit(exit_text, exit_text_rect.topleft)

    htp_text = custom_font.render("How to Play", True, (255, 255, 255))
    htp_text_rect = htp_text.get_rect(center=htp_button.center)
    htp_text_rect.x += htp_button.width // 30  # Adjust horizontally to the left
    htp_text_rect.y += htp_button.height // 30  # Adjust vertically upwards
    screen.blit(htp_text, htp_text_rect.topleft)

# Main game loop
running = True
menu_active = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if menu_active:
                if start_button.collidepoint(mouse_pos):
                    menu_active = False
                elif exit_button.collidepoint(mouse_pos):
                    running = False
                elif htp_button.collidepoint(mouse_pos):
                    # TODO: Implement how to play instructions
                    pass

    if menu_active:
        draw_start_menu(screen)
    else:
        # Clear clouds that moved off-screen
        clouds[:] = [cloud for cloud in clouds if cloud['x'] > -cloud_image.get_width()]

        # Create new clouds if needed
        if len(clouds) < maxClouds:
            new_cloud = create_cloud(clouds)
            if is_valid_position(new_cloud, clouds):
                clouds.append(new_cloud)

        # Move clouds
        for cloud in clouds:
            cloud['x'] -= 1

        # Update background frame
        frame_timer += 1
        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(background_frames)

        # Render current background frame
        screen.blit(background_frames[frame_index], (0, 0))

        # Render clouds
        for cloud in clouds:
            screen.blit(cloud['image'], (cloud['x'], cloud['y']))

    pygame.display.flip()
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