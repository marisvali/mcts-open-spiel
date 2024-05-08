# This is required for type annotation to work for this line: def copyFrom(game: Game):
from __future__ import annotations
from game import Game
import numpy as np
from absl import app
import pyspiel
from policy import Policy_Player_MCTS
from node import Node
from visualize import *

def write_to_csv(vals, create: bool):
    if create:
        f = open("vals.csv", "w")
    else: 
        f = open("vals.csv", "a")
    line = ''
    for i in range(len(vals) - 1):
        line += str(vals[i]) + ','
    line += str(vals[-1]) + '\n'
    f.write(line)

def main(_):
    np.random.seed(19)
    rewards = []
    
    game = Game()
    total_reward = 0
    mytree = Node(game, False, 0, 0)
    original = mytree
    # PrintNode(original)
    step_idx = 0
    print(TreeSize(original), TreeSize(mytree))
    write_to_csv([step_idx, TreeSize(original), TreeSize(mytree)], True)
    while True:
        step_idx += 1
        # actions = game.actions()
        # action = np.random.choice(actions)
        mytree, action = Policy_Player_MCTS(mytree)
        # PrintNode(original)
        total_tree_size = TreeSize(original)
        current_tree_size = TreeSize(mytree)
        print(total_tree_size, current_tree_size)
        write_to_csv([step_idx, total_tree_size, current_tree_size], False)
        done, reward = game.step(action)
        total_reward += reward
        # print('#', end='')
        print(step_idx)
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