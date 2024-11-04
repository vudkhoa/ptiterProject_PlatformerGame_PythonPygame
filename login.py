import pygame
import button
from os.path import isfile, join
from raw_object import *
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Login Screen")

font = pygame.font.SysFont("arialblack", 30)
input_font = pygame.font.SysFont("arial", 32)
TEXT_COL = (255, 255, 255)
INPUT_BOX_COLOR = (0, 0, 0)
ACTIVE_INPUT_BOX_COLOR = (255, 255, 255)

play_img = pygame.image.load("assets/Menu/Buttons/Play.png").convert_alpha()
play_button = button.Button(470, 580, play_img, 3)

input_box = pygame.Rect(350, 400, 300, 50)  # Input box for username
input_box_2 = pygame.Rect(350, 500, 300, 50)  # Input box for password

active_input_box = None  # Variable to keep track of which input box is active
username = ''
password = ''  # Variable to store password input

def login_screen():
    global active_input_box, username, password
    
    background, bg_image = get_bg_login("Gray.png")
        
    run = True
    while run:       
        draw_bg_login(window, background, bg_image)
        draw_text_login("Enter username:", font, TEXT_COL, 370, 350)
        draw_text_login("Enter password:", font, TEXT_COL, 370, 450)
        
        # Draw input box for username
        color = ACTIVE_INPUT_BOX_COLOR if active_input_box == input_box else INPUT_BOX_COLOR
        pygame.draw.rect(window, color, input_box, 2)
        text_surface = input_font.render(username, True, TEXT_COL)
        window.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        input_box.w = max(300, text_surface.get_width() + 40)

        # Draw input box for password
        color = ACTIVE_INPUT_BOX_COLOR if active_input_box == input_box_2 else INPUT_BOX_COLOR
        pygame.draw.rect(window, color, input_box_2, 2)
        password_surface = input_font.render('*' * len(password), True, TEXT_COL)  # Hide password with '*'
        window.blit(password_surface, (input_box_2.x + 10, input_box_2.y + 10))
        input_box_2.w = max(300, password_surface.get_width() + 40)

        # Draw play button
        if play_button.draw(window):
            return username, password

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return "None", "None"

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if user clicked inside the input boxes
                if input_box.collidepoint(event.pos):
                    active_input_box = input_box
                elif input_box_2.collidepoint(event.pos):
                    active_input_box = input_box_2
                else:
                    active_input_box = None

            if event.type == pygame.KEYDOWN:
                if active_input_box == input_box:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_input_box == input_box_2:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.update()
