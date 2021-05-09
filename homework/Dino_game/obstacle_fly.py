import pygame

colour = 255,0,0
class flyer:
    def __init__(self, x, size, GroundHeight):
        self.x = x
        self.size = size
        self.GroundHeight = GroundHeight - 35

    def draw(self, gameDisplay):
        self.objrect = pygame.draw.rect(gameDisplay, colour, [self.x, self.GroundHeight - self.size, (self.size / 2), (self.size / 2)])

    def update(self, deltaTime, velocity):
        self.x -= velocity * deltaTime

    def checkOver(self):
        if self.x < 0:
            return True
        else:
            return False
