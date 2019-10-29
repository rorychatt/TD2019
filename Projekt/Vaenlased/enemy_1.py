import pygame
import os
from .enemy import Enemy

class Mehike(Enemy):
    imgs = []
    for x in range(2):
        add_str = str(x)
        imgs.append(pygame.image.load(os.path.join("Assets/Vaenlased","Vaenlane_1_" +add_str +".png")))
    
    def __init__(self):
        super().__init__()
    
    