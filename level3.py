from level3_round3 import *
from obj import *
from menu import *
from end_screen import *

pygame.init()
pygame.display.set_caption("Level 3")

FPS = 60
block_x = 96
block_y = 96 * 2 / 3

window = pygame.display.set_mode((WIDTH, HEIGHT))




def lv3_main(window, name_player, password_player):
    clock = pygame.time.Clock()
    
    x = Player(0, 0, 0, 0)
    x.user_name = name_player
    x.Password = password_player
    player, phandu = load_address_sprite(x)
    
    quit_game = False
    
    menu_play = Menu_play(window)
    menu = Menu(window)
    play_bg_music('assets/music/bg_music.mp3')

    scroll_area_width = int(200)
    offset_x = player.rect.x
    offset_x_tmp = 0
    offset_y = player.rect.y - HEIGHT + phandu

    scroll_area_width = 200
    check = False
    restart = False
    objs = []
    objs = [lv3_r1_block0, lv3_r1_block1, lv3_r1_block2, lv3_r1_block3, lv3_r1_block4, lv3_r1_block5, 
            block06, block07, block08, block09, block10, block11, block12, block13, block14, block15,
            block16, block17, block18, block19, block20, block21, block22, block23, block24, block25, block26, 
            lv3_r1_saw_0, lv3_r1_saw_1, lv3_r1_saw_2, lv3_r1_saw_3, lv3_r1_saw_4, lv3_r1_saw_5, lv3_r1_saw_6, lv3_r1_saw_7, lv3_r1_saw_8, lv3_r1_saw_9, lv3_r1_saw_10, 
            obj_saw_19, obj_saw_11, obj_saw_12, obj_saw_13, obj_saw_14, obj_saw_15, obj_saw_16, obj_saw_17,
            lv3_r1_trampoline_00, lv3_r1_trampoline_01, lv3_r1_trampoline_02, 
            obj_trampoline_03, obj_trampoline_04,
            lv3_r2_obj_fire_00, lv3_r2_obj_fire_01, lv3_r2_obj_fire_02, lv3_r2_obj_fire_03, lv3_r2_obj_fire_04, lv3_r2_obj_fire_05, lv3_r2_obj_fire_06, lv3_r2_obj_fire_07, lv3_r2_obj_fire_08, lv3_r2_obj_fire_09, 
            lv3_r2_obj_fire_10, lv3_r2_obj_fire_11, lv3_r2_obj_fire_12, lv3_r2_obj_fire_13, lv3_r2_obj_fire_14, lv3_r2_obj_fire_15, lv3_r2_obj_fire_16, lv3_r2_obj_fire_17, lv3_r2_obj_fire_18, lv3_r2_obj_fire_19,
            lv3_r2_obj_fire_20,
            block05_fire]
    
    background00, bg_image_00 = get_bg("Blue.png", WIDTH * 2, HEIGHT, 2000 * 0, 0)
    background01, bg_image_01 = get_bg("Brown.png", WIDTH * 2, HEIGHT, 2000 * 1, 0)
    background02, bg_image_02 = get_bg("Gray.png", WIDTH * 3, HEIGHT, 2000 * 2, 0)
    background_tmp = []
    background_tmp.append(background00)
    background_tmp.append(background01)
    background_tmp.append(background02)
    bg_tmp = []
    bg_tmp.append(bg_image_00)
    bg_tmp.append(bg_image_01)
    bg_tmp.append(bg_image_02)

    backgrounds = background_tmp
    bg_images = bg_tmp
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
            if quit_game:
                player.level = 0
                player.round = 0
                return player, restart
            return player, restart
        hd_fall_block(player, handle_fall_block, blockks)
        round1_handle_move_obj(player)
        round2_handle_move_obj()
        round3_handle_move_obj()
        round1_loop()
        round2_loop()
        round3_loop()
        player.loop(FPS)
        if player.rect.right >=  6980:
            for index in range(len(data_input)):
                if data_input[index]['name'] == player.user_name and data_input[index]['password'] == player.Password:
                        data_input.pop(index)
                        break
            data_input.append({"name": player.user_name, "level": player.level, "round": player.round, "password": player.Password})

            with open("output.txt", "w", encoding="utf-8") as file:
                for index in range(len(data_input)):
                    file.write(data_input[index]['name'] + "#" +  str(data_input[index]['level']) + "#" + str(data_input[index]['round']) + "#" + data_input[index]['password'] + '\n')

            return player, restart
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
            if offset_x + player.x_vel >= 0 and  player.rect.right + player.x_vel <= 7000 - scroll_area_width:
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
