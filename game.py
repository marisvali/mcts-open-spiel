# This is required for type annotation to work for this line: def copyFrom(game: Game):
from __future__ import annotations
import numpy as np
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
    
    def won(self):
        if not self.state.is_terminal():
            return False
        
        return '2048' in str(self.state)
        
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