from engine.creatures import Entity
from engine.consts import *


class Player(Entity):
    def __init__(self, game_engine, x, y):
        super().__init__(game_engine, x, y, COLOR[PLAYER])
        self.size = self.game_engine.graphic.cell_size // 2
        self.velocity = PLAYER_VELOCITY

    def input_keys(self):
        pg = self.game_engine.pg
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_engine.running = False

        # player's input keys
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[pg.K_ESCAPE]:
            self.game_engine.running = False

        if pressed_keys[pg.K_w]:
            self.move(0, self.velocity)

        if pressed_keys[pg.K_s]:
            self.move(0, -self.velocity)

        if pressed_keys[pg.K_a]:
            self.rotate(1)

        if pressed_keys[pg.K_d]:
            self.rotate(-1)

    def draw(self, shift):
        x, y, rx, ry, pg = super(Player, self).draw(shift)
        pg.draw.circle(self.game_engine.screen, self.clr, (x, y), self.size)
        pg.draw.line(self.game_engine.screen, (255, 255, 0), (x, y), (rx, ry), 3)
