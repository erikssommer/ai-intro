from state import *

class Search_node:
    def __init__(self, state: State, status, parent, kids) -> None:
        self.state = state
        self.g = 0
        self.h = 0
        self.status = status
        self.parent = parent
        self.kids = kids
        
    
    def get_f(self):
        return self.g + self.h
    