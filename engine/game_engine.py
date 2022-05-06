import pygame as pg
from engine.graphic import Graphic
from engine.consts import *


class GameEngine:
    def __init__(self, width, height, display_none=False):
        self.display_none = display_none
        self.pg = pg
        self.screen = self.pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.running = True
        self.lvl = 'lvl1'
        self.graphic = Graphic(self, width, height)

    def run(self):
        while self.running:
            self.player_events()
            self.game_events()
            self.update_screen()

    def player_events(self):
        """
        All player's action will be processed here
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

        # player's input keys
        pressed_keys = self.pg.key.get_pressed()
        if pressed_keys[self.pg.K_ESCAPE]:
            self.running = False

    def update_screen(self):
        """
        Redraw screen
        """
        if self.display_none:
            return
        self.clock.tick()
        self.screen.fill(COLOR['background'])
        self.graphic.draw_environment()
        self.pg.display.update()

    def game_events(self):
        """
        There will be logic for enemies
        """
        pass

