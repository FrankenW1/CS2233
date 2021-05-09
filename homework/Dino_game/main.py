# DONT FORGET TO FIX GROUND

import pygame
from pygame import *
import os
import random


pygame.init() # starts up game

# ---Initializing Game---
size = width,height = 640,480
gameDisplay = pygame.display.set_mode(size) # makes screen
GROUND_HEIGHT = 360
xPos = 0
yPos = 0
# --- NEW LOAD ---
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'sprites')

FPS = 30
clock = pygame.time.Clock()
gravity = 0.6

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Scoreboard():
    def __init__(self,x=-1,y=-1):
        self.score = 0
        self.tempimages,self.temprect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y

    def draw(self):
        gameDisplay.blit(self.image,self.rect)

    def update(self,score):
        score_digits = extractDigits(score)
        self.image.fill(black)
        for s in score_digits:
            self.image.blit(self.tempimages[s],self.temprect)
            self.temprect.left += self.temprect.width
        self.temprect.left = 0

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'boulder.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 320)
        self.y_speed = 5
        self.x = x
    def update(self):
        self.rect.x -= 5

    def draw(self):
        gameDisplay.blit(self.image, self.rect)

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False

class Obstacle2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'Roid.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 320)
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


class flyer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'UFO.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 140)
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

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'Flyno.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (70, 320)
        self.y = 270
        self.jumpCount = 10
        self.isJumping = False
        self.movemnt = 0
    def draw(self):
        gameDisplay.blit(self.image, self.rect)

    def update(self):
        self.rect.y = self.y
        keystate = pygame.key.get_pressed()
        if self.y == 110:
            while self.y is not 270:
                self.isJumping = True
        if keystate[pygame.K_SPACE] and self.isJumping == False and self.y > 110:
            self.y -= 5
        else:
            if self.y < 270:
                self.y += 5
            self.isJumping = False

    def jump(self):
        self.movemnt = 0




# --- OLD LOAD FOR SCOREBOARD---
def load_image(name, sizex = -1, sizey = -1, colorkey = None):
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

def load_sprite_sheet(sheetname, nx, ny, scalex = -1, scaley = -1, colorkey = None):
    fullname = os.path.join('sprites', sheetname)
    sheet = pygame.image.load(fullname)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites,sprite_rect

def extractDigits(number):
    if number > -1:
        digits = []
        i = 0
        while(number/10 != 0):
            digits.append(number%10)
            number = int(number/10)

        digits.append(number%10)
        for i in range(len(digits),5):
            digits.append(0)
        digits.reverse()
        return digits
# --- END OLD LOAD FOR SCOREBOARD ---

# # ---Game Colors---
black = 0,0,0
# white = 255, 255, 255



def gameplay():
        # ---Obstacle---
    MINGAP = 200
    VELOCITY = 300
    MAXGAP = 600
    obs1 = []
    obs2 = []
    obs3 = []
    flyers = []
    num_of_obstacles = 4
    lastObstacle = pygame.sprite.Group()
    lastobs = width
    SCORE = 0
    obstaclesize = 50
    Boulder = pygame.sprite.Group()
    Roid = pygame.sprite.Group()

    UFO = pygame.sprite.Group()

    # ---Create Dino---
    player = Dinosaur()
    Boldor = Obstacles(lastobs)
    Fly = flyer()
    Bot = Obstacle2()

    # ---Making LastFrame---
    lastFrame = pygame.time.get_ticks()

    # ---Game Colors---
    black = 0,0,0
    white = 255, 255, 255

    # ---Clock---

    scb = Scoreboard()
    gameOver = False
    gameOn = True
    while gameOn: # makes frames of games, the loop that runs this
        clock.tick(FPS)
        SCORE += 1

        for event in pygame.event.get(): # check for actions
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: # if user presses keyboard
                if event.key == pygame.K_SPACE: # if that key is space
                    player.jump()

    # --- GAME PAUSE AND RESTART LOOP---
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOn = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player.isJumping = True
                    if event.key == pygame.K_ESCAPE:
                        gameOn = False
                        gameOver = False
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        gameOver = False
                        gameplay()
    # --- GAME PAUSE AND RESTART LOOP END---
        if pygame.display.get_surface() != None:
            gameDisplay.fill(black)
            # Boldor.draw()
            # Bot.draw()
            # Fly.draw()
            player.draw()
        if pygame.display.get_surface() == None:
            print('NO DISPLAY SURFACE')


        #---COLLISION---
        # if pygame.sprite.collide_mask(player, Boldor):
        #     gameOver = True
        for b in Boulder:
            Boldor.update()
            if pygame.sprite.collide_mask(player, b):
                gameOver = True
        for r in Roid:
            Roid.update()
            if pygame.sprite.collide_mask(player, r):
                gameOver = True
        for u in UFO:
            UFO.update()
            if pygame.sprite.collide_mask(player, u):
                gameOver = True

        # ---OBJECT SPAWN---
        zed = random.randint(0, 250)
        if zed == 100:
            obs1.append(Obstacles(lastobs))
        if zed == 150:
            obs2.append(Obstacle2())
        if zed == 2:
            obs3.append(flyer())
        # for i in range(random.randint(0, 1)):
        #         obs1.append(Obstacles(lastobs))
        for obs in obs1:
            obs.update()
            obs.draw()
            if pygame.sprite.collide_mask(player, obs):
                gameOver = True
        for obs in obs2:
            obs.update()
            obs.draw()
            if pygame.sprite.collide_mask(player, obs):
                gameOver = True
        for obs in obs3:
            obs.update()
            obs.draw()
            if pygame.sprite.collide_mask(player, obs):
                gameOver = True


        player.update()

    # --- COLLISION DETECTION END---




            # draws rectangle at coordinate 30,30 with width of 40 and height of 50
        pygame.draw.rect(gameDisplay, white, [0,GROUND_HEIGHT, width, height - GROUND_HEIGHT])



        scb.update(SCORE)
        scb.draw()
        pygame.display.update() # updates each frame





if __name__ == '__main__':
    gameplay()

