from engine.game_objects import GameObject
from engine.consts import *


class Player(GameObject):
    def __init__(self, game_engine, x, y):
        super().__init__(game_engine, x, y, COLOR[PLAYER])
        self.size = self.game_engine.graphic.cell_size // 2

    def input_keys(self):
        pg = self.game_engine.pg
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_engine.running = False

        # player's input keys
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[pg.K_ESCAPE]:
            self.game_engine.running = False

    def draw(self, shift):
        x, y, pg = super(Player, self).draw(shift)
        pg.draw.circle(self.game_engine.screen, self.clr, (x, y), self.size)
