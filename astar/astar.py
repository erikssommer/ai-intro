from search_node import Search_node

def best_first_search(map_obj):
    open = []
    closed = []

    root_node = Search_node(map_obj.get_start_pos())
    goal_node = Search_node(map_obj.get_goal_pos())

    root_node.g = 0
    root_node.h = manhattan_distance(root_node, goal_node)
    root_node.calculate_f()

    open.append(root_node)

    # Agenda loop
    while open:

        if len(open) == 0:
            print("Failed")
            return None

        current_node = open.pop()
        closed.append(current_node)

        if current_node.__eq__(goal_node):
            return current_node

        path = current_node.generate_all_successors(map_obj)

        for node in path:
            node_state = node_open_closed_check(node, open, closed)

            if node_state not in open and node_state not in closed:
                attach_and_eval(node_state, current_node, map_obj)
                open.append(node_state)
                open.sort(key=lambda node: node.f, reverse=True)
            elif (current_node.g + arc_cost(node_state, map_obj)) < node_state.g:
                attach_and_eval(node_state, current_node, map_obj)
                if node_state in closed:
                    propagate_path_improvements(node_state, map_obj)


def node_open_closed_check(node, open, closed):
    for i in open:
        if i.state == node.state:
            return i

    for i in closed:
        if i.state == node.state:
            return i

    return node


def attach_and_eval(child, parent, map_obj):
    child.parent = parent
    child.g = parent.g + arc_cost(child, map_obj)
    child.h = manhattan_distance(child, Search_node(map_obj.get_end_goal_pos()))
    child.f = child.g + child.h


# Returns the Manhattan distance between the two nodes
def manhattan_distance(curr_node, goal_node):
    return abs(curr_node.state[0] - goal_node.state[0]) + abs(curr_node.state[1] - goal_node.state[1])


def arc_cost(child, map_obj):
    return map_obj.get_cell_value(child.state)


def propagate_path_improvements(parent, map_obj):
    for child in parent.children:
        if parent.g + arc_cost(child, map_obj) < child.g:
            child.parent = parent
            child.g = parent.g + arc_cost(child, map_obj)
            child.f = child.g + child.h
            propagate_path_improvements(child, map_obj)
