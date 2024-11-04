from raw_object import *
#round nào cũng có block_size :)))
block_size = 96
start_x = 2900  

lv1_r2_blockFloor1 = [Block(start_x + 80 + i * block_size, HEIGHT - block_size, block_size, 1,1)
                    for i in range(2)]

lv1_r2_blockFloor2 = [Block(start_x + 2208 + i * block_size, HEIGHT - block_size, block_size, 1,1)
                    for i in range(8)]

lv1_r2_obstacle1 = [Block(start_x + 288 + 128, HEIGHT - block_size * 2, block_size, 1,1),
                    Block(start_x + (288 + 128) + 128 * 2, HEIGHT - block_size * 2, block_size, 1,1),
                    Block(start_x + (288 + 128) + 128 * 4, HEIGHT - block_size * 2, block_size, 1,1),
                    Block(start_x + (288 + 128) + 128 * 8, HEIGHT - block_size * 2, block_size, 1,1),
                    Block(start_x + (288 + 128) + 128 * 10, HEIGHT - block_size * 2, block_size, 1,1),
                    Block(start_x + (288 + 128) + 128 * 12, HEIGHT - block_size * 2, block_size, 1,1)]

lv1_r2_obstacle2 = [Block(start_x + (288 + 128) + 128 * 6, HEIGHT - block_size * 6, block_size, 1,1),
                Block(start_x + (288 + 128) + 128, HEIGHT - block_size * 4, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 3, HEIGHT - block_size * 6, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 5, HEIGHT - block_size * 4, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 7, HEIGHT - block_size * 4, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 9, HEIGHT - block_size * 6, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 11, HEIGHT - block_size * 4, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 14, HEIGHT - block_size * 6, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 16, HEIGHT - block_size * 6, block_size, 1,1),
                Block(start_x + (288 + 128) + 128 * 18, HEIGHT - block_size * 6, block_size, 1,1)]

lv1_r2_fireFloor = [Fire_lv1(start_x + (i * 40) + 2180, HEIGHT - block_size - 64, 16, 32, '0') 
                for i in range(1, 16)]
lv1_r2_fire =   [Fire_lv1(start_x + (288 + 128) + 128 * 4 + 32, HEIGHT - block_size - 160, 16, 32, '0'),
                Fire_lv1(start_x + (288 + 128) + 128 * 7 + 32, HEIGHT - block_size - 352, 16, 32, '0'),
                Fire_lv1(start_x + (288 + 128) + 128 * 10 + 32, HEIGHT - block_size - 160, 16, 32, '0')]

def loop_lv1_2():
    for i in lv1_r2_fire:
        i.on()
        i.loop()
        
    for i in lv1_r2_fireFloor:
        i.on()
        i.loop()    
objs_lv1_2 = lv1_r2_blockFloor1 + lv1_r2_blockFloor2 + lv1_r2_obstacle1 + lv1_r2_obstacle2 + lv1_r2_fireFloor + lv1_r2_fire