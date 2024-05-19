import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Epidemik")

# Load cloud image
cloud_image = pygame.image.load('C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/cloud_sprite.png')

# Load background frames
background_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE2.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE3.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE4.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE5.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/BACKGROUNDLEVELONE6.png')
]

# Load Fishman frames
fishman_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/ACTUAL_FISH_MAN_SPRITEEEE_DRUID1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/ACTUAL_FISH_MAN_SPRITEEEE_DRUID2.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/ACTUAL_FISH_MAN_SPRITEEEE_DRUID3.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/ACTUAL_FISH_MAN_SPRITEEEE_DRUID4.png')
]

# Scale factor
scale_factor = 3  # Adjust this factor to change the size of the Fishman

# Scale the Fishman frames
fishman_frames = [
    pygame.transform.scale(frame, (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor)))
    for frame in fishman_frames
]

# Background animation variables
frame_index = 0
frame_delay = 8  # Adjust the delay to control the speed of the animation
frame_timer = 0

# Fishman animation variables
fishman_frame_index = 0
fishman_frame_delay = 10  # Adjust the delay to control the speed of the Fishman animation
fishman_frame_timer = 0
fishman_position = (250, 241)  # Adjust this position as needed

# Load fish images for animation
purple_fish_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH2.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH3.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH4.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH5.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH6.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH7.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/PURPLE_FISH8.png')
]

rainbow_gold_fish_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish2.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish3.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish4.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish5.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish6.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish7.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish8.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish9.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish10.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish11.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish12.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish13.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish14.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/rainbow_gold_fish15.png')
]

clown_rainbow_fish_frames = [
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/clownrainbowfish1.png'),
    pygame.image.load(r'C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/sprite_level_one/clownrainbowfish2.png')
]

# Function to scale fish frames
def scale_fish_frames(fish_frames, scale_factor=2):
    return [
        pygame.transform.scale(frame, (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor)))
        for frame in fish_frames
    ]

# Scale the fish frames
purple_fish_frames = scale_fish_frames(purple_fish_frames)
rainbow_gold_fish_frames = scale_fish_frames(rainbow_gold_fish_frames)
clown_rainbow_fish_frames = scale_fish_frames(clown_rainbow_fish_frames)

# Load custom font for title and buttons
custom_font = pygame.font.Font('C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/SuperPixel-m2L8j.ttf', 36)
points_font = pygame.font.Font('C:/Users/Smg21/OneDrive/Desktop/Pixel_Jam_Fish_Epidemik/SuperPixel-m2L8j.ttf', 24)

# Define buttons globally so they can be accessed in the game loop
start_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 - 75, 400, 50)
exit_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 10, 400, 50)
htp_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 95, 400, 50)
top_exit_button = pygame.Rect(WIDTH - 100, 10, 80, 30)  # Exit button at the top

# Function to draw the start menu
def draw_start_menu(screen):
    screen.fill((31, 81, 69))  # Clear the screen with a background color
    title_text = custom_font.render("Fish Epidemik", True, WHITE)
    start_text = custom_font.render("Start Game", True, WHITE)
    exit_text = custom_font.render("Exit Game", True, WHITE)
    htp_text = custom_font.render("How to Play", True, WHITE)
    pygame.draw.rect(screen, RED, start_button)
    pygame.draw.rect(screen, RED, exit_button)
    pygame.draw.rect(screen, RED, htp_button)
    screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, HEIGHT / 2 - 150))
    screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) / 2, start_button.y + (start_button.height - start_text.get_height()) / 2))
    screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) / 2, exit_button.y + (exit_button.height - exit_text.get_height()) / 2))
    screen.blit(htp_text, (htp_button.x + (htp_button.width - htp_text.get_width()) / 2, htp_button.y + (htp_button.height - htp_text.get_height()) / 2))

# Define game variables
points = 0
fish_caught = False
fish_timer = 0
fish_frame_index = 0
no_fish_caught = False
no_fish_timer = 0
click_to_fish = True
fish_choice = random.choice([purple_fish_frames, rainbow_gold_fish_frames, clown_rainbow_fish_frames])

