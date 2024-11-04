from raw_object import *
from player import *

PLAYER_VEL = 5 
def handle_vertical_collistion(player, objects, dy):
    collided_objects = []
    
    for obj in objects:
        if player.mask and obj.mask:
            
            if pygame.sprite.collide_mask(player, obj):
                
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                    
                if dy < 0: 
                    player.rect.top = obj.rect.bottom
                    player.hit_head()
                collided_objects.append(obj)
    return collided_objects
 

def handle_collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collide_object = None

    for obj in objects:
        if player.mask and obj.mask:
            if pygame.sprite.collide_mask(player, obj):
                collide_object = obj
                break

    player.move(-dx, 0)
    player.update()
    return collide_object
                    

# Xử lý di chuyển 
def handle_move(player, objects):
    # Lấy danh sách phím ở hiện tại
    keys = pygame.key.get_pressed()

    collide_left = handle_collide(player, objects, -PLAYER_VEL * 2)
    collide_right = handle_collide(player, objects, PLAYER_VEL * 2)

    player.x_vel = 0
    if (keys[pygame.K_LEFT]) and not collide_left:
        player.move_left(PLAYER_VEL)
    if (keys[pygame.K_RIGHT]) and not collide_right:
        player.move_right(PLAYER_VEL)
    vertical_collide = handle_vertical_collistion(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]
    for obj in to_check:
        if obj:
            if obj.name == "Trampoline":
                player.make_hit_trampoline()
            if obj.name == "fire1" and obj.is_on():
                player.make_hit()
                player.health-=0.5
            if obj.name == "fire":
                player.make_hit()
                player.health-=0.5
            if obj.name == "spike":
                player.make_hit()
                player.health-=0.5
            if obj.name == "Saw":
                player.die()
            if obj.name == "falling_platform":
                player.hit_fl_pl()
            else:
                player.hit_fallingplatform=False

# Thiết kế riêng để phục vụ level 3
def hd_fall_block(player, blocks, blockks):
    fal_vel_bl = 5
    for i, block in enumerate(blocks):
        if i == 0:
            if player.rect.x >= block.rect.x + 96: 
                block.rect.y += fal_vel_bl
        else:
            if (abs(blocks[i - 1].rect.y - blockks[i - 1]) >= 500):
                block.rect.y += fal_vel_bl
    
    if player.rect.x == 4000:
        for i, block in enumerate(blocks):
            if i % 2 == 0:
                block.rect.x = 4000 + 96 * 4
            else:
                block.rect.x = 4000 + 96 * 8
            block.rect.y =  HEIGHT - 96 * (2.5 + 2 * i)