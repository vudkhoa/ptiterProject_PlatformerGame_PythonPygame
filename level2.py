from level2_round1 import *
from level2_round2 import *
from level2_round3 import *
from obj import *
from menu import *

pygame.init()
pygame.display.set_caption("Level 2")

FPS = 60
block_x = 96
block_y = 96 * 2 / 3


window = pygame.display.set_mode((WIDTH, HEIGHT))

def lv2_main(window, name_player, password_player):
    clock = pygame.time.Clock()
    
    x = Player(0, 0, 0, 0)
    x.user_name = name_player
    x.Password = password_player
    player, phandu = load_address_sprite(x)
    quit_game = False

    menu_play = Menu_play(window)
    menu = Menu(window)
    play_bg_music('assets/music/bg_music.mp3')

    if player.round == 2:
        offset_x = player.rect.x - 200
    else :
        offset_x = player.rect.x
    offset_x_tmp = 0
    offset_y = player.rect.y - HEIGHT + phandu
    
    scroll_area_width = 200
    check = False
    restart = False

    falling_platforms = [
        lv2_r1_falling_platform,
        lv2_r2_falling_platform1,
        lv2_r2_falling_platform2,
        lv2_r2_falling_platform3,
        lv2_r3_falling_platform1,
        lv2_r3_falling_platform2,
        lv2_r3_falling_platform3,
        lv2_r3_falling_platform4]

    objs = [
        *lv2_r1_blockFloor,
        *lv2_r1_spikes,
        *lv2_r1_fires,
        *lv2_r1_saw,    
        *lv2_r1_sawtmp,
        lv2_r1_trampo,
        

        lv2_r2_block1,
        
        lv2_r2_block2,
        lv2_r2_fire,
        lv2_r2_block3,
        lv2_r2_trampo,
        lv2_r2_block4,
        *lv2_r2_saw,
        lv2_r2_block5,
        lv2_r2_block6,
        

        *lv2_r3_blockFloor,
        *lv2_r3_fires,
        
        lv2_r3_block1,
        lv2_r3_block2,
        lv2_r3_block3,
        lv2_r3_block4,
        lv2_r3_block5,
        lv2_r3_block6,
        lv2_r3_block7,
        lv2_r3_block8,
        lv2_r3_block9,
        lv2_r3_block10,
        lv2_r3_block11,
        lv2_r3_block12,
        lv2_r3_block13,
        lv2_r3_block14,
        lv2_r3_block15,
        lv2_r3_block16,
        lv2_r3_block17,
        lv2_r3_block18,
        lv2_r3_block19,
        lv2_r3_block20,
        lv2_r3_block21,
        lv2_r3_block22,
        lv2_r3_block23,
        lv2_r3_trampo,
        lv2_r3_trampo1,
        *lv2_r3_saw,
        *lv2_r3_sawtmp,
        *falling_platforms]
    
    background00, bg_image_00 = get_bg("Blue.png", WIDTH * 3, HEIGHT, 0, 0)
    background01, bg_image_01 = get_bg("Brown.png", WIDTH * 3, HEIGHT, 3000 * 1, 0)
    background02, bg_image_02 = get_bg("Gray.png", WIDTH * 4, HEIGHT, 3000 * 2, 0)



    backgrounds = []
    backgrounds.append(background00)
    backgrounds.append(background01)
    backgrounds.append(background02)

    bg_images = []
    bg_images.append(bg_image_00)
    bg_images.append(bg_image_01)
    bg_images.append(bg_image_02)

    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                return None, restart
            if event.type == pygame.KEYDOWN: 
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and player.jump_count < 2: 
                    player.jump()   
                if event.key == pygame.K_ESCAPE:
                    menu.run_menu = True
                    if not menu.loop():
                        if menu.quit_pressed:
                            quit_game = True
                        menu.run_menu = False
        
        if player.health <= 0:
            for platform in falling_platforms:
                platform.reset()
            menu_play.run_menu = True
            while menu_play.run_menu:
                check_menu_play, quitt = menu_play.loop()
                if quitt == "quit":
                    return None, restart
                if not check_menu_play:
                    if menu_play.quit_pressed:
                        quit_game = True
                    menu_play.run_menu = False

        if menu_play.click == "restart":
            restart = True

        if player.health <= 0 or quit_game:
            if check == False: 
                check_update_data = True
                for index in range(len(data_input)):
                    if data_input[index]['name'] == player.user_name and data_input[index]['password'] == player.Password:
                        if data_input[index]['level'] <=  player.level and data_input[index]['round'] <= player.round:
                            data_input.pop(index)
                            break
                        else:
                            check_update_data = False
                            break
                if check_update_data:         
                    data_input.append({"name": player.user_name, "level": player.level, "round": player.round, "password": player.Password})
                with open("output.txt", "w", encoding="utf-8") as file:
                    for index in range(len(data_input)):
                        file.write(data_input[index]['name'] + "#" +  str(data_input[index]['level']) + "#" + str(data_input[index]['round']) + "#" + data_input[index]['password'] + '\n')
                check = True
            return player, restart
        player.loop(FPS)
        if player.rect.x >=  9740:
            player.level += 1
            player.round = 1
            for index in range(len(data_input)):
                if data_input[index]['name'] == player.user_name and data_input[index]['password'] == player.Password:
                        data_input.pop(index)
                        break
            data_input.append({"name": player.user_name, "level": player.level, "round": player.round, "password": player.Password})

            with open("output.txt", "w", encoding="utf-8") as file:
                for index in range(len(data_input)):
                    file.write(data_input[index]['name'] + "#" +  str(data_input[index]['level']) + "#" + str(data_input[index]['round']) + "#" + data_input[index]['password'] + '\n')
            if quit_game:
                player.level = 0
                player.round = 0
                return player, restart
            return player, restart
        lv2_1_loop()
        lv2_2_loop()
        lv2_3_loop()
        distance_to_platform = abs(player.rect.x - lv2_r1_falling_platform.rect.x)
        if distance_to_platform < lv2_r1_falling_platform.TRIGGER_DISTANCE:
            lv2_r1_falling_platform.trigger_fall()
        lv2_r1_falling_platform.loop()

        distance_to_platform1 = abs(player.rect.x - lv2_r2_falling_platform1.rect.x)
        if distance_to_platform1 < lv2_r2_falling_platform1.TRIGGER_DISTANCE:
            lv2_r2_falling_platform1.trigger_fall()
        lv2_r2_falling_platform1.loop()

        distance_to_platform2 = abs(player.rect.x - lv2_r2_falling_platform2.rect.x)
        if distance_to_platform2 < lv2_r2_falling_platform2.TRIGGER_DISTANCE:
            lv2_r2_falling_platform2.trigger_fall()
        lv2_r2_falling_platform2.loop()

        distance_to_platform3 = abs(player.rect.x - lv2_r2_falling_platform3.rect.x)
        if distance_to_platform3 < lv2_r2_falling_platform3.TRIGGER_DISTANCE:
            lv2_r2_falling_platform3.trigger_fall()
        lv2_r2_falling_platform3.loop()

        distance_to_platform4 = abs(player.rect.x - lv2_r3_falling_platform1.rect.x)
        if distance_to_platform4 < lv2_r3_falling_platform1.TRIGGER_DISTANCE:
            lv2_r3_falling_platform1.trigger_fall()
        lv2_r3_falling_platform1.loop()

        distance_to_platform5 = abs(player.rect.x - lv2_r3_falling_platform2.rect.x)
        if distance_to_platform5 < lv2_r3_falling_platform2.TRIGGER_DISTANCE:
            lv2_r3_falling_platform2.trigger_fall()
        lv2_r3_falling_platform2.loop()

        distance_to_platform6 = abs(player.rect.x - lv2_r3_falling_platform3.rect.x)
        if distance_to_platform6 < lv2_r3_falling_platform3.TRIGGER_DISTANCE:
            lv2_r3_falling_platform3.trigger_fall()
        lv2_r3_falling_platform3.loop()

        distance_to_platform7 = abs(player.rect.x - lv2_r3_falling_platform4.rect.x)
        if distance_to_platform7 < lv2_r3_falling_platform4.TRIGGER_DISTANCE:
            lv2_r3_falling_platform4.trigger_fall()
        lv2_r3_falling_platform4.loop()

        handle_move(player, objs)
        draw(window, backgrounds, bg_images, objs, player, offset_x, offset_y)
        # WIDTH = 1000
        # scroll_area_width = 200 
        # WIDTH - scroll_area_width >= 800 
        # Giới hạn của player.rect.eight <= 800 
        # tầm nhìn buộc phải là 200 => player.rect.right - offset_x (*) <= 800
        # player.rect.right: vị trí nhân vật bên phải cùng, offset_X: độ dời so với ban đầu
        # khi nhân vật di chuyển vượt 800 -> (*) vượt 800 -> cập nhật lại offset
        # = (*) > 200 bao nhiêu
        if (player.x_vel > 0 and (player.rect.right - offset_x >= WIDTH - scroll_area_width)) or (
            # Tương tự 
            player.x_vel < 0 and (player.rect.left  - offset_x <= scroll_area_width)):
            if (offset_x + player.x_vel >= 0 and offset_x + player.x_vel <= 9055 - scroll_area_width):
                offset_x += player.x_vel

            if offset_x != offset_x_tmp:
                update_offset(offset_x - offset_x_tmp, backgrounds)
                offset_x_tmp = offset_x

        if ((player.rect.top + offset_y <= scroll_area_width) and player.y_vel < 0) or (
            (player.rect.bottom + offset_y >= HEIGHT - scroll_area_width) and player.y_vel > 0):
            if (offset_y - player.y_vel >= 0):
                offset_y -= player.y_vel
        
        pygame.display.update()
    pygame.quit()
    quit()
