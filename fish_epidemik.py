import pygame
import sys
import random
import os  # To get file paths

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up file paths
current_directory = os.path.dirname(__file__)
sprite_directory = os.path.join(current_directory, 'sprite_level_one')

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fish Epidemik")

# Load images
cloud_image = pygame.image.load(os.path.join(sprite_directory, 'cloud_sprite.png'))

background_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'BACKGROUNDLEVELONE{i}.png'))
    for i in range(1, 7)
]

fishman_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'ACTUAL_FISH_MAN_SPRITEEEE_DRUID{i}.png'))
    for i in range(1, 5)
]

evil_fish_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'EVEN BETTER EVUL FISH{i}.png'))
    for i in range(1, 5)
]

purple_fish_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'PURPLE_FISH{i}.png'))
    for i in range(1, 9)
]

rainbow_gold_fish_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'rainbow_gold_fish{i}.png'))
    for i in range(1, 16)
]

clown_rainbow_fish_frames = [
    pygame.image.load(os.path.join(sprite_directory, f'clownrainbowfish{i}.png'))
    for i in range(1, 3)
]

# Function to scale frames
def scale_frames(frames, scale_factor):
    return [pygame.transform.scale(frame, (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor))) for frame in frames]

# Scale the frames
scale_factor = 3
fishman_frames = scale_frames(fishman_frames, scale_factor)
purple_fish_frames = scale_frames(purple_fish_frames, 2)
rainbow_gold_fish_frames = scale_frames(rainbow_gold_fish_frames, 2)
clown_rainbow_fish_frames = scale_frames(clown_rainbow_fish_frames, 2)
evil_fish_frames = scale_frames(evil_fish_frames, 2)

# Load custom fonts
menu_font = pygame.font.Font(os.path.join(current_directory, 'SuperPixel-m2L8j.ttf'), 36)
points_font = pygame.font.Font(os.path.join(current_directory, 'MinecraftBold-nMK1.otf'), 24)

# Define buttons
start_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 - 75, 400, 50)
exit_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 10, 400, 50)
htp_button = pygame.Rect(WIDTH / 2 - 200, HEIGHT / 2 + 95, 400, 50)
top_exit_button = pygame.Rect(WIDTH - 100, 10, 80, 30)
game_exit_button = pygame.Rect(WIDTH - 100, HEIGHT - 40, 80, 30)

# Function to draw the start menu
def draw_start_menu(screen):
    screen.fill((31, 81, 69))
    title_text = menu_font.render("Fish Epidemik", True, WHITE)
    start_text = menu_font.render("Start Game", True, WHITE)
    exit_text = menu_font.render("Exit Game", True, WHITE)
    htp_text = menu_font.render("How to Play", True, WHITE)
    pygame.draw.rect(screen, BLACK, start_button)
    pygame.draw.rect(screen, BLACK, exit_button)
    pygame.draw.rect(screen, BLACK, htp_button)
    screen.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, HEIGHT / 2 - 150))
    screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) / 2, start_button.y + (start_button.height - start_text.get_height()) / 2))
    screen.blit(exit_text, (exit_button.x + (exit_button.width - exit_text.get_width()) / 2, exit_button.y + (exit_button.height - exit_text.get_height()) / 2))
    screen.blit(htp_text, (htp_button.x + (htp_button.width - htp_text.get_width()) / 2, htp_button.y + (htp_button.height - htp_text.get_height()) / 2))

# Function to draw "How to Play" screen
def draw_htp_screen(screen):
    screen.fill((31, 81, 69))
    instructions = [
        "Click to fish!",
        "",
        "If you catch a purple fish you get 10 points,",
        "",
        "15 points for the gold fish",
        "",
        "20 points for the clown fish",
        "",
        "Evil Fish is -30 Points",
        "",
        "Try to reach 500 points to win the game!",
        "",
        "Good luck!"
    ]
    for i, line in enumerate(instructions):
        instruction_text = points_font.render(line, True, WHITE)
        screen.blit(instruction_text, (WIDTH / 2 - instruction_text.get_width() / 2, HEIGHT / 2 - 150 + i * 30))
    pygame.draw.rect(screen, RED, top_exit_button)
    exit_text = menu_font.render("Exit", True, WHITE)
    screen.blit(exit_text, (top_exit_button.x + (top_exit_button.width - exit_text.get_width()) / 2, top_exit_button.y + (top_exit_button.height - exit_text.get_height()) / 2))

# Function to draw additional messages
def draw_messages(screen, message, y_offset):
    message_text = points_font.render(message, True, WHITE)
    screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, 50 + y_offset))

