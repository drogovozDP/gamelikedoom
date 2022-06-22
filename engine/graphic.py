from engine.consts import *


class Graphic:
    def __init__(self, game_engine, width, height):
        self.game_engine = game_engine
        self.width = width
        self.height = height
        self.set_max_xy()
        self.set_cell_wh()

    def draw_environment(self):
        # print(self.game_engine.env_to_draw)
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
        # self.cell_pad = (0, 0)
