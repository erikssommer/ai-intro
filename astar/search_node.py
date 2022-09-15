from state import *

class Search_node:
    def __init__(self, state, parent, path_cost, est_total_cost) -> None:
        self.parent = parent # parent node
        self.path_cost = path_cost # cost from the starting node to this node
        self.est_total_cost = est_total_cost # estimated total costs: f(n)=g(n)+h(n)
        self.state = state # coordinates of the given position (x, y)
    
    def __eq__(self, other):
        return self.est_total_cost == other.est_total_cost
    
    def __gt__(self, other):
        return self.est_total_cost > other.est_total_cost

    def __lt__(self, other):
        return self.est_total_cost < other.est_total_cost