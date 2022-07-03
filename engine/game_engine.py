import pygame as pg
from engine.graphic import Graphic
from engine.consts import *
from engine.player import Player
from engine.game_objects import Wall


class GameEngine:
    def __init__(self, width, height, display_none=False):
        self.display_none = display_none
        self.pg = pg
        self.screen = self.pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.running = True
        self.lvl = 'lvl1'
        self.player_view = []
        self.graphic = Graphic(self, width, height)
        self.environment = self.generate_environment()
        self.player = Player(self, x=self.graphic.cell_size * 1.5, y=self.graphic.cell_size * 1.5)

    def generate_environment(self):
        environment = []
        size = self.graphic.cell_size
        for y, row in enumerate(LEVELS[self.lvl]):
            for x, cell in enumerate(row):
                if cell != FLOOR:
                    environment.append(Wall(self, x * size, y * size, cell, size))
        return environment

    def run(self):
        while self.running:
            self.player_events()
            self.game_events()
            self.update_screen()

    def player_events(self):
        """
        All player's action will be processed here
        """
        self.player.input_keys()
        self.player.look_around()

    def update_screen(self):
        """
        Redraw screen
        """
        if self.display_none:
            return
        self.clock.tick(self.FPS)
        self.screen.fill(COLOR['background'])
        # self.graphic.draw_environment()
        self.graphic.draw_player_view()
        self.pg.display.update()

    def game_events(self):
        """
        There will be logic for enemies
        """
        pass

