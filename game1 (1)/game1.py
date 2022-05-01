# Разработай свою игру в этом файле!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):
        '''перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
win_width = 700
win_height = 500
display.set_caption('Лабиринт')
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('g.jpg'), (win_width, win_height))
w1 = GameSprite('Brick_Wall.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('Brick_Wall.png',370, 100, 50, 400)
#Спрайты
packman = Player('Pacman_HD.png', 5, win_height - 80, 80, 80, 0, 0)
#Игровой цикл
run = True
while run:
    #Цикл срабатывает кадую 0.05 секунду
    time.delay(50)
    window.blit(back, (0,0))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -5
            elif e.key == K_RIGHT:
                packman.x_speed = 5
            elif e.key == K_UP:
                packman.y_speed == -5
            elif e.key == K_DOWN:
                packman.y_speed == 5
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed == 0
            elif e.key == K_UP:
                packman.y_speed == 0
            elif e.key == K_DOWN:
                packman.y_speed == 0
#рисуем объекты
w1.reset()
w2.reset()
packman.reset()

packman.update()

display.update()