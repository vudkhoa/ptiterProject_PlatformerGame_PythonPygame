from raw_object import *
block_size = 96

lv1_r1_blockFloor = [Block(i * block_size, HEIGHT - block_size, block_size,0,1)
            for i in range(-WIDTH // block_size, (WIDTH* 3) // block_size - 7)]

lv1_r1_obstacles1 = [  
    Block(280, HEIGHT - block_size * 3, block_size,0,1),  
    Block(480, HEIGHT - block_size * 5, block_size,0,1), 
    Block(680, HEIGHT - block_size * 4, block_size,0,1)
]

lv1_r1_obstacles2 = [  
    Block(880, HEIGHT - block_size * 2.5, block_size - 32,0,1),  
    Block(1080, HEIGHT - block_size * 2.5, block_size - 32,0,1), 
    Block(1280, HEIGHT - block_size * 2.5, block_size - 32,0,1),
    Block(1480, HEIGHT - block_size * 2.5, block_size - 32,0,1),
    Block(1680, HEIGHT - block_size * 2.5, block_size - 32,0,1)
]

lv1_r1_obstacles3 = [  
    Block(2016, HEIGHT + 32 - block_size * 2, block_size - 32,1,3),
    Block(2016, HEIGHT + 32 -block_size * 4, block_size - 32,1,3),
    Block(2016, HEIGHT + 32 -block_size * 6, block_size - 32,1,3)  
]

lv1_r1_obstacles4 = [  
    Block(2308, HEIGHT - block_size * 2.5, block_size - 32,0,1),
    Block(2500, HEIGHT -block_size * 3.5, block_size - 32,0,1),
    Block(2692, HEIGHT -block_size * 4.5, block_size - 32,0,1), 
    Block(2900, HEIGHT -block_size * 6, block_size - 32,0,1)
]


lv1_r1_fireFloor1 = [Fire_lv1(i * 200, HEIGHT - block_size - 64, 16, 32,'0') for i in range(1,5)]

lv1_r1_fireFloor2 = [Fire_lv1(800 + i * 40, HEIGHT - block_size - 64, 16, 32,'0') for i in range(1,25)]

lv1_r1_fireFloor3 = [Fire_lv1(1956 + 16, HEIGHT - block_size -56, 16, 32,'x'),
                    Fire_lv1(1956 + 16, HEIGHT - block_size -248, 16, 32,'x'),
                    Fire_lv1(1956 + 16, HEIGHT - block_size - 440, 16, 32,'x')]

def loop_lv1_1():
    for i in lv1_r1_fireFloor1:
        i.on()
        i.loop()

    for i in lv1_r1_fireFloor2:
        i.on()
        i.loop()
        
    for i in lv1_r1_fireFloor3:
        i.on()
        i.loop()

objs_lv1_1 = lv1_r1_obstacles1 + lv1_r1_obstacles2 + lv1_r1_obstacles3 + lv1_r1_obstacles4 
objs_lv1_1 += lv1_r1_fireFloor1 + lv1_r1_fireFloor2 + lv1_r1_fireFloor3 + lv1_r1_blockFloor