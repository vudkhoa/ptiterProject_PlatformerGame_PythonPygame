from level1 import *
from level2 import *
from level3 import *
from obj import *
from login import *
from end_screen import *

check = True
restart = False

while (check):
    if not restart:
        player.user_name, player.Password = login_screen()
        if player.user_name == "None" and player.Password == "None":
            break
    else:
        restart = False

    player, phandu = load_address_sprite(player)

    if player.level == 1:
        player, restart = lv1_main(window, player.user_name, player.Password)
    if player == None:
        break

    if player.level == 2:
        player, restart = lv2_main(window, player.user_name, player.Password)
    if player == None:
        break

    if player.level == 3:
        player, restart = lv3_main(window, player.user_name, player.Password)
    if player == None:
        break

    if player.level == 3 and player.round == 3 and player.health > 0:
        run_end_screen(True)