from obj import *

lv3_r1_block0 = Block(0, HEIGHT - block_size, block_size, 2, 0)
lv3_r1_block1 = Block(block_size * 9.35, HEIGHT - block_size * 5, block_size, 2, 0)
lv3_r1_block2 = Block(1300, HEIGHT - block_size * 5, block_size, 2, 0)
lv3_r1_block3 = Block(1400, HEIGHT - block_size * 5, block_size, 2, 0)
lv3_r1_block4 = Block(1800, HEIGHT - block_size * 5, block_size, 2, 0)
lv3_r1_block5 = Block(2000, HEIGHT - block_size * 5, block_size, 1, 0)

lv3_r1_saw_0 = Saw(block_size * 2.35 + 50  + 200, HEIGHT - block_size - 300, 38, 38, "Saw")
lv3_r1_saw_1 = Saw(block_size * 2.35 + 134 + 200, HEIGHT - block_size - 300, 38, 38, "Saw")
lv3_r1_saw_2 = Saw(block_size * 2.35 + 218 + 200, HEIGHT - block_size - 300, 38, 38, "Saw")
lv3_r1_saw_3 = Saw(block_size * 2.35 + 302 + 200, HEIGHT - block_size - 300, 38, 38, "Saw")
lv3_r1_saw_4 = Saw(block_size * 2.35 + 386 + 200, HEIGHT - block_size - 300, 38, 38, "Saw")  
lv3_r1_saw_5 = Saw(block_size * 2.35 + 50  + 200, HEIGHT - block_size - 600, 38, 38, "Saw")
lv3_r1_saw_6 = Saw(block_size * 2.35 + 134 + 200, HEIGHT - block_size - 600, 38, 38, "Saw")
lv3_r1_saw_7 = Saw(block_size * 2.35 + 218 + 200, HEIGHT - block_size - 600, 38, 38, "Saw")
lv3_r1_saw_8 = Saw(block_size * 2.35 + 302 + 200, HEIGHT - block_size - 600, 38, 38, "Saw")
lv3_r1_saw_9 = Saw(block_size * 2.35 + 386 + 200, HEIGHT - block_size - 600, 38, 38, "Saw")
lv3_r1_saw_10 = Saw(block_size * 9.35 + 300, HEIGHT - block_size * 5 - 80, 38, 38, "Saw")
lv3_r1_saw_10_x = int(-2)

lv3_r1_fallBlock_vel = int(0)

lv3_r1_saw_0.on()
lv3_r1_saw_1.on()
lv3_r1_saw_2.on()
lv3_r1_saw_3.on()
lv3_r1_saw_4.on()
lv3_r1_saw_5.on()
lv3_r1_saw_6.on()
lv3_r1_saw_7.on()
lv3_r1_saw_8.on()
lv3_r1_saw_9.on()
lv3_r1_saw_10.on()

lv3_r1_trampoline_00 = Trampoline(block_size, HEIGHT - block_size, 28, 28, "Trampoline")
lv3_r1_trampoline_01 = Trampoline(block_size * 2.35 + 150, HEIGHT - block_size - 500, 28, 28, "Trampoline")
lv3_r1_trampoline_02 = Trampoline(block_size * 2.35 + 250, HEIGHT - block_size - 670, 28, 28, "Trampoline")


def round1_loop():
    lv3_r1_trampoline_00.loop()
    lv3_r1_trampoline_01.loop()
    lv3_r1_trampoline_02.loop()

    lv3_r1_saw_0.loop()
    lv3_r1_saw_1.loop()
    lv3_r1_saw_2.loop()
    lv3_r1_saw_3.loop()
    lv3_r1_saw_4.loop()
    lv3_r1_saw_5.loop()
    lv3_r1_saw_6.loop()
    lv3_r1_saw_7.loop()
    lv3_r1_saw_8.loop()
    lv3_r1_saw_9.loop()  
    lv3_r1_saw_10.loop()

def round1_handle_move_obj(player):
    global lv3_r1_block3
    global lv3_r1_saw_10_x
    global lv3_r1_fallBlock_vel
    global offset_X, offset_y, offset_x_tmp
    if lv3_r1_saw_10.rect.x >= 1200 or lv3_r1_saw_10.rect.x <= 600:
        lv3_r1_saw_10_x *= -1
    if player.rect.x >= 1420: 
        lv3_r1_fallBlock_vel = 5
    
    lv3_r1_saw_10.rect.x += lv3_r1_saw_10_x
    lv3_r1_block3.rect.y += lv3_r1_fallBlock_vel

    if player.rect.x == 0:
        lv3_r1_fallBlock_vel = 0
        lv3_r1_block3.rect.y = HEIGHT - block_size * 5
        offset_x = 0
        offset_x_tmp = 0
        offset_y = 0