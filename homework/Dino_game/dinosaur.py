import pygame
dinocolour = 255, 255, 255
DINOHEIGHT = 40
DINOWIDTH = 20

# def load_image(name, colorkey=None):
#     try:
#         image = pygame.image.load(name)
#     except:
#         None
#
#     image = image.convert()
#
#     return image, image.get_rect()

class Dinosaur(pygame.sprite.Sprite):
    # def __init__(self):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.image.load(os.path.join(img_folder, 'dino.png')).convert()
    #     self.image.set_colorkey(BLACK)
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (0, 0)
    #     self.y_speed = 5
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        # self.image = pygame.image.load("/Testing/dino.png").convert_alpha()
        self.height = DINOHEIGHT
        self.width = DINOWIDTH
        self.surfaceHeight = surfaceHeight
    def jump(self):
        if(self.y == 0):
            self.yvelocity = 300
    def update(self, deltaTime):
        self.yvelocity += -500*deltaTime # This is Gravity
        self.y += self.yvelocity * deltaTime
        if self.y < 0: # if dino sinks into ground, make velocity and y = 0
            self.y = 0
            self.yvelocity = 0

    def draw(self, display):
        self.dinorect = pygame.draw.rect(display, dinocolour, [self.x, self.surfaceHeight - self.y - self.height + 60, self.width, self.height])
        # screen.blit(self.image,self.surfaceHeight)
