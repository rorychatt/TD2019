import pygame
import math

class Enemy:
    imgs = []
    
    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.healt = 1
        self.vel = 3
        self.path = [(7, 161), (364, 162), (422, 237), (429, 348), (367, 384), (180, 400), (135, 489), (165, 582), (271, 595), (462, 596), (659, 605), (800, 605), (903, 598), (929, 537), (935, 397), (946, 188), (1152, 181), (1359, 194)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        
    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        if self.animation_count > len(self.imgs):
            self.animation_count = 0
            
        win.blit(self.img, (self.x, self.y))
        self.move
        
        
    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        x1,y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1400, 194)
        else:
            x2,y2 = self.path[self.path_pos+1]
        self.dis += math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
        dirn = (x2-x1,y2-y1)
        
        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.dis += math.sqrt((move_x-x1)**2 + (move_y-y1)**2)
        
        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path.pos += 1
        
        self.x = move_x
        self.y = move_y
            
    
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return true
        