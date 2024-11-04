from player import *
from level1_round1 import *
from level1_round2 import *
from level1_round3 import *
from handle import *
from obj import *
from menu import *

pygame.init()
pygame.display.set_caption("Level 1")

FPS = 60
block_x = 96
block_y = 96 * 2 / 3
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def lv1_main(window, name_player, password_player):#username):
    clock = pygame.time.Clock()

    x = Player(0, 0, 0, 0)
    x.user_name = name_player
    x.Password = password_player
    quit_game = False

    player, phandu = load_address_sprite(x)
    scroll_area_width = 200

    menu_play = Menu_play(window)
    menu = Menu(window)
    play_bg_music('assets/music/bg_music.mp3')

    background00, bg_image_00 = get_bg("Blue.png", WIDTH * 3, HEIGHT, 2000 * 0, 0)
    background01, bg_image_01 = get_bg("Brown.png", WIDTH * 3, HEIGHT, 2975 * 1, 0)
    background02, bg_image_02 = get_bg("Gray.png", WIDTH * 3, HEIGHT, 2000 * 2.9 + 75, 0)

    offset_x = player.rect.x
    offset_x_tmp = 0
    offset_y = player.rect.y - HEIGHT + phandu
    
    backgrounds = []
    backgrounds.append(background00)
    backgrounds.append(background01)
    backgrounds.append(background02)

    bg_images = []
    bg_images.append(bg_image_00)
    bg_images.append(bg_image_01)
    bg_images.append(bg_image_02)
    check = False
    restart = False

    objs = objs_lv1_1 + objs_lv1_2 + objs_lv1_3
    run = True
    while run: 
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #or menu.quit_pressed: 
                run = False
                return None, restart
            if event.type == pygame.KEYDOWN: 
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and player.jump_count < 2: 
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
            if quit_game:
                player.level = 0
                player.round = 0
                return player, restart
            return player, restart
        player.loop(FPS)
        if player.rect.right >= 8829:
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
            return player, restart
        loop_lv1_1()
        loop_lv1_2()
        loop_lv1_3()
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
            if (offset_x + player.x_vel >= 0 and offset_x + player.x_vel <= 8050 - scroll_area_width):
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

if __name__ == '__main__':
    main(window)