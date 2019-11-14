import pygame
from .Tower import tower
import os
import math

class vibulane(tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.vibu_imgs = []
        self.vibu_count = 0
        self.range = 200
        self.inRange = False

        #tower images
        for x in range(5):
            add_str = str(x)
            if x < 3:
                self.tower_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("Assets/Towers", "tower_1_" + add_str + ".png")),
                    (64, 64)))
        #vibulane images
        for x in range(5):
            add_str = str(x)
            if x < 1:
                self.vibu_imgs.append(pygame.transform.scale(
                    pygame.image.load(os.path.join("Assets/Towers", "vibulane_" + add_str + ".png")),
                    (32, 32)))

    def draw(self, win):
        super().draw(win)
        vibu = self.vibu_imgs[self.vibu_count]
        win.blit(vibu, ((self.x + self.width/2) - (vibu.get_width()/2), (self.y - vibu.get_height()*2)))
        if self.inRange: # kui on animatsioon
            # self.vibu_count += 1
            #if self.vibu_count >= len(self.vibu_imgs):
            #    self.vibu_count = 0
            pass

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x-x)**2 + (self.y-y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)