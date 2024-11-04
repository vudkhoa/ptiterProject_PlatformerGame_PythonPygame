import pygame
import button
from raw_object import *
from bg_volume import *
pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# define fonts
font = pygame.font.SysFont("arialblack", 40)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)

# load button images
resume_img = pygame.image.load("assets/images_menu/button_resume.png").convert_alpha()
options_img = pygame.image.load("assets/images_menu/button_options.png").convert_alpha()
quit_img = pygame.image.load("assets/images_menu/button_quit.png").convert_alpha()
video_img = pygame.image.load('assets/images_menu/button_video.png').convert_alpha()
audio_img = pygame.image.load('assets/images_menu/button_audio.png').convert_alpha()
keys_img = pygame.image.load('assets/images_menu/button_keys.png').convert_alpha()
back_img = pygame.image.load('assets/images_menu/button_back.png').convert_alpha()
restart_img = pygame.image.load("assets/Menu/Buttons/Restart.png").convert_alpha()
continue_img = pygame.image.load("assets/Menu/Buttons/Next.png")


# Create the Menu class
class Menu:
    def __init__(self, window):
        self.window = window
        self.game_paused = False
        self.menu_state = "main"
        self.run_menu = False
        self.quit_pressed = False
        # Load background
        self.bg, self.bg_img = get_bg_login("Yellow.png")
        
        # Create button instances with centered x position
        self.resume_button = button.Button((SCREEN_WIDTH - resume_img.get_width()) // 2, 125 + 100, resume_img, 1)
        self.options_button = button.Button((SCREEN_WIDTH - options_img.get_width()) // 2, 250 + 100, options_img, 1)
        self.quit_button = button.Button((SCREEN_WIDTH - quit_img.get_width()) // 2, 375 + 100, quit_img, 1)
        self.video_button = button.Button((SCREEN_WIDTH - video_img.get_width()) // 2, 75 + 100, video_img, 1)
        self.audio_button = button.Button((SCREEN_WIDTH - audio_img.get_width()) // 2, 200 + 100, audio_img, 1)
        self.keys_button = button.Button((SCREEN_WIDTH - keys_img.get_width()) // 2, 325 + 100, keys_img, 1)
        self.back_button = button.Button((SCREEN_WIDTH - back_img.get_width()) // 2, 450 + 100, back_img, 1)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.window.blit(img, (x, y))
    
    def update(self):
        draw_bg_login(self.window, self.bg, self.bg_img)

        if self.menu_state == "main":
            if self.resume_button.draw(self.window):
                return False
            if self.options_button.draw(self.window):
                self.menu_state = "options"
            if self.quit_button.draw(self.window):
                self.quit_pressed = True
                return False

        elif self.menu_state == "options":
            # if self.video_button.draw(self.window):
            #     print("Video Settings")
            if self.audio_button.draw(self.window):
                if not BG_VOLUME():
                    self.menu_state == "main"

            # if self.keys_button.draw(self.window):
            #     print("Change Key Bindings")
            if self.back_button.draw(self.window):
                self.menu_state = "main"

        return True  # Continue running the menu

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False  # Exit the menu

        return True  # Continue running
    
    def loop(self):
        
        while self.run_menu:
            for event in pygame.event.get():
                if not self.handle_event(event):   
                    return False
                
                if not self.update():
                    return False
                
                pygame.display.update()
            
        return True
class Menu_play:
    def __init__(self, window):
        self.window = window
        self.run_menu = False
        self.menu_state = "main"
        self.quit_pressed = False
        self.bg, self.bg_img = get_bg_login("Yellow.png")
        self.click = ""

        self.restart_button = button.Button(((SCREEN_WIDTH - restart_img.get_width()) // 2) - 50, 275, restart_img,5)
        self.continue_button = button.Button(((SCREEN_WIDTH - restart_img.get_width()) // 2) - 50, 400, continue_img,5)
        
    def update(self):
        draw_bg_login(self.window, self.bg, self.bg_img)
        
        if self.menu_state == "main":
            if self.restart_button.draw(self.window):
                self.click = "restart"
                return False
            if self.continue_button.draw(self.window):
                self.quit_pressed = True
                return False
            
        
        return True
    
    def handle_event(self,event):
        if event.type == pygame.QUIT:
            return False
        return True
    
    def loop(self):
        while self.run_menu:
            for event in pygame.event.get():
                if not self.handle_event(event):
                    return False, "quit"
                
                if not self.update():
                    return False, ""
                
                pygame.display.update()
            self.update()
            pygame.display.update()

        return True, ""