# Function to draw "How to Play" screen
def draw_htp_screen(screen):
    screen.fill((31, 81, 69))  # Clear the screen with a background color
    instructions = [
        "Click to fish!",
        "If you catch a fish, you get points.",
        "Purple Fish: 10 points",
        "Rainbow Clown Fish: 15 points",
        "Rainbow Gold Fish: 20 points",
        "Try to reach 500 points to win the game!",
        "Good luck!"
    ]
    for i, line in enumerate(instructions):
        instruction_text = custom_font.render(line, True, WHITE)
        screen.blit(instruction_text, (WIDTH / 2 - instruction_text.get_width() / 2, HEIGHT / 2 - 150 + i * 30))
    # Draw the exit button
    pygame.draw.rect(screen, RED, top_exit_button)
    exit_text = custom_font.render("Exit", True, WHITE)
    screen.blit(exit_text, (top_exit_button.x + (top_exit_button.width - exit_text.get_width()) / 2, top_exit_button.y + (top_exit_button.height - exit_text.get_height()) / 2))

# Function to draw points
def draw_points(screen, points):
    points_text = points_font.render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (WIDTH // 2 - points_text.get_width() // 2, 10))

# Function to draw additional messages
def draw_messages(screen, message, y_offset):
    message_text = points_font.render(message, True, BLACK)
    screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 50 + y_offset))

# Game loop
clock = pygame.time.Clock()
menu = True
showing_htp = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if menu:
                if start_button.collidepoint(event.pos):
                    menu = False
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif htp_button.collidepoint(event.pos):
                    showing_htp = True
                    menu = False
            elif showing_htp:
                if top_exit_button.collidepoint(event.pos):
                    showing_htp = False
                    menu = True
            else:
                if not fish_caught and not no_fish_caught:
                    if random.randint(0, 1) == 0:
                        fish_caught = True
                        fish_timer = pygame.time.get_ticks()
                        fish_choice = random.choice([purple_fish_frames, rainbow_gold_fish_frames, clown_rainbow_fish_frames])
                        if fish_choice == purple_fish_frames:
                            points += 10
                        elif fish_choice == rainbow_gold_fish_frames:
                            points += 20
                        elif fish_choice == clown_rainbow_fish_frames:
                            points += 15
                    else:
                        no_fish_caught = True
                        no_fish_timer = pygame.time.get_ticks()
                click_to_fish = False

    if menu:
        draw_start_menu(screen)
    elif showing_htp:
        draw_htp_screen(screen)
    else:
        screen.fill(WHITE)  # Clear the screen with white background

        # Background animation
        screen.blit(background_frames[frame_index], (0, 0))
        frame_timer += 1
        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(background_frames)

        # Fishman animation
        screen.blit(fishman_frames[fishman_frame_index], fishman_position)
        fishman_frame_timer += 1
        if fishman_frame_timer >= fishman_frame_delay:
            fishman_frame_timer = 0
            fishman_frame_index = (fishman_frame_index + 1) % len(fishman_frames)

        draw_points(screen, points)

        # Fish animation
        if fish_caught:
            fish_frame_index = (pygame.time.get_ticks() - fish_timer) // 100 % len(fish_choice)
            screen.blit(fish_choice[fish_frame_index], (350, 300))
            if pygame.time.get_ticks() - fish_timer > 1000:
                fish_caught = False

        # Display messages
        if click_to_fish:
            draw_messages(screen, "Click to fish!!", 0)
        if no_fish_caught:
            draw_messages(screen, "No Fish Caught", 20)
            if pygame.time.get_ticks() - no_fish_timer > 1000:
                no_fish_caught = False

        # Draw exit button at top right
        pygame.draw.rect(screen, RED, top_exit_button)
        exit_text = custom_font.render("Exit", True, WHITE)
        screen.blit(exit_text, (top_exit_button.x + (top_exit_button.width - exit_text.get_width()) / 2, top_exit_button.y + (top_exit_button.height - exit_text.get_height()) / 2))

        # Check for win condition
        if points >= 500:
            draw_messages(screen, "Congrats You Win!", 40)
            pygame.display.flip()
            pygame.time.wait(3000)  # Display the win message for 3 seconds
            menu = True  # Return to the main menu
            points = 0  # Reset points for the next game
            click_to_fish = True
            fish_caught = False
            no_fish_caught = False

    pygame.display.flip()
    clock.tick(FPS)


