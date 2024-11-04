from level3_round2 import *


block06 = Block(4000, HEIGHT - block_size, block_size, 0, 0)
block07 = Block(4000 + block_size * 4, HEIGHT - block_size * 2.5, block_size, 0, 0)
block08 = Block(4000 + block_size * 8, HEIGHT - block_size * 4.5, block_size, 0, 0)
block09 = Block(4000 + block_size * 4, HEIGHT - block_size * 6.5, block_size, 0, 0)
block10 = Block(4000 + block_size * 8, HEIGHT - block_size * 8.5, block_size, 0, 0)
block11 = Block(4000 + block_size * 4, HEIGHT - block_size * 10.5, block_size, 0, 0)
block12 = Block(4000 + block_size * 8, HEIGHT - block_size * 12.5, block_size, 0, 0)
block13 = Block(4000 + block_size * 4, HEIGHT - block_size * 14.5, block_size, 0, 0)
block14 = Block(4000 + block_size * 8 - 60 + 96, HEIGHT - block_size * 16.5, block_size, 0, 0)
block15 = Block(4000 + block_size * 8 - 60 + 96 * 2, HEIGHT - block_size * 16.5, block_size, 0, 0)
block16 = Block(4000 + block_size * 8 - 60 + 96 * 3, HEIGHT - block_size * 16.5, block_size, 0, 0)
block17 = Block(4000 + block_size * 8 - 60 + 96 * 4, HEIGHT - block_size * 16.5, block_size, 0, 0)
block18 = Block(4000 + block_size * 8 - 60 + 96 * 5, HEIGHT - block_size * 16.5, block_size, 0, 0)
block19 = Block(4000 + block_size * 8 - 60 + 96 * 6, HEIGHT - block_size, block_size, 0, 0)
block20 = Block(4000 + block_size * 8 - 60 + 96 * 10.5, HEIGHT - block_size * 2.5, block_size, 0, 0)
block21 = Block(4000 + block_size * 8 - 60 + 96 * 16.5, HEIGHT - block_size * 10, block_size, 0, 0)
block22 = Block(4000 + block_size * 8 - 60 + 96 * 17.5, HEIGHT - block_size * 10, block_size, 0, 0)
block23 = Block(4000 + block_size * 8 - 60 + 96 * 18.5, HEIGHT - block_size * 10, block_size, 0, 0)
block24 = Block(4000 + block_size * 8 - 60 + 96 * 19.5, HEIGHT - block_size * 10, block_size, 0, 0)
block25 = Block(4000 + block_size * 8 - 60 + 96 * 20.5, HEIGHT - block_size * 10, block_size, 0, 0)
block26 = Block(7000 - 96, HEIGHT - block_size * 10, block_size, 0, 0)

blockks = []
blockks.append(block07.rect.y)
blockks.append(block08.rect.y)
blockks.append(block09.rect.y)
blockks.append(block10.rect.y)
blockks.append(block11.rect.y)
blockks.append(block12.rect.y)
blockks.append(block13.rect.y)

handle_fall_block = []
handle_fall_block.append(block07)
handle_fall_block.append(block08)
handle_fall_block.append(block09)
handle_fall_block.append(block10)
handle_fall_block.append(block11)
handle_fall_block.append(block12)
handle_fall_block.append(block13)

obj_saw_19 = Saw(7000 - 96 * 2 - 8, HEIGHT - block_size * 10 + 8, 38, 38, "Saw")
obj_saw_19_y = int(20)
obj_saw_19.on()

obj_trampoline_04 = Trampoline(4000 + block_size * 8 - 60 + 96 * 11, HEIGHT - block_size * 6 , 28, 28, "Trampoline")

def round3_handle_move_obj():
    global obj_saw_19_y 
    global background00, bg_image_00
    global background01, bg_image_01
    global background02, bg_image_02
    if obj_saw_19.rect.y <= HEIGHT - block_size * 12 or obj_saw_19.rect.y >= HEIGHT - block_size * 10:
        obj_saw_19_y *= -1

    obj_saw_19.rect.y += obj_saw_19_y
    

def round3_loop():
    obj_saw_19.loop()
    obj_trampoline_04.loop()