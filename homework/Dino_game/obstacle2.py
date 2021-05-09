import pygame

colour = 0,255,0
class Droid:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'Roid.png')).convert()
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
