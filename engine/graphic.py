from engine.consts import *


class Graphic:
    def __init__(self, game_engine, width, height):
        self.game_engine = game_engine
        self.width = width
        self.height = height
        self.set_max_xy()
        self.set_cell_wh()

    def draw_player_view(self):
        width = WIDTH / len(self.game_engine.player_view)
        for i, view in enumerate(self.game_engine.player_view):
            height = HEIGHT / (view[RAY_LEN] * view[RAY_COS]) * WALL_HEIGHT
            self.game_engine.pg.draw.rect(
                self.game_engine.screen,
                COLOR[WALL],
                self.game_engine.pg.Rect(
                    width * i, (HEIGHT - height) / 2,
                    width, height
                )
            )

    def draw_environment(self):
        for obj in self.game_engine.environment:
            obj.draw(self.cell_pad)
        self.game_engine.player.draw(self.cell_pad)

    def set_max_xy(self):
        self.max_y = len(LEVELS[self.game_engine.lvl])
        self.max_x = max([len(row) for row in LEVELS[self.game_engine.lvl]])

    def set_cell_wh(self):
        """
        Cretas cell_size for cell width and height and cell_pad for padding
        """
        self.cell_size = min(self.height / self.max_y, self.width / self.max_x)
        self.cell_pad = ((self.width - self.max_x * self.cell_size) / 2, 0) \
            if self.max_x * self.cell_size < self.width else \
            (0, (self.height - self.max_y * self.cell_size) / 2)
