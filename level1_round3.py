from raw_object import *
#:)))
block_size = 96
start_x = 5870

lv1_r3_blockFloor1 = [Block(start_x + i * block_size, HEIGHT - block_size, block_size, 1, 0)
            for i in range(3)]

lv1_r3_blockFloor2 = [Block(start_x + (288 + 128) + 128 * 14 + i * block_size, HEIGHT - block_size, block_size, 1, 0)
            for i in range(8)]

lv1_r3_obstacle1 = [Block(start_x + 288 + 128,               HEIGHT - block_size * 2, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 2,   HEIGHT - block_size * 4, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 1.25,HEIGHT - block_size * 8, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 4,   HEIGHT - block_size * 6, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 5.5, HEIGHT - block_size + 96, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 7.5, HEIGHT - block_size, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 9.5, HEIGHT - block_size, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 7,   HEIGHT - block_size * 6, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 9,   HEIGHT - block_size * 4, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 11.5,HEIGHT - block_size * 2, block_size, 1, 0),
                Block(start_x + 192, HEIGHT - block_size * 4, block_size, 1, 0),
                Block(start_x + (288 + 128) + 128 * 14 + 20, HEIGHT - block_size * 4, block_size, 1, 0)
]

lv1_r3_obstacle2 = [Block(start_x + (288 + 128) + 128 * 14 + i * block_size, HEIGHT - block_size * 8, block_size, 1, 0)
                for i in range(6)]

lv1_r3_fire =  [Fire_lv1(start_x + (288 + 128) + 128 * 2 + 30, HEIGHT - block_size - 64 - 96 * 3, 16, 32, '0'), 
                Fire_lv1(start_x + (288 + 128) + 128 * 9 + 30, HEIGHT - block_size - 64 - 96 * 3, 16, 32, '0')]

lv1_r3_fireFloor = [Fire_lv1(start_x + (288 + 128) + 128 * 14 - 30 + 30 * i, HEIGHT - block_size - 64, 16, 32, '0') 
        for i in range(1, 20)]

lv1_r3_trampoline = [Trampoline(start_x + 210, HEIGHT - block_size - 58 * 6, 28,28,"Trampoline"),
                    Trampoline(start_x + (288 + 128) + 128 * 14 + 40, HEIGHT - block_size - 58 * 6, 28,28,"Trampoline")]

def loop_lv1_3():
    for i in lv1_r3_fire:
        i.on()
        i.loop()

    for i in lv1_r3_fireFloor:
        i.on()
        i.loop()

    for i in lv1_r3_trampoline:
        i.loop()

objs_lv1_3 = lv1_r3_blockFloor1 + lv1_r3_blockFloor2 + lv1_r3_obstacle1 + lv1_r3_obstacle2 + lv1_r3_fire + lv1_r3_fireFloor + lv1_r3_trampoline
    