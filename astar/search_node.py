class Search_node:
    def __init__(self, state=None, parent=None):
        self.g = 0  # cost of getting to this node
        self.h = 0  # estimated cost to goal
        self.f = 0
        self.state = state  # coordinates given 2D position (x,y)
        self.status = True  # open = True / closed = False
        self.parent = parent  # pointer to best parent node
        self.children = []  # node children

    # checking if state is the same
    def __eq__(self, other):
        return self.state == other.state

    def __gt__(self, other):
        return (self.g + self.h) > (other.g + other.h)

    # estimated total cost: f(n) = g(n) + h(n)
    def get_f(self):
        return self.g + self.h

    def calculate_f(self):
        self.f = self.g + self.h

    def generate_all_successors(self, map_obj):
        up = [self.state[0] - 1, self.state[1]]
        down = [self.state[0] + 1, self.state[1]]
        left = [self.state[0], self.state[1] - 1]
        right = [self.state[0], self.state[1] + 1]

        matrix = [up, down, left, right]
        successors = []

        for state in matrix:
            value = map_obj.get_cell_value(state)
            if value >= 0:
                node = Search_node(state)
                successors.append(node)

        return successors
