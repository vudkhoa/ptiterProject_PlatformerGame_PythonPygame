from level3_round1 import *

lv3_r2_obj_fire_00 = Fire(3800, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_01 = Fire(3832, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_02 = Fire(2050, HEIGHT - block_size, 16, 32)
lv3_r2_obj_fire_03 = Fire(2300, HEIGHT - block_size, 16, 32)
lv3_r2_obj_fire_04 = Fire(2350, HEIGHT - block_size, 16, 32)
lv3_r2_obj_fire_05 = Fire(2600, HEIGHT - block_size * 3, 16, 32)
lv3_r2_obj_fire_06 = Fire(2900, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_07 = Fire(2900 + 32, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_08 = Fire(2900 + 32 * 2, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_09 = Fire(2900 + 32 * 3, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_10 = Fire(2900 + 32 * 4, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_11 = Fire(2900 + 32 * 5, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_12 = Fire(2900 + 32 * 6, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_13 = Fire(2900 + 32 * 7, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_14 = Fire(2900 + 32 * 8, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_15 = Fire(2900 + 32 * 9, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_16 = Fire(2900 + 32 * 10, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_17 = Fire(2900 + 32 * 11, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_18 = Fire(2900 + 32 * 12, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_19 = Fire(2900 + 32 * 13, HEIGHT - block_size * 5, 16, 32)
lv3_r2_obj_fire_20 = Fire(2900 + 32 * 14, HEIGHT - block_size * 5, 16, 32) 
block05_fire = Fire(2033, HEIGHT - block_size * 5 + 15, 16, 32)

obj_saw_11 = Saw(2900, HEIGHT - block_size * 5 - 74 - 240, 38, 38, "Saw")
obj_saw_12 = Saw(2900 + 84 + 120, HEIGHT - block_size * 5 - 74 - 240, 38, 38, "Saw")
obj_saw_13 = Saw(2900 + 84 * 2 + 120 * 2, HEIGHT - block_size * 5 - 74 - 240, 38, 38, "Saw")
obj_saw_14 = Saw(2900, (HEIGHT - block_size * 5 - 74) / 2, 38, 38, "Saw")
obj_saw_15 = Saw(2900 + 84 * 2 + 120 * 2, (HEIGHT - block_size * 5 - 74) / 2, 38, 38, "Saw")
obj_saw_18 = Saw(2900 + 120 + 84 ,HEIGHT - block_size * 5 - 74, 38, 38, "Saw")
obj_saw_18_x = int(2)
obj_saw_16 = Saw(2900 + 84 + 18 , HEIGHT - block_size * 5 - 74, 38, 38, "Saw")
obj_saw_17 = Saw(2900 + 84 * 3 + 18 * 3, HEIGHT - block_size * 5 - 74, 38, 38, "Saw")
obj_saw_11_12_13_y = int(-3)
obj_saw_14_x = int(3)

obj_trampoline_03 = Trampoline(3100 + 84 * 2 + 120 * 2, HEIGHT - block_size, 28, 28, "Trampoline")

lv3_r2_obj_fire_00.on()
lv3_r2_obj_fire_01.on()
lv3_r2_obj_fire_02.on()
lv3_r2_obj_fire_03.on()
lv3_r2_obj_fire_04.on()
lv3_r2_obj_fire_05.on()
lv3_r2_obj_fire_06.on()
lv3_r2_obj_fire_07.on()
lv3_r2_obj_fire_08.on()
lv3_r2_obj_fire_09.on()
lv3_r2_obj_fire_10.on()
lv3_r2_obj_fire_11.on()
lv3_r2_obj_fire_12.on()
lv3_r2_obj_fire_13.on()
lv3_r2_obj_fire_14.on()
lv3_r2_obj_fire_15.on()
lv3_r2_obj_fire_16.on()
lv3_r2_obj_fire_17.on()
lv3_r2_obj_fire_18.on()
lv3_r2_obj_fire_19.on()
lv3_r2_obj_fire_20.on()
block05_fire.on()

obj_saw_11.on()
obj_saw_12.on()
obj_saw_13.on()
obj_saw_14.on()
obj_saw_15.on()
obj_saw_16.on()
obj_saw_17.on()
obj_saw_18.on()

def round2_loop():
    lv3_r2_obj_fire_00.loop()
    lv3_r2_obj_fire_01.loop()
    lv3_r2_obj_fire_02.loop()
    lv3_r2_obj_fire_03.loop()
    lv3_r2_obj_fire_04.loop()
    lv3_r2_obj_fire_05.loop()
    lv3_r2_obj_fire_06.loop()
    lv3_r2_obj_fire_07.loop()
    lv3_r2_obj_fire_08.loop()
    lv3_r2_obj_fire_09.loop()
    lv3_r2_obj_fire_10.loop()
    lv3_r2_obj_fire_11.loop()
    lv3_r2_obj_fire_12.loop()
    lv3_r2_obj_fire_13.loop()
    lv3_r2_obj_fire_14.loop()
    lv3_r2_obj_fire_15.loop()
    lv3_r2_obj_fire_16.loop()
    lv3_r2_obj_fire_17.loop()
    lv3_r2_obj_fire_18.loop()
    lv3_r2_obj_fire_19.loop()
    lv3_r2_obj_fire_20.loop()
    block05_fire.loop()
    
    obj_saw_11.loop()
    obj_saw_12.loop()
    obj_saw_13.loop()
    obj_saw_14.loop()
    obj_saw_15.loop()
    obj_saw_16.loop()
    obj_saw_17.loop()
    obj_saw_18.loop()

    obj_trampoline_03.loop()


def round2_handle_move_obj():
    global obj_saw_11_12_13_y
    global obj_saw_14_x
    global obj_saw_18_x
    global background00, bg_image_00
    global background01, bg_image_01
    global background02, bg_image_02
    
    if obj_saw_11.rect.y >= HEIGHT - block_size * 5 - 74 or obj_saw_11.rect.y <= HEIGHT - block_size * 5 - 74 - 240:
        obj_saw_11_12_13_y *= -1
    
    if obj_saw_14.rect.x >= 2900 or obj_saw_14.rect.x <= 2900 - 120 :
        obj_saw_14_x *= -1

    if obj_saw_18.rect.x >= 2900 + 84 * 4 + 18 * 4 or obj_saw_18.rect.x <= 2900 + 84 + 120:
        obj_saw_18_x *= -1

    obj_saw_11.rect.y += obj_saw_11_12_13_y
    obj_saw_12.rect.y += obj_saw_11_12_13_y
    obj_saw_13.rect.y += obj_saw_11_12_13_y
    obj_saw_16.rect.y += obj_saw_11_12_13_y * (-1)
    obj_saw_17.rect.y += obj_saw_11_12_13_y * (-1)
    obj_saw_14.rect.x += obj_saw_14_x
    obj_saw_15.rect.x += obj_saw_14_x * (-1)
    obj_saw_18.rect.x += obj_saw_18_x
    

