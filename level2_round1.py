from handle import *
block_size = 96

lv2_r1_blockFloor = [Block(i * block_size, HEIGHT - block_size, block_size,2,0)
        for i in range(-1000 // block_size, (1000 * 3) // block_size)]
    
lv2_r1_spikes = [Spike(250 + i * 40, 675, 32, 32) for i in range(7)]
lv2_r1_fires  = [Fire1(750+i*50,640,16,32) for i in range(6)]
lv2_r1_sawtmp = [Saw(1900 + i * 77, 610, 38, 38, "Saw") for i in range(8)]
lv2_r1_saw = [Saw(1300 + i * 77, 610, 38, 38, "Saw") for i in range(3)]
lv2_r1_falling_platform = FallingPlatform(2800,-64,32,20)

lv2_r1_trampo = Trampoline(1400 + 84 * 2 + 120 * 2, HEIGHT - block_size-50, 28, 28, "Trampoline")


for i in lv2_r1_saw:
        i.on()

for i in lv2_r1_sawtmp:
        i.on()
 
def lv2_1_loop():
    for i in lv2_r1_fires:
        i.loop()
    for i in lv2_r1_sawtmp:
        i.loop()
    for i in lv2_r1_saw:
        i.loop()
        
    lv2_r1_trampo.loop()
    





