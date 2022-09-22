class AlphaBeta:
    def __init__(self, game_tree) -> None:
        self.game_tree = game_tree
        self.root = game_tree.root
        return
    

    def alpha_beta_search(self, node):


    def max_value(self, node, alpha, beta):


    def min_value(self, node, alpha, beta):


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
