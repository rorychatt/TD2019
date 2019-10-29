import pygame
import os
from .enemy import Enemy

class Mehike(Enemy):
    imgs = [pygame.image.load(os.path.join("Assets/vaenlased", "vaenlane_1.png"))]
    
    def __init__(self):
        super().__init__()
    
    