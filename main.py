from pygame import *
import random

win_height = 500
win_width = 700

COLOR_RED = 255, 0 , 0
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

    # function for output player
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # function for moving the player
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

# basic setting for window(size of window, window caption)
window = display.set_mode((win_width, win_height))
display.set_caption("Multi Game")

# create and settings background
bg = transform.scale(image.load("background.jpg"), (700, 500))

# create and settings for player and win point
player = Player("player.png", 325, 225, 40, 40, 5)

#sprites for treasure - win point
win_point = GameSprite("treasure.png", 580, 420, 60, 60, 0 )


# sprites for snake (activate snake game by number 5)
apple = GameSprite("apple.png", 100, 100, 40, 40, 0)

# game settings
score = 0
game = True
finish = False
clock = time.Clock()
FPS = 60

# game 
while game:
    # keys and keyboard
    for e in event.get():
        # here we implement exit from the game
        if e.type == QUIT:
            game = False

    if not finish:
        # Screen cleaning
        window.fill((0, 0, 0))
    
        # screen output
        window.blit(bg, (0, 0))

        player.update()
        player.reset()

        win_point.reset()

        window.blit(apple.image, (apple.rect.x, apple.rect.y))  # output apple

        # check collision player and apple
        if player.rect.colliderect(apple.rect):
            apple.rect.x = random.randint(10, win_width - 10)
            apple.rect.y = random.randint(40, win_height - 30)
            score += 1
            
        # output score
        score_text = font1.render("Рахунок: " + str(score), 1, (COLOR_BLACK))
        window.blit(score_text, (10, 5))
 


        display.flip()

    clock.tick(FPS) # you can use time.delay(50) 