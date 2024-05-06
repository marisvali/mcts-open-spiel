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
    rewards = []
    
    game = Game()
    total_reward = 0
    mytree = Node(game, False, 0, 0)
    step_idx = 0
    while True:
        # actions = game.actions()
        # action = np.random.choice(actions)
        mytree, action = Policy_Player_MCTS(mytree)
        done, reward = game.step(action)
        total_reward += reward
        step_idx += 1
        # print('#', end='')
        print(game.state)
        if done:
            break

    # Game is now done. Print utilities for player 1.
    # print(f'{total_reward}', end=' ')
    if game.won():
        print("WINNER!")
    rewards.append(total_reward)
    # print(str(state))

    print(max(rewards))
if __name__ == "__main__":
    app.run(main)