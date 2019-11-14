import pygame


class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell = (0,0,0)
        self.price = (0,0,0)
        self.stage = 1
        self.level = 1
        self.xp = 0
        self.selected = False
        self.menu = None
        self.tower_imgs = []
        self.damage = 1
        self.range = 0

    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def draw_range(self, win):
        if self.selected:
            print("run")
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            win.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        # kas on valitud
        img = self.tower_imgs[self.level - 1]
        if X <= self.x - img.get_width() // 2 + 70 and X >= self.x - img.get_width() // 2:
            if Y <= self.y + 60 - img.get_height() // 2 and Y >= self.y - img.get_height() // 2:
                return True
        return False

    def upgrade(self):
        self.level += 1
        self.damage += 1

    def upgrade_cost(self):
        return self.price[self.level-1]

    def stage_up(self):
        pass

    def move(self):
        self.x = x
        self.y = y

    def sell(self):
        return self.sell[self.level-1]