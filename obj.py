from handle import *
block_size = 96
phandu = 0
name_player = ""
pass_player = ""

def read_file():
    data_input = []
    with open('output.txt', 'r', encoding = 'utf-8') as file:
        for string in file:
            x = string.strip().split("#")
            data_input.append({"name": x[0], "level": int(x[1]), "round": int(x[2]), "password": x[3]})
    return data_input

player = Player(0, 0, 0, 0)
player.user_name = name_player
player.Password = pass_player
phandu = 0
backgrounds = []
bg_images = []
exits = False
index_player = 0
def load_address_sprite(player):
    phandu = 0
    exits = False
    global name_player
    name_player = player.user_name
    pass_player = player.Password
    
    for index in range(len(data_input)):
        if data_input[index]['name'] == player.user_name and data_input[index]['password'] == player.Password:
            index_player = index
            exits = True
            if data_input[index]['level'] == 1:
                if data_input[index]['round'] == 1:    
                    player = Player(0, 800 - 96, 50, 50)
                    phandu = 96
                elif data_input[index]['round'] == 2:
                    player = Player(2980, 800 - 96, 50, 50)
                    phandu = 96
                elif data_input[index]['round'] == 3:
                    player = Player(5875, 800 - 96, 50, 50)
                    phandu = 96

            if data_input[index]['level'] == 2:
                if data_input[index]['round'] == 1:    
                    player = Player(0, 800 - 96, 50, 50)
                    phandu = 96
                elif data_input[index]['round'] == 2:
                    player = Player(3200, 800 -((HEIGHT - block_size * 7) + 96), 50, 50)
                    phandu = ((HEIGHT - block_size * 7) + 96) + (HEIGHT - block_size * 7)
                elif data_input[index]['round'] == 3:
                    player = Player(6000, 800 - 96, 50, 50)
                    phandu = 96

            if data_input[index]['level'] == 3:
                if data_input[index]['round'] == 1:
                    player = Player(0, 800 - 96, 50, 50)
                    phandu = 96
                elif data_input[index]['round'] == 2:
                    # Round 2
                    player = Player(2000, 800 - ((HEIGHT - block_size * 5) + 96), 50, 50)
                    phandu = ((HEIGHT - block_size * 5) + 96) + (HEIGHT - block_size * 5)
                elif data_input[index]['round'] == 3:
                    # Round 3
                    player = Player(4000, 800 - 96, 50, 50)
                    phandu = 96
                    
            player.level = data_input[index]['level']
            player.round = data_input[index]['round']
    if exits == False:
        player = Player(0, 800 - 96, 50, 50)
        phandu = 96
    player._draw = True
    player.user_name = name_player
    player.Password = pass_player
    return player, phandu

data_input = read_file()
player, phandu = load_address_sprite(player)
