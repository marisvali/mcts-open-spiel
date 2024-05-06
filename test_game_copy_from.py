# This is required for type annotation to work for this line: def copyFrom(game: Game):
from __future__ import annotations
from game import Game
import numpy as np
from absl import app
import pyspiel
from policy import Policy_Player_MCTS
from node import Node

def main(_):
    np.random.seed(19)
    
    game = Game()
    for _ in range(3):
        game.step(game.actions()[0])
    
    game2 = Game()
    game2.copyFrom(game)

    print(str(game.state))
    print(str(game2.state))
    assert(str(game.state) == str(game2.state))

    for _ in range(5):
        game.step(game.actions()[0])

    for _ in range(5):
        game2.step(game2.actions()[0])

    print(str(game.state))
    print(str(game2.state))
    assert(str(game.state == str(game2.state)))

if __name__ == "__main__":
    app.run(main)