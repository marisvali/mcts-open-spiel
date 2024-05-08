from copy import deepcopy
from math import *
import random
from game import Game
import time

c = 1.0
idx = 0
total1 = 0
total2 = 0

class NaiveNode:
    def __init__(self, game: Game, done, parent, action_index, score):
          
        # child nodes
        self.children = None
        
        # the environment
        self.game = game

        # description
        self.desc = str(self.game.state)
        
        # if game is won/loss/draw
        self.done = done

        # link to parent node
        self.parent = parent
        
        # action index that leads to this node
        self.action_index = action_index

        self.score = score
    
    def label(self):
        return f'{self.score:.0f}\n{self.desc}'
        
    def getScore(self):
        return self.score
    
    def detach_parent(self):
        # free memory detaching nodes
        del self.parent
        self.parent = None
        
    def create_child(self):
        if self.done:
            return
    
        self.children = {} 
        actions = self.game.actions()
        for action in actions: 
            new_game = Game()
            new_game.copyFrom(self.game)
            done, reward = new_game.step(action)
            self.children[action] = NaiveNode(new_game, done, self, action, self.score + reward)
            
    def explore(self):
        global idx
        global total1
        global total2
        idx += 1
            
        start_time = time.time()
        # find a leaf node by choosing random nodes
        current = self
        while current.children:
            children = list(current.children.values())
            current = random.choice(children)
        duration = time.time() - start_time
        total1 += duration

        if idx % 1000 == 0:
            print("--- %s seconds ---" % (total1))
            total1 = 0

        start_time = time.time()
        # expand
        current.create_child()
        duration = time.time() - start_time
        total2 += duration
        if idx % 1000 == 0:
            print("--- %s seconds ---" % (total2))
            total2 = 0
    
    def next(self):
        # find the leaf with max reward
        nodes = [self]
        leafs = []
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.children:
                for child in node.children.values():
                    nodes.append(child)
            else:
                leafs.append(node)
        
        max_leaf = leafs[0]
        for leaf in leafs:
            if leaf.score > max_leaf.score:
                max_leaf = leaf
        
        # now go to parents until we are the child of the current node
        max_child = max_leaf
        while max_child.parent != self:
            max_child = max_child.parent
        
        return max_child, max_child.action_index