from engine.creatures import Entity
from engine.consts import *


class Player(Entity):
    def __init__(self, game_engine, x, y):
        super().__init__(game_engine, x, y, COLOR[PLAYER])
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
            self.move(self.velocity)

        if pressed_keys[pg.K_s]:
            self.move(-self.velocity)

        if pressed_keys[pg.K_LEFT]:
            self.rotate(-1)

        if pressed_keys[pg.K_RIGHT]:
            self.rotate(1)

    def look_around(self):
        vision = self.vision.collision()
        objects, env_to_draw = vision[:, 0], vision[:, 1]
        self.game_engine.env_to_draw = env_to_draw

    def draw(self, shift):
        x, y, rays, pg = super(Player, self).draw(shift)
        pg.draw.circle(self.game_engine.screen, self.clr, (x, y), self.radius)
        for rx, ry in rays:
            pg.draw.line(self.game_engine.screen, (255, 255, 0), (x, y), (rx, ry), 3)
