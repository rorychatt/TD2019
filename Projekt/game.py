import pygame
import os
from Vaenlased.enemy_1 import Mehike
from Towers.Vibulane import vibulane


class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Mehike()]
        self.towers = [vibulane(300,300)]
        self.lives = 100
        self.money = 100
        self.bg = pygame.image.load(os.path.join("Assets", "taust.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height))
        self.clicks = []
        self.pause = False
        
    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
            if not self.pause:
                to_del = []
                for en in self.enemys:
                    en.move()
                    if en.x > 1390:
                        to_del.append(en)
                for tw in self.towers:
                    tw.attack(self.enemys)

                for d in to_del:
                    self.lives -= 1
                    self.enemys.remove(d)
            self.draw()
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for en in self.enemys:
            en.draw(self.win)
        for tw in self.towers:
            tw.draw(self.win)


        pygame.display.update()
        
g = Game()
g.run()