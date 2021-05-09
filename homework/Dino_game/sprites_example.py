import os
import sys
import pygame
import random
from pygame import *
from Dino_game import sprites

WIDTH = 800
HEIGHT = 600
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
sc_sz = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(sc_sz)
pygame.display.set_caption("My Game")

# set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'sprites')


class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'boulder.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 380)
        self.y_speed = 5

    def update(self):
        self.rect.x -= 5

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False
class flyer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'UFO.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 380)
        self.y_speed = 5

    def update(self):
        self.rect.x -= 5

    def draw(self):
        gameDisplay.blit(self.image, self.rect)

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'dino.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
newg = pygame.sprite.Group()
player = Player()
obstacle = Obstacles()
newg.add(obstacle)
all_sprites.add(player)
newp = pygame.sprite.Group()
fly = flyer()
newp.add(fly)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    all_sprites.update()
    newg.update()
    newp.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    newg.draw(screen)
    newp.draw(screen)
    pygame.display.flip()

pygame.quit()
