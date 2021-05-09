import pygame

class Parent:
    def __init__(self, x_cord: int = 0, y_cord: int = 0, length = 30, width = 30):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.length = length
        self.width = width


    def coordInArea(self, coord:list):
        x = self.x_cord
        y = self.y_cord
        a = self.length
        b = self.width
        v = coord[0]
        w = coord[1]
        if x<=v<=x+a and y<w<y+b :
            return True
        return False

