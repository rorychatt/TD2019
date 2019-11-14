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

    def draw(self, win):
        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x-img.get_width()//2, self.y-img.get_height()//2))

    def click(self, X, Y):
        #kas on valitud
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def upgrade(self):
        self.level += 1

    def upgrade_cost(self):
        return self.price[self.level-1]

    def stage_up(self):
        pass

    def move(self):
        self.x = x
        self.y = y

    def sell(self):
        return self.sell[self.level-1]