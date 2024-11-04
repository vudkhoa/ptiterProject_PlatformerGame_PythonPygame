from load import *

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA) 
        self.width = width
        self.height = height
        self.name = name
    # đi qua phải khung cảnh dịch về trái ("đi qua)")
    def draw(self, win, offset_x, offset_y):
        window.blit(self.image, (self.rect.x - offset_x, self.rect.y + offset_y))

class Saw(Object):
    ANIMATION_DELAY = 1
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)
        # Load
        self.saw = load_sprite_sheets("Traps", "Saw", width, height)
        # 
        self.image = self.saw["off"][0]
        #
        self.mask = pygame.mask.from_surface(self.image)
        #    
        self.animation_count = 0 
        # 
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def update_saw(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    # Cập nhật trạng thái tạo animation mượt mà 
    def loop(self):
        sprites = self.saw[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.update_saw()

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Trampoline(Object):
    ANIMATION_DELAY = 2
    def __init__(self, x, y, width, height, name): 
        super().__init__(x, y, width, height, name)
        self.trampoline = load_sprite_sheets("Traps", "Trampoline", width, height)
        self.image = self.trampoline["Jump (28x28)"][0]
        self.animation_count = 0
        self.animation_name = "Jump (28x28)"

    def update_trampoline(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def loop(self):
        sprites = self.trampoline[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.update_trampoline()

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Block(Object):
    def __init__(self, x, y, size, xBlock, yBlock):
        super().__init__(x, y, size, size)
        self.size = size
        self.xBlock = xBlock
        self.yBlock = yBlock
        block = get_block(size, xBlock, yBlock)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)


    def update(self):
        block = get_block(self.size, self.xBlock, self.yBlock)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)


class Fire(Object):
    ANIMATION_DELAY = 3
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"
    
    def off(self):
        self.animation_name = "off"
    
    def update(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.update()

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Fire1(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire1")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.state_time = 0  # Timer to track state duration
        self.state_duration = 300  # Duration for each state (3 seconds at 60 FPS)

    def toggle_state(self):
        """Toggle between 'on' and 'off' states."""
        if self.animation_name == "off":
            self.animation_name = "on"
        else:
            self.animation_name = "off"

    def is_on(self):
        """Check if the fire is currently on."""
        return self.animation_name == "on"

    def loop(self):
        """Update the fire state and animation."""
        self.state_time += 1
        if self.state_time >= self.state_duration:
            self.toggle_state()
            self.state_time = 0  # Reset the timer

        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class Fire_lv1(Object):
    ANIMATION_DELAY = 3
    def __init__(self, x, y, width, height,flip):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.flip = flip
    def on(self):
        self.animation_name = "on"
    
    def off(self):
        self.animation_name = "off"
    
    def update(self):
        self.rect = self.image.get_rect(topleft = (self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        if self.flip == 'x':
            self.image = pygame.transform.rotate(sprites[sprite_index], 90)  
        else:    
            self.image = sprites[sprite_index]
        self.animation_count += 1

        self.update()

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class FallingPlatform(Object):
    ANIMATION_DELAY = 3  # Thời gian giữa các khung hình
    FALL_SPEED = 25  # Tốc độ rơi của platform
    FALL_DURATION = 60  # Thời gian rơi tối đa (theo frame)
    TRIGGER_DISTANCE = 100  # Khoảng cách để kích hoạt rơi

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "falling_platform")
        self.start_y = y  # Lưu vị trí ban đầu
        self.images = load_sprite_sheets("Traps", "Falling Platforms", width, height)
        self.image = self.images["Off"][0]  # Ban đầu là trạng thái "Off"
        self.mask = pygame.mask.from_surface(self.image)

        self.falling = False  # Trạng thái rơi
        self.fall_timer = 0  # Bộ đếm thời gian rơi
        self.has_fallen = False  # Chưa rơi

    def trigger_fall(self):
        """Kích hoạt quá trình rơi nếu chưa rơi."""
        if not self.has_fallen:
            self.falling = True
            self.has_fallen = True  # Đánh dấu đã rơi

    def reset(self):
        """Đặt lại trạng thái rơi của platform."""
        self.falling = False
        self.fall_timer = 0
        self.has_fallen = False
        self.image = self.images["Off"][0]  # Đặt lại hình ảnh trạng thái ban đầu
        self.rect.y = self.start_y  # Đặt lại vị trí ban đầu

    def loop(self):
        """Cập nhật trạng thái rơi và animation."""
        if self.falling:
            if self.fall_timer < self.FALL_DURATION:
                self.rect.y += self.FALL_SPEED  # Di chuyển xuống
                self.fall_timer += 1
            else:
                self.falling = False  # Dừng lại sau khi hết thời gian

        # Cập nhật hình ảnh và mask để phát hiện va chạm
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win, offset_x, offset_y):
        """Vẽ platform lên màn hình."""
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y - offset_y))
        
class Spike(Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "spike")
        self.image = pygame.image.load(join("assets", "Traps", "Spikes", "Idle.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        # Không có animation nên không cần cập nhật hình ảnh
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, win, offset_x, offset_y=0):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))

def update_offset(dx, blocks):
    for bl in blocks:
        for tile in bl:
            tile[0] -= dx
            
def draw(window, backgrounds, bg_images, blocks, player, offset_x, offset_y):
    for i, background in enumerate(backgrounds):
        for tile in background:
            
            window.blit(bg_images[i], tile)
        
    # Duyệt tất cả block và vẽ
    for bl in blocks:
        bl.draw(window, offset_x, offset_y)

    # Vẽ player
    player.draw(window, offset_x, offset_y)
    
    pygame.display.update()

# x : chiều dài
# y : chiều rộng
# dx: Từ tọa độ x bao nhieu
# dy: Từ tọa độ y bao nhiêu
def get_bg(name, x, y, dx, dy):
    # Load link 
    image = pygame.image.load(join("assets", "Background", name))
    # _, _,: Bỏ qua vị trí x y
    _, _, width, height = image.get_rect()

    titles = [] 
    # Chia chiều dài tổng cho từng ô để xác định vị trí vẽ
    for i in range(x // width + 1):
        for j in range(y // height + 1):
            pos = [dx + i * width, dy + j * height]
            titles.append(pos)

    return titles, image

def get_bg_login(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)
    return tiles, image

def draw_bg_login(window,background,bg_image):
    for tile in background:
        window.blit(bg_image, tile)  
        

def draw_text_login(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

