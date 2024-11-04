from handle import *
block_size = 96

lv2_r3_blockFloor = [Block(6000+i*block_size, HEIGHT - block_size, block_size, 2, 1) for i in range(28)]
lv2_r3_fires = [Fire1(6200+i*50, 640, 16, 32) for i in range(10)]
    
lv2_r3_falling_platform1 = FallingPlatform(6400, -64, 32, 20)
lv2_r3_falling_platform2 = FallingPlatform(7148, -64, 32, 20)
lv2_r3_falling_platform3 = FallingPlatform(8570, -64, 32, 20)
lv2_r3_falling_platform4 = FallingPlatform(9300, -64, 32, 20)

lv2_r3_trampo = Trampoline(7640, HEIGHT - block_size-53, 28, 28, "Trampoline")
lv2_r3_trampo1 = Trampoline(9090, HEIGHT - block_size-53, 28, 28, "Trampoline")

lv2_r3_saw = [Saw(6865+i*58, 630, 38, 38, "Saw") for i in range(3)]
lv2_r3_sawtmp = [Saw(7750+i*77, 610, 38, 38, "Saw") for i in range(8)]

lv2_r3_block1  = Block(6768, HEIGHT - block_size * 2, block_size, 2, 1)
lv2_r3_block2  = Block(6768, HEIGHT - block_size * 6, block_size, 2, 1)
lv2_r3_block3  = Block(7152, HEIGHT - block_size * 4, block_size, 2, 1)
lv2_r3_block4  = Block(7056, HEIGHT - block_size * 2, block_size, 2, 1)
lv2_r3_block5  = Block(7152, HEIGHT - block_size * 2, block_size, 2, 1)
lv2_r3_block6  = Block(7152, HEIGHT - block_size * 3, block_size, 2, 1)
lv2_r3_block7  = Block(7248, HEIGHT - block_size * 2, block_size, 2, 1)
lv2_r3_block8  = Block(7248, HEIGHT - block_size * 3, block_size, 2, 1)
lv2_r3_block9  = Block(7248, HEIGHT - block_size * 4, block_size, 2, 1)
lv2_r3_block10 = Block(7248, HEIGHT - block_size * 5, block_size, 2, 1)
lv2_r3_block11 = Block(7248, HEIGHT - block_size * 6, block_size, 2, 1)
lv2_r3_block12 = Block(7248, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block13 = Block(7248, HEIGHT - block_size * 8, block_size, 2, 1)
lv2_r3_block14 = Block(7152, HEIGHT - block_size * 8, block_size, 2, 1)
lv2_r3_block15 = Block(8592, HEIGHT - block_size * 3, block_size, 2, 1)
lv2_r3_block16 = Block(8592, HEIGHT - block_size * 5, block_size, 2, 1)
lv2_r3_block17 = Block(8592, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block18 = Block(8688, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block19 = Block(8784, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block20 = Block(8880, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block21 = Block(9076, HEIGHT - block_size * 7, block_size, 2, 1)
lv2_r3_block22 = Block(9072, HEIGHT - block_size ,    block_size, 2, 1) 
lv2_r3_block23 = Block(9760, HEIGHT-block_size*5 ,    block_size, 2, 1) 

def lv2_3_loop():
    for i in lv2_r3_saw:
        i.on()

    for i in lv2_r3_sawtmp:
        i.on()

    for i in lv2_r3_fires:
        i.loop()

    lv2_r3_trampo.loop()
    lv2_r3_trampo1.loop()

    for i in lv2_r3_saw:
        i.loop()

    for i in lv2_r3_sawtmp:
        i.loop()