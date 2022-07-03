from engine.game_engine import GameEngine
from engine.consts import WIDTH, HEIGHT


if __name__ == '__main__':
    display_none = False
    game_engine = GameEngine(width=WIDTH, height=HEIGHT, display_none=display_none)
    game_engine.run()
