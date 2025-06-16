from pygame import *
from time import sleep
'''Required classes'''
#parent class for sprites
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
color_back = (10, 52, 99)
window.fill(color_back)

ball = GameSprite('Ping-Pong/ball.png', 200, 200, 4, 40, 40)
player1 = Player('Ping-Pong/trash.png', 30, 200, 4, 50, 150)
player2 = Player('Ping-Pong/good.png', 615, 200, 4, 50, 150)


clock = time.Clock()
finish = False
game = True
speed_x = 3
speed_y = 3

player1_point = 0
player2_point = 0

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 LOSE!', True, (180,0,0))
lose2 = font.render('Player 2 LOSE!', True, (180,0,0))
win1 = font.render('Player 1 WIN!', True, (0,180,0))
win2 = font.render('Player 2 WIN!', True, (0,180,0))
cooldown_collision = 15
cooldown_timer = 15
while finish != True:
    for e in event.get():
        if e.type == QUIT:
            finish = True
    if game:
        window.fill(color_back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.update_l()
        player2.update_r()
        if cooldown_collision <= 0:
            if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
                speed_x *= -1.05
                speed_y *= 1.05
            if ball.rect.y > win_height - 50 or ball.rect.y < 0:
                speed_y *= -1.05
            cooldown_collision = 15
        cooldown_collision -= 1 
        if ball.rect.x > win_width - 50:
            player1_point += 1
            if player1_point >= 5:
                window.blit(win1, (200, 200))
                game = False
            else:
                window.blit(lose2, (200,200))
                display.update()
                time.delay(2000)
                ball.rect.x = win_width//2
                ball.rect.y = win_height//2
                speed_x = -4
                speed_y = 4
        if ball.rect.x < 0:
            ball.rect.x = 200
            ball.rect.y = 200
            player2_point += 1
            if player2_point >= 5:
                window.blit(win2, (200, 200))  
                game = False
            else:
                window.blit(lose1, (200,200))
                display.update()
                time.delay(2000)
                ball.rect.x = win_width//2
                ball.rect.y = win_height//2
                speed_x = 4
                speed_y = 4

        point_display = font.render(f'Player 1: {player1_point} - Player 2: {player2_point}', True, (255,255,255))
        window.blit(point_display, (220, 20))
        player1.reset()
        player2.reset()
        ball.reset()
    
    display.update()
    clock.tick(60)