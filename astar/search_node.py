from state import *

class Search_node:
    def __init__(self, state = None, parent = None):
        self.g = 0 #cost of getting to this node
        self.h = 0 #estimated cost to goal
        self.state = state # coordinates given 2D position (x,y) 
        self.status = True # open = True / closed = False
        self.parent = parent # pointer to best parent node
        self.children = [] # node children
    
    # checking if state is the same
    def __eq__(self, other):
        return self.state == other.state
    
    def __gt__(self, other):
        return (self.g + self.h) > (other.g + other.h)

    # estimated total cost: f(n) = g(n) + h(n)
    def get_f(self):
        return self.g + self.h