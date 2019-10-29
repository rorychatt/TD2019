import pygame
import os
from Vaenlased.enemy_1 import Mehike

class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Mehike()]
        self.towers = []
        self.lives = 100
        self.money = 1000
        self.bg = pygame.image.load(os.path.join("Assets", "taust.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height))
        self.clicks = []
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
            self.draw()
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for en in self.enemys:
            en.draw(self.win)
            
        pygame.display.update()
        
g = Game()
g.run()