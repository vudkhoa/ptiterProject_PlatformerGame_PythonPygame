import pygame
import button
from raw_object import *


pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

back_img = pygame.image.load('assets/images_menu/button_back.png').convert_alpha()
back_button = button.Button((WIDTH - back_img.get_width()) // 2, 450, back_img, 1)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)

bg_volume = 0.5

slider_x = 200
slider_y = 400
slider_width = 600
slider_height = 10
slider_knob_radius = 15
slider_knob_x = slider_x + bg_volume * slider_width


def draw_volume_slider(window, volume):
   
    pygame.draw.rect(window, GREY, (slider_x, slider_y, slider_width, slider_height))
    
    knob_x = slider_x + volume * slider_width
    pygame.draw.circle(window, RED, (int(knob_x), slider_y + slider_height // 2), slider_knob_radius)

    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Volume: {int(volume * 100)}%', True, BLACK)
    window.blit(text, (slider_x, slider_y - 40))


def play_bg_music(music_file):
    pygame.mixer.init()
    
    pygame.mixer.music.load(music_file)
    
    pygame.mixer.music.play(-1)
    

bg,bg_img = get_bg_login("Yellow.png")
def BG_VOLUME():
    global bg_volume
    running = True
    
    while running:
        
        draw_bg_login(window,bg,bg_img)
        draw_volume_slider(window, bg_volume)
        
        if(back_button.draw(window)):
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    # Kiểm tra xem con trỏ có đang trong phạm vi của thanh trượt không
                    if (slider_x <= mouse_x <= slider_x + slider_width and
                slider_y <= mouse_y <= slider_y + slider_height):
                        # Cập nhật vị trí của nút trượt dựa trên vị trí chuột
                        bg_volume = (mouse_x - slider_x) / slider_width
                        
                        # Giới hạn âm lượng trong khoảng 0.0 - 1.0
                        bg_volume = max(0, min(1, bg_volume))
                        
                    pygame.mixer.music.set_volume(bg_volume)
                        

        pygame.display.update()
        
    return True