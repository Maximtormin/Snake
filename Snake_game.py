from random import randint
from pygame import *
font.init()
font1 = font.SysFont('Arial',80)
win = font1.render('победа',True ,(255,255,255))
lose = font1.render('луз',True,(100,0,0))
font2 = font.SysFont('Arial',36)
width = 700
height =500
window = display.set_mode((width, height))
display.set_caption("Змейка")
background = transform.scale(image.load('grass.jpg'), (width, height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x ,player_y, player_speed,size_x , size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        if e.type == KEYUP:
            if e.key==K_w:
                self.rect.y -= self.speed
            if e.key==K_s:
                self.rect.y += self.speed
            if e.key==K_a:
                self.rect.x -= self.speed
            if e.key==K_d:
                self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        '''self.rect.y+=self.speed'''
        global lost
        if self.rect.y > height:
            self.rect.x = randint(80, 80)
            self.rect.y = randint(80, 80)
        
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y +=self.speed
        if self.rect.y <0:
            self.kill()



lost = 0
score = 0
finish = False
run = True
FPS = 60
clock = time.Clock()
snake = Player("zz.jpg", 100, 100 , 2,55,55)
apple = Enemy('apple.png', randint(0, 300), randint(0, 300), 2,65,65)

'''monsters = sprite.Group()
asteroids = sprite.Group()
for a in range(1, 3):
    asteroid = Enemy('asteroid.png', randint(80, 620), -40, randint(1, 7), 80, 80)
    asteroids.add(asteroid)
for i in range(1,5):
    monster = Enemy('ufo.png', randint(80,width-80),-40,randint(1,3),65,65)
    monsters.add(monster)

    bullets = sprite.Group()'''

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background,(0, 0))

        if sprite.collide_rect(snake, apple):
            apple.kill()
            apple = Enemy('apple.png', randint(0, 300), randint(0, 300), 2,65,65)

        snake.update()
        snake.reset()
        apple.update()
        apple.reset()
        display.update()

    clock.tick(FPS)

