import pygame
import os
from Vaenlased.enemy_1 import Mehike
from Towers.Vibulane import vibulane
import time
pygame.font.init()

lives_img = (pygame.transform.scale(pygame.image.load(os.path.join("Assets/Menu", "süda.png")), (60,60)))

class Game:
    def __init__(self):
        self.width = 1366
        self.height = 768
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Mehike()]
        self.towers = [vibulane(300,300), vibulane(500,300)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("Assets", "taust.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height))
        self.clicks = []
        self.pause = False
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("hobostdopentype", 64) # texti suurus
        self.selected_tower = None

    def run(self):
        run = True
        clock = pygame.time.Clock()
        
        while run:
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                self.enemys.append(Mehike())
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for tw in self.towers:
                        if tw.click(pos[0], pos[1]):
                            tw.selected = True
                            self.selected_tower = tw
                        else:
                            tw.selected = False

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

                if self.lives <= 0:
                    print("You Lose")
                    run = False
            self.draw()
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for en in self.enemys:
            en.draw(self.win)

        for tw in self.towers:
            tw.draw(self.win)
            tw.draw_range(self.win)
        #elud
        text = self.life_font.render(str(self.lives), 1, (0,0,0))

        life = lives_img
        start_x = self.width - life.get_width() - 5
        self.win.blit(text, (start_x-text.get_width()-10, 10))
        self.win.blit(life, (start_x, 10))

        pygame.display.update()
    def draw_menu(self):
        pass
        
g = Game()
g.run()