from load import *

class Player(pygame.sprite.Sprite): 
    # TRỌNG LỰC 
    GRAVITY = 1
    # NHÂN VẬT 
    SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)
    # THỜI GIAN LẶP LẠI KHUNG HÌNH CHO PLAYER
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        # Hàm khởi tạo
        super().__init__()
        # x, y -> vị trí
        # width, height -> kích thước
        self.rect = pygame.Rect(x, y, width, height)
        # Khởi tạo thuộc tính sprite
        self.sprite = pygame.Surface((width, height))
        # Vận tốc theo trục x 
        self.x_vel = 0
        # _________________ y 
        self.y_vel = 0
        # mask: xác định vị trí va chạm
        self.mask = None
        # Khởi tạo hướng di chuyển 
        self.direction = "left"
        # Khởi tạo số lần hoạt ảnh 
        self.animation_count = 0
        # Số lần rơi
        self.fall_count = 0
        # Số lần nhảy
        self.jump_count = 0
        #
        self.hit = False
        self.hit_count = 0
        self.hit_fallingplatform = False
        #
        self.run = True
        self.health = 100
        self.level = 1
        self.round = 1
        self.user_name = ""
        self.Password = ""
        self._draw = False
    
    # Tiếp đất
    def landed(self):
        # Rơi về 0
        self.fall_count = 0
        # Tốc độ trục y về 0
        self.y_vel = 0
        # Nhảy về 0
        self.jump_count = 0
    
    # Đụng đầu
    def hit_head(self): 
        self.y_vel *= -1

    def jump(self):
        # Thiết lập tốc độ bay lên >< hướng vs trọng lực
        self.y_vel = -self.GRAVITY * 8
        # Đứng xuống sẽ giống lúc đầu trò chơi
        self.animation_count = 0
        # Tăng số lần nhảy và reset lần rơi
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def make_hit(self):
        self.hit = True

    def hit_fl_pl(self):
        if(self.hit_fallingplatform==False):
            self.hit_fallingplatform=True
            self.health-=10
            self.make_hit()

    def make_hit_trampoline(self):
        self.y_vel = -15

    def die(self):
        self.health = 0

    def next_level(self):
        self.level += 1
        self.round = 1

    # Cập nhật vị trí nhân vật
    def move(self, dx, dy):
        if self.rect.y > 800:
            self.die()
        # Lượng x thay đổi 
        if self.level == 1:
            if self.rect.left + dx >= 0 and self.rect.right + dx <= 8862:
                self.rect.x += dx
                self.run = True
            else:
                self.run = False
        if self.level == 2:
            if self.rect.left + dx >= 0 and self.rect.right + dx <= 9856:
                self.rect.x += dx
                self.run = True
            else:
                self.run = False
        
        if self.level == 3:
            if self.rect.left + dx >= 0 and self.rect.right + dx <= 7000:
                self.rect.x += dx
                self.run = True
            else: 
                self.run = False

        # Lượng y thay đổi
        self.rect.y += dy

    # Cập nhật lượng sang trái
    def move_left(self, vel): 
        # Về trái - velocity(vận tốc)
        self.x_vel = -vel
        # Kiểm tra mặt quay sang đâu
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    # Cập nhật lượng sang phải
    def move_right(self, vel): 
        # Về phải velocity
        self.x_vel = vel
        # Kiểm tra mặt sang đâu
        if (self.direction != "right"):
            self.direction = "right"
            self.animation_count = 0

    def draw_health_bar(self, win, offset_x, offset_y):
        # Màu sắc cho thanh máu (xanh lá cây cho phần còn, đỏ cho phần mất)
        full_health_color = (255, 0, 0)  # Red
        lost_health_color = (128, 128, 128)  # Gray

        # Kích thước và vị trí thanh máu
        bar_width = 80
        bar_height = 10
        bar_x = self.rect.x - 15 - offset_x
        bar_y = self.rect.y - 10 + offset_y

        # Tính toán lượng máu còn lại (dựa trên health / max_health)
        health_ratio = self.health / bar_width
        # Vẽ thanh máu mất trước (dưới cùng)
        pygame.draw.rect(win, lost_health_color, (bar_x, bar_y, bar_width, bar_height))

        # Vẽ thanh máu còn lại trên cùng
        pygame.draw.rect(win, full_health_color, (bar_x, bar_y, bar_width * health_ratio * 0.8, bar_height))
        # Thêm chữ hiển thị số lượng máu
        font = pygame.font.SysFont(None, 24)
        health_text = font.render(f"Health: {self.health}", True, (255, 255, 255))
        win.blit(health_text, (bar_x, bar_y - 20))
        
        name_text = font.render(f"Name: {self.user_name}", True, (255, 255, 255))
        win.blit(name_text, (bar_x , bar_y - 45))

    # addAnimation
    def update_sprite(self):
        # Mặc định
        sprite_sheet = "idle"

        # Lấy tên theo hành động
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        # self.GRAVITY * 2: x2 so với trọng lục -> Xác định thời điểm rơi nhanh
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0 and self.run == True:
            sprite_sheet = "run"
        
        # Lấy tên danh sách ảnh theo hành động
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        
        # Lấy danh sách ảnh theo hành động
        sprites = self.SPRITES[sprite_sheet_name]

        # Công thức tính lấy ảnh cho đúng và mượt:
        # Số animation đã diễn ra // chia cho delay ) % len: Không bị tràn
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        
        # Ảnh cẩn tìm
        self.sprite = sprites[sprite_index]

        # Tăng animation đã diễn ra
        self.animation_count += 1
        self.update()

    # 
    def update(self):
        # Tao rect mới từ rect cũ, -> topleft ở góc trên bên trái màn hình, giúp đảm bảo trục x, y -> quan trong trong việc 
        # cập nhật lại vị trí
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        # Tạo mặt nạ từ sprite -> để xác dịnh va chạm.
        self.mask = pygame.mask.from_surface(self.sprite)

    # Vòng lặp cập nhật ví trí nhân vật
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        if self.hit: 
            self.hit_count += 1
        if self.hit_count > fps * 2: 
            self.hit = False
            self.hit_count = 0

        if self.level == 1:
            if self.rect.x > 3000:
                self.round = 2
            if self.rect.x > 6000:
                self.round = 3

        if self.level == 2:
            if self.rect.x > 3000:
                self.round = 2
            if self.rect.x > 6000:
                self.round = 3
        if self.level == 3:

            if self.rect.x > 2000:
                self.round = 2
            if self.rect.x > 4000:
                self.round = 3
        self.fall_count += 1
        self.update_sprite()

    # Vẽ đối tượng lên cửa sỗ game
    def draw(self, win, offset_x, offset_y):
        # self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y + offset_y))
        # Tiếp tục tăng số lần rơi nếu chưa có dấu hiệu chạm
        self.draw_health_bar(win, offset_x, offset_y)
