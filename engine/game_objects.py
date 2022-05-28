from engine.consts import *


class GameObject:
    def __init__(self, game_engine, x, y, clr):
        self.game_engine = game_engine
        self.x = x
        self.y = y
        self.clr = clr

    def collision(self, shape):
        for obj in self.game_engine.environment:
            if obj.check_collision(shape):
                return True
        return False

    def check_collision(self, shape):
        pass

    def draw(self, shift):
        pg = self.game_engine.pg
        x, y = self.x + shift[0], self.y + shift[1]
        return x, y, pg


class Wall(GameObject):
    def __init__(self, game_engine, x, y, clr, size):
        super().__init__(game_engine, x, y, COLOR[clr])
        self.size = size

    def check_collision(self, shape):
        wx, wy, ws = self.x, self.y, self.size
        for dot in shape:
            x, y, _ = dot
            if wx <= x <= wx + ws and wy <= y <= wy + ws and self.clr == COLOR[WALL]:
                return True
        return False

    def draw(self, shift):
        x, y, pg = super(Wall, self).draw(shift)
        pg.draw.rect(self.game_engine.screen, self.clr, pg.Rect(x, y, self.size, self.size))