# Function to draw points
def draw_points(screen, points):
    points_text = points_font.render(f"Points: {points}", True, BLACK)
    screen.blit(points_text, (WIDTH // 2 - points_text.get_width() // 2, 10))

# Game variables
points = 0
fish_caught = False
fish_timer = 0
fish_frame_index = 0
no_fish_caught = False
no_fish_timer = 0
click_to_fish = True
# Game variables (continued)
fish_choice = random.choice([purple_fish_frames, rainbow_gold_fish_frames, clown_rainbow_fish_frames])
fishman_position = (250, 241)

# Background animation variables
frame_index = 0
frame_delay = 8
frame_timer = 0

# Fishman animation variables
fishman_frame_index = 0
fishman_frame_delay = 10
fishman_frame_timer = 0

# Fish animation variables
fish_frame_delay = 10
fish_frame_timer = 0

# Main game loop
clock = pygame.time.Clock()
menu = True
showing_htp = False
win_message_shown = False  # Add this variable to track if the win message has been shown

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
                if game_exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                #HERE
                if not win_message_shown:
                    if not fish_caught and not no_fish_caught:
                        if random.randint(0, 6) == 0:
                            fish_caught = True
                            fish_timer = pygame.time.get_ticks()
                            fish_choice = evil_fish_frames  # Use the evil fish frames
                            points -= 30  # Deduct 30 points for catching the evil fish
                            fish_sound = pygame.mixer.Sound("wrong-answer-21-199825.mp3")  # Load the fish caught sound
                            fish_sound.play()  # Play the sound effect
                        else:
                            if random.randint(0, 1) == 0:
                                fish_caught = True
                                fish_timer = pygame.time.get_ticks()
                                fish_choice = random.choice([purple_fish_frames, rainbow_gold_fish_frames, clown_rainbow_fish_frames])
                                if fish_choice == purple_fish_frames:
                                    points += 10
                                elif fish_choice == rainbow_gold_fish_frames:
                                    points += 15
                                elif fish_choice == clown_rainbow_fish_frames:
                                    points += 20
                                fish_sound = pygame.mixer.Sound("collect-points-190037.mp3")  # Load the fish caught sound
                                fish_sound.play()  # Play the sound effect
                            else:
                                no_fish_caught = True
                                no_fish_timer = pygame.time.get_ticks()
                                # HERE
                                no_fish_sound = pygame.mixer.Sound("080047_lose_funny_retro_video-game-80925.mp3")  # Load the no fish caught sound
                                no_fish_sound.play()  # Play the sound effect
                    click_to_fish = False
            pygame.mixer.init()
            win_sound = pygame.mixer.Sound("congratulations-deep-voice-172193.mp3")
#Sound Effect CONGRATULATIONS by <a href="https://pixabay.com/users/voicebosch-30143949/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=172193">Otto</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=172193">Pixabay</a>
#Sound Effect COIN POINTS by <a href="https://pixabay.com/users/liecio-3298866/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190037">LIECIO</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=190037">Pixabay</a>
#Sound Effect WRONGANSWER by <a href="https://pixabay.com/users/audiosto-40753689/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=199825">Audiosto</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=199825">Pixabay</a>
#Sound Effect LOOSEFUNNY from <a href="https://pixabay.com/sound-effects/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=80925">Pixabay</a>
        if points >= 500:
            if not win_message_shown:
                screen.fill((31, 81, 69))
                win_message_shown = True
                draw_messages(screen, "You Will Now Return To The Main Menu!", 60)
                draw_messages(screen, "You Won!", 10)
                draw_messages(screen, "Thank You For Playing My First Game!", 40)
                # Play the winning sound effect
                win_sound.play()
                pygame.display.flip()
                pygame.time.wait(3000)  # Display the win message for 3 seconds
                menu = True  # Return to the main menu
                points = 0  # Reset points for the next game
                click_to_fish = True
                fish_caught = False
                no_fish_caught = False
                win_message_shown = False

    if menu:
        draw_start_menu(screen)
    elif showing_htp:
        draw_htp_screen(screen)
    else:
        screen.fill(WHITE)

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

        # Fish catching animation
        if fish_caught:
            current_time = pygame.time.get_ticks()
            if current_time - fish_timer < 1000:
                fish_frame_timer += 1
                if fish_frame_timer >= fish_frame_delay:
                    fish_frame_timer = 0
                    fish_frame_index = (fish_frame_index + 1) % len(fish_choice)
                if fish_frame_index < len(fish_choice):
                    screen.blit(fish_choice[fish_frame_index], (350, 275))
                draw_messages(screen, "Fish Caught!", 50)
            else:
                fish_caught = False
                click_to_fish = True
        elif no_fish_caught:
            current_time = pygame.time.get_ticks()
            if current_time - no_fish_timer < 1000:
                draw_messages(screen, "No Fish Caught!", 50)
            else:
                no_fish_caught = False
                click_to_fish = True
        if not win_message_shown and not fish_caught and not no_fish_caught:
            draw_messages(screen, "Click to Fish!", 50)

        # Draw points
        draw_points(screen, points)

        # Draw game exit button
        exit_button_surface = pygame.Surface((game_exit_button.width, game_exit_button.height), pygame.SRCALPHA)
        exit_button_surface.fill((255, 0, 0, 128))  # Semi-transparent red
        screen.blit(exit_button_surface, game_exit_button.topleft)
        exit_text = points_font.render("Exit", True, BLACK)
        screen.blit(exit_text, (game_exit_button.x + (game_exit_button.width - exit_text.get_width()) / 2, game_exit_button.y + (game_exit_button.height - exit_text.get_height()) / 2))

    pygame.display.flip()
    clock.tick(FPS)
