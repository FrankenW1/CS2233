import pygame
import os
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'sprites')

#  from main import load_sprite_sheet, width, height, random, gameDisplay
colour = 0,0,255
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'boulder.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (640, 380)
        self.y_speed = 5

    def update(self):
        self.rect.x -= 300 * 0.0001

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False

    # def __init__(self, x, size, GroundHeight):
    #     self.x = x
    #     self.size = size
    #     self.GroundHeight = GroundHeight
    #
    # def draw(self, gameDisplay):
    #     self.objrect = pygame.draw.rect(gameDisplay, colour, [self.x, self.GroundHeight - self.size, self.size, self.size])
    #
    # def update(self, deltaTime, velocity):
    #     self.x -= velocity * deltaTime
    #
    # def checkOver(self):
    #     if self.x < 0:
    #         return True
    #     else:
    #         return False
