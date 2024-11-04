import os
import pygame
import math

from os import listdir
from os.path import isfile, join
WIDTH, HEIGHT = 1000, 800
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

block_x = 96
block_y = 96 * 2 / 3

enemy_x = 32
enemy_y = 32 * 2 / 3

# Lật hình 
def flip(sprites): 
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

# Tải nhân vậtza
def load_sprite_sheets(dir1, dir2, width, height, direction = False):
    # Đường dẫn
    path = join("assets", dir1, dir2)
    # Lấy hình dạng 
    # listdir(path): Lấy tất cả các tệp
    # isfile(join(path, f)): là hình ảnh
    images = [f for f in listdir(path) if isfile(join(path, f))]

    # Lưu vào sheets
    all_sprites = {}

    for image in images:
        # load sheet hình ảnh
        sprite_sheets = pygame.image.load(join(path, image)).convert_alpha()

        # Tạo ds rỗng
        sprites = []

        # sprite_sheets.get_width(): chiều rộng của sprite
        # width: chiều rộng muốn cắt
        # Tính số lượng prite cần có
        for i in range(sprite_sheets.get_width() // width):
            # pygame.Surface(width, height): tạo surface có kích thước
            # Chuyển kênh dùng được độ trong suốt 
            # 32: color depth
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            # Tạo dãy ô vuông theo width cần có
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheets, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction: 
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else: 
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites

def get_block(size, xBlock, yBlock):
    path = join("assets", "Terrain", "Terrain.png")
    # covert_alpha: Tối ưu hóa hình ảnh để hỗ trợ độ trong suốt
    #               Giúp game chạy mượt + hiển thị hình ảnh nhiều lần
    image = pygame.image.load(path).convert_alpha()
    # (size, size): Tạo bề mặt vs kích thước -> width, height: size
    # pygame.SRCALPHA: vẽ các hình ảnh or color with độ trong suốt #
    # 32: Độ sâu của màu 
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    # rect: xác định vị trí + kích thước
    rect = pygame.Rect(yBlock * block_x, xBlock * block_y, size, size)
    # .blit:    vẽ
    # image:    Hình ảnh muốn vẽ
    # (0, 0):   tọa độ vẽ lên surface
    # rect:     vẽ phần xác định bởi hcn       
    surface.blit(image, (0, 0), rect)
    # phóng to surface
    return pygame.transform.scale2x(surface)

