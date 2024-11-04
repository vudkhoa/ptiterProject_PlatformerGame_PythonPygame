import pygame
import random
from login import *
from menu import play_bg_music


pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("End Game Screen")


WHITE = (255, 255, 255)
FIREWORK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
font_large = pygame.font.Font(None, 80)
font_small = pygame.font.Font(None, 50)


congrat_text = font_large.render("CONGRATULATION", True, WHITE)
author_text = font_small.render("Author: Thien, Khoa, Khanh", True, WHITE)


center_x = screen.get_width() // 2
center_y = screen.get_height() // 2


def draw_fireworks():
    for _ in range(50):
        x = random.randint(center_x - 200, center_x + 200)
        y = random.randint(center_y - 200, center_y + 200)
        color = random.choice(FIREWORK_COLORS)
        pygame.draw.circle(screen, color, (x, y), random.randint(2, 5))


def run_end_screen(go):
    clock = pygame.time.Clock()
    running = go
    show_author = False
    time_next = pygame.USEREVENT
    time_end  = pygame.USEREVENT + 1

    pygame.time.set_timer(time_next, 1000) 
    pygame.time.set_timer(time_end, 8000) 

    play_bg_music('assets/music/sound_end_game.mp3')

    while running:
        screen.fill((0, 0, 0))  #Black
        screen.blit(congrat_text, congrat_text.get_rect(center=(center_x, center_y)))
        
        if not show_author:
            draw_fireworks()
        
        pygame.display.flip()
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == time_next:
                show_author = True
            elif event.type == time_end:
                pygame.mixer.music.stop()
                running = False
                break

        if show_author:
            screen.fill((0, 0, 0))  # Làm mới màn hình
            screen.blit(congrat_text, congrat_text.get_rect(center=(center_x, center_y)))
            screen.blit(author_text, author_text.get_rect(center=(center_x, center_y + 100)))
            pygame.display.flip()
            pygame.time.delay(100)

        clock.tick(30)

