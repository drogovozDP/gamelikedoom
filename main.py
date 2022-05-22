from engine.game_engine import GameEngine


if __name__ == '__main__':
    display_none = False
    game_engine = GameEngine(width=800, height=600, display_none=display_none)
    game_engine.run()
