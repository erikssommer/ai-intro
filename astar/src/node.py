from map import Map_Obj


class Node:
    """
    Class to encapsulate search states within nodes in the search tree/graph.
    """
    def __init__(self, state=None, g=0, h=0, parent=None) -> None:
        self.state = state  # coordinates given 2D position (x,y)
        self.g = g  # cost of getting to this node
        self.h = h  # estimated cost to goal
        self.f = g + h  # sum of g and h
        self.parent = parent  # pointer to best parent node
        self.children = []  # node children

    def __eq__(self, other) -> bool:
        """
        checking if state is the same
        """
        return self.state == other.state

    def calculate_f(self) -> int:
        """
        Calculating f based on g and h
        """
        self.f = self.g + self.h

    def generate_all_successors(self, map_obj: Map_Obj) -> list:
        """
        Generating all successors for given node
        """
        up = [self.state[0] - 1, self.state[1]]
        down = [self.state[0] + 1, self.state[1]]
        left = [self.state[0], self.state[1] - 1]
        right = [self.state[0], self.state[1] + 1]

        matrix = [up, down, left, right]
        successors = []

        for state in matrix:
            value = map_obj.get_cell_value(state)
            # Avoiding valls (-1)
            if value >= 0:
                node = Node(state)
                successors.append(node)

        return successors
