class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

class AlphaBeta:
    def __init__(self, game_tree) -> None:
        self.game_tree = game_tree
        self.root = game_tree.root
        return
    

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print("AlphaBeta: Utility Value of Root Node: = " + str(best_val))
        print("AlphaBeta: Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        print("AlphaBeta --> Max: Visited node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        
        infinity = float('inf')
        value = -infinity

        succressors = self.getSuccessors(node)

        for state in succressors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value


    def min_value(self, node, alpha, beta):
        print("AlphaBeta --> Min: Visited node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        
        infinity = float('inf')
        value = -infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)
        
        return value

    # Utility methods

    # Successor states in a game tree are the child nodes
    def getSuccessors(self, node):
        assert node is not None
        return node.children
    
    # return true if the node has NO children
    # return false if the node has children
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0
    
    # returns the value of the node
    def getUtility(self, node):
        assert node is not None
        return node.value

def main():
    game_tree = None
    search = AlphaBeta(game_tree)
