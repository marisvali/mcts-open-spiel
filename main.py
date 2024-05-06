# This is required for type annotation to work for this line: def copyFrom(game: Game):
from __future__ import annotations
import random
from absl import app
from absl import flags
import numpy as np

from open_spiel.python import games  # pylint: disable=unused-import
import pyspiel

class Game:
    open_spiel_game = pyspiel.load_game("2048")
    
    def __init__(self) -> None:
        self.state = Game.open_spiel_game.new_initial_state()
        # 2048 starts with two chance nodes, so that 2 numbers '2' are placed in the grid.
        self.__execute_chance_node()
        self.__execute_chance_node()

    def __execute_chance_node(self):
        assert(self.state.is_chance_node())
        outcomes = self.state.chance_outcomes()
        action_list, prob_list = zip(*outcomes)
        action = np.random.choice(action_list, p=prob_list)
        self.state.apply_action(action)

    def actions(self):
        return self.state.legal_actions(0)

    def copyFrom(self, game: Game):
        self.state = Game.open_spiel_game.deserialize_state(game.state.serialize())
        
    def step(self, action) -> tuple[bool, float]:
        # Check if the game is done.
        if self.state.is_terminal():
            return True, self.state.returns()[0]
        
        # We are currently accepting an action from the player.
        assert(not self.state.is_chance_node())
        self.state.apply_action(action)

        # Check if the game is done.
        if self.state.is_terminal():
            return True, self.state.returns()[0]

        # Now we let the chance node do its thing.
        self.__execute_chance_node()

        return self.state.is_terminal(), self.state.rewards()[0]

def main(_):
    np.random.seed(13)

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
        print(f'{total_reward}', end=' ')
        # print(str(state))

if __name__ == "__main__":
    app.run(main)