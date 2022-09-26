from map import Map_Obj


class Node:
    def __init__(self, state=None, g=0, h=0, parent=None) -> None:
        self.state = state  # coordinates given 2D position (x,y)
        self.g = g  # cost of getting to this node
        self.h = h  # estimated cost to goal
        self.f = g + h  # sum of g and h
        self.parent = parent  # pointer to best parent node
        self.children = []  # node children

    # checking if state is the same
    def __eq__(self, other) -> bool:
        return self.state == other.state

    # Calculating f based on g and h
    def calculate_f(self) -> int:
        self.f = self.g + self.h

    # Generating all successors for given node
    def generate_all_successors(self, map_obj: Map_Obj) -> list:
        up = [self.state[0] - 1, self.state[1]]
        down = [self.state[0] + 1, self.state[1]]
        left = [self.state[0], self.state[1] - 1]
        right = [self.state[0], self.state[1] + 1]

        matrix = [up, down, left, right]
        successors = []

        for state in matrix:
            value = map_obj.get_cell_value(state)
            if value >= 0:
                node = Node(state)
                successors.append(node)

        return successors
