# This is required for type annotation to work for this line: def copyFrom(game: Game):
from __future__ import annotations
from game import Game
import numpy as np
from absl import app
import pyspiel

def main(_):
    np.random.seed(19)
    rewards = []

    for _ in range(0, 100):
        game = Game()
        total_reward = 0
        while True:
            actions = game.actions()
            action = np.random.choice(actions)
            done, reward = game.step(action)
            total_reward += reward
            if done:
                break

        # Game is now done. Print utilities for player 1.
        # print(f'{total_reward}', end=' ')
        print(game.won(), end=' ')
        rewards.append(total_reward)
        # print(str(state))

    print(max(rewards))
if __name__ == "__main__":
    app.run(main)