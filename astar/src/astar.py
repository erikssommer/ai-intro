from map import Map_Obj
from node import Node

# All algorithms are implemented based on the pseudocode given in "Essentials of the A* Algorithm" - handout
def best_first_search(map_obj: Map_Obj):
    open: list[Node] = []
    closed: list[Node] = []

    start_node = Node(map_obj.get_start_pos())
    goal_node = Node(map_obj.get_goal_pos())

    start_node.g = 0
    start_node.h = manhattan_distance(start_node, goal_node)
    start_node.calculate_f()

    open.append(start_node)

    # Agenda loop
    while open:
        if len(open) == 0:
            return None

        current_node: Node = open.pop()

        closed.append(current_node)

        if current_node == goal_node:
            return current_node  # Solution

        successors = current_node.generate_all_successors(map_obj)

        for successor in successors:
            node = uniqueness_check(successor, open, closed)
            current_node.children.append(successor)
            if node not in open and node not in closed:
                attach_and_eval(node, current_node, goal_node, map_obj)
                open.append(node)
                open.sort(key=lambda node: node.f, reverse=True)
            elif (current_node.g + arc_cost(node, map_obj)) < node.g:
                attach_and_eval(node, current_node, goal_node, map_obj)
                if node in closed:
                    propagate_path_improvements(node, map_obj)


# Returns node if previously created, and successor if not
def uniqueness_check(successor: Node, open: list[Node], closed: list[Node]) -> Node:
    for node in open:
        if node == successor:
            return node

    for node in closed:
        if node == successor:
            return node

    return successor

# Attaches a child node to a node that is considered its best parent so far
def attach_and_eval(child: Node, parent: Node, goal_node: Node, map_obj: Map_Obj) -> None:
    child.parent = parent
    child.g = parent.g + arc_cost(child, map_obj)
    child.h = manhattan_distance(child, goal_node)
    child.f = child.g + child.h


# Heuristic function
# Returns the Manhattan distance between the two nodes
def manhattan_distance(curr_node: Node, goal_node: Node):
    return abs(curr_node.state[0] - goal_node.state[0]) + abs(curr_node.state[1] - goal_node.state[1])

# Calculates the cost of taking the step
def arc_cost(child: Node, map_obj: Map_Obj) -> int:
    return map_obj.get_cell_value(child.state)


def propagate_path_improvements(parent: Node, map_obj: Map_Obj) -> None:
    child: Node
    for child in parent.children:
        if parent.g + arc_cost(child, map_obj) < child.g:
            child.parent = parent
            child.g = parent.g + arc_cost(child, map_obj)
            child.f = child.g + child.h
            propagate_path_improvements(child, map_obj)
