from typing import Any
import pygame
pygame.init()


pygame.mixer.music.load('audio/pacman_melody.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
class GameSprite(pygame.sprite.Sprite):
    # создание класса спарайтов
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # создание подкласса игрока и его функций
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    def update(self):
        if self.rect.x <= win_width-80 and self.x_speed > 0 or self.rect.x > 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = pygame.sprite.spritecollide(self,barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = p.rect.left
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = p.rect.right
        if self.rect.y <= win_height-80 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = p.rect.bottom

    def fire(self):
        # добавление спрайта пули
        bullet = Bullet('pictures/tap.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    # создание класса призрака вместе его движения и функции

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y,)
        self.speed = player_speed
        self.side = 'left'

    def update(self):
        if self.rect.x <= 420:
            self.side = 'right'
        if self.rect.x >= win_width-85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Bullet(GameSprite):
    # создание класса пули его функций и убийства врага
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y,)
        self.speed = player_speed
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()



        
        
                                   
# создание окна
win_width = 900
win_height = 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('PAC-MAN')
back = (0, 0, 0)
                            #  1 расположение по x - левее + правее
                            # 2 расположение по y - вниз + вверх
                            # 3 длина
                            # 4 ширина
# создание платформ                    

barriers = pygame.sprite.Group()
bullets = pygame.sprite.Group()
monsters = pygame.sprite.Group()

w1 = GameSprite('pictures/stenka.png',117, 250, 295, 40)

w2 = GameSprite('pictures/stena.png',370, 100, 60, 700)

w3 = GameSprite('pictures/stenka.png',-20, 380, 300, 40)

w4 = GameSprite('pictures/stenka.png',-20, 130, 300, 40)


w5 = GameSprite('pictures/stena.png',100, 40, 300, 30)

w6 = GameSprite('pictures/stena.png',-20, 130, 300, 40)

w7 = GameSprite('pictures/stena.png',-20, 130, 300, 40)

w8 = GameSprite('pictures/stena.png',-20, 130, 300, 40)

w9 = GameSprite('pictures/stena.png',-20, 130, 300, 40)

w10 = GameSprite('pictures/stena.png',-20, 130, 300, 40)
# группы стен для облегчения работы с ними
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
# barriers.add(w5)
# barriers.add(w6)
# barriers.add(w7)
# barriers.add(w8)
# barriers.add(w9)
# barriers.add(w10)


packman1 = ('pictures/my_pacman_right.png')
packman = Player(packman1 , 5, 420, 40, 40, 0, 0)

# up = packman
# down = pygame.transform.flip(packman, 0, 1)
# left = pygame.transform.rotate(packman, 90)
# right = pygame.transform.rotate(packman, -90)

# Rpackman = up
# редактор призраков 
monster1 = Enemy('pictures/blue ghost.png', win_width - 80, 180, 87, 80, 5)
monster2 = Enemy('pictures/red ghost.png', win_width - 150, 340, 100, 100, 5)
monster3 = Enemy('pictures/ghost 3.png', win_width - 300, 50, 50, 50, 5)
final_sprite = GameSprite('pictures/pac_finish.png', win_width - 75, win_height - 80, 80, 100)
# группы для работы с призраками для облегчения работы с ними
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
finish = False



# движок пакмэна
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            # pygame.mixer.music.load('audio/waka waka.mp3')
            # pygame.mixer.music.play(-1)
            # pygame.mixer.music.set_volume(0.1)
            if e.key == pygame.K_a:
                packman1 = ('my_pacman_left.png')
                packman.x_speed = -8
                pygame.mixer.music.load('audio/waka waka.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            elif e.key == pygame.K_d:
                pygame.mixer.music.load('audio/waka waka.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
                packman.x_speed = 8
            elif e.key == pygame.K_w:
                pygame.mixer.music.load('audio/waka waka.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
                packman.y_speed = -8
            elif e.key == pygame.K_s:
                pygame.mixer.music.load('audio/waka waka.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
                packman.y_speed = 8
            elif e.key == pygame.K_e:
                pygame.mixer.music.load('audio/shoot.mp3')
                pygame.mixer.music.play(1)
                pygame.mixer.music.set_volume(0.1)
                packman.fire()
        elif e.type == pygame.KEYUP:
            pygame.mixer.music.pause()
            if e.key == pygame.K_a:
                pygame.mixer.music.pause()
                packman.x_speed = 0
            elif e.key == pygame.K_d:
                pygame.mixer.music.pause()
                packman.x_speed = 0
            elif e.key == pygame.K_w:
                pygame.mixer.music.pause()
                packman.y_speed = 0
            elif e.key == pygame.K_s:
                pygame.mixer.music.pause()
                packman.y_speed = 0
    if finish == False:
        window.fill(back)
        barriers.draw(window)
        bullets.update()
        bullets.draw(window)
        final_sprite.reset()
        packman.reset()
        packman.update()

        pygame.sprite.groupcollide(bullets, barriers, True, False)

        if not(pygame.sprite.groupcollide(monsters, bullets, True, True)):

            monsters.draw(window)
            monsters.update()
        else:
            pygame.mixer.music.load('audio/dead.mp3')
            pygame.mixer.music.play(1)


        if pygame.sprite.spritecollide(packman, monsters, True):
            finish = True
            img = pygame.image.load('pictures/you dead.jpg')
            window.fill((0, 0, 0))
            window.blit(pygame.transform.scale(img, (win_width, win_height)), (0, 0))
        if pygame.sprite.collide_rect(packman, final_sprite):
            finish = True
            img = pygame.image.load('pictures/thumb.jpg')
            window.fill((0, 0, 0))
            window.blit(pygame.transform.scale(img, (win_width, win_height)), (0, 0))
    pygame.time.delay(25)

    pygame.display.update()

