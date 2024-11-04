from handle import *
block_size = 96

lv2_r2_trampo = Trampoline(3640 + 84 * 2 + 120 * 2, HEIGHT - block_size * 3 - 50, 28, 28, "Trampoline")
lv2_r2_saw = [Saw(5250 + i * 77, 610, 38, 38, "Saw") for i in range(3)]
lv2_r2_fire = Fire1(3435, HEIGHT - block_size * 5 - 63, 16, 32)

lv2_r2_block1 = Block(3200, HEIGHT - block_size*3, block_size, 1, 1)
lv2_r2_block2 = Block(3400, HEIGHT - block_size*5, block_size, 1, 1)
lv2_r2_block3 = Block(3700, HEIGHT - block_size*3, block_size, 1, 1)
lv2_r2_block4 = Block(4700, HEIGHT - block_size*6, block_size, 1, 1)
lv2_r2_block5 = Block(5150, HEIGHT - block_size*2, block_size, 1, 1)
lv2_r2_block6 = Block(5485, HEIGHT - block_size*2, block_size, 1, 1)

lv2_r2_falling_platform1 = FallingPlatform(3350, -64, 32, 20)
lv2_r2_falling_platform2 = FallingPlatform(3900, -64, 32, 20)
lv2_r2_falling_platform3 = FallingPlatform(5700, -64, 32, 20)

def lv2_2_loop():
    for i in lv2_r2_saw:
        i.on()

    lv2_r2_fire.loop()
    lv2_r2_trampo.loop()

    for i in lv2_r2_saw:
        i.loop()