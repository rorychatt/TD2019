import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(10):
    add_str = str(x)
    if x < 4:
        imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/Vaenlased", "vaenlane_1_" + add_str + ".png")),
        (64, 64)))

class Mehike(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Mehike"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]