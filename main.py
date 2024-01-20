# 1 - перший рівень лабіринту
# 2 - другий рівень лабіринту
# 3 - змійка
# 0 - вихід в меню
#
#
#


from pygame import *
import random

win_height = 500
win_width = 700

COLOR_RED = 255, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_BLACK = 0, 0, 0

font.init()
font1 = font.SysFont("Arial", 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 40:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 40:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((win_width, win_height))
display.set_caption("Multi Game")

bg = transform.scale(image.load("background.jpg"), (700, 500))

player = Player("player.png", 20, 325, 40, 40, 5)
BASIC_X = 20 # base position x for the player
BASIC_Y = 325 # base position y for the player
BASIC_RECT = BASIC_X, BASIC_Y
win_point = GameSprite("treasure.png", 580, 410, 80, 80, 0)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)

apple = GameSprite("apple.png", 100, 100, 40, 40, 0)

MENU = 0
MAZE_1LVL = 1
MAZE_2LVL = 2
MAZE_3LVL = 3
SNAKE = 4

current_state = MENU

score = 0
game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))

    if current_state == MENU:
        keys = key.get_pressed()

        if keys[K_1] and current_state != MAZE_1LVL:
            current_state = MAZE_1LVL
        elif keys[K_2] and current_state != MAZE_2LVL:
            current_state = MAZE_2LVL
        elif keys[K_3] and current_state != MAZE_3LVL:
            current_state = MAZE_3LVL
        elif keys[K_4] and current_state != SNAKE:
            current_state = SNAKE

    elif current_state == MAZE_1LVL:
        # print("Гра у лабіринт - рівень 1")

        player.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        win_point.reset()  # Виводимо скарб

        player.reset()

        # defeat
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # win
        elif sprite.collide_rect(player, win_point):
            current_state = MENU  # Повертаємося в меню
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # реалізація виходу в меню
        keys = key.get_pressed()
        if keys[K_0] and current_state != MENU:
            current_state = MENU

            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325



    elif current_state == MAZE_2LVL:
        # print("Гра у лабіринт - рівень 2")
        # Додайте код для другого рівня лабіринту, включаючи вивід win_point
        
        player.update()

        
        w1.draw_wall()

        w2.draw_wall()
        w3.draw_wall()

        w4.rect.y = 35
        w4.draw_wall()

        w5.draw_wall()

        w6.rect.y = 140
        w6.draw_wall()

        w7.draw_wall()

        win_point.reset()  # Виводимо скарб

        player.reset()

        # defeat
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # win
        elif sprite.collide_rect(player, win_point):
            current_state = MENU  # Повертаємося в меню
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # реалізація виходу в меню
        keys = key.get_pressed()
        if keys[K_0] and current_state != MENU:
            current_state = MENU

            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

            w4.rect.y = 130
            w6.rect.y = 20

        
    
    elif current_state == MAZE_3LVL:
        # print("Гра у лабіринт - рівень 3")

        player.update()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        w5.rect.y = 50
        w5.draw_wall()

        w6.draw_wall()
        # w7.draw_wall()

        win_point.reset()  # Виводимо скарб

        player.reset()

        # defeat
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6):
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # win
        elif sprite.collide_rect(player, win_point):
            current_state = MENU  # Повертаємося в меню
            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

        # реалізація виходу в меню
        keys = key.get_pressed()
        if keys[K_0] and current_state != MENU:
            current_state = MENU

            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325

            w5.rect.y = 130



    elif current_state == SNAKE:
        # print("Гра змійка")

        window.blit(apple.image, (apple.rect.x, apple.rect.y))

        player.update()

        player.reset()

        if player.rect.colliderect(apple.rect):
            apple.rect.x = random.randint(10, win_width - 20)
            apple.rect.y = random.randint(40, win_height - 35)
            score += 1

        score_text = font1.render("Рахунок: " + str(score), 1, (COLOR_BLACK))
        window.blit(score_text, (10, 5))

        # реалізація виходу в меню
        keys = key.get_pressed()
        if keys[K_0] and current_state != MENU:
            current_state = MENU

            score = 0

            player.rect.x = BASIC_X # 20
            player.rect.y = BASIC_Y # 325
        
    display.flip()
    clock.tick(FPS)

