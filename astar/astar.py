from logging import root
import Map
from search_node import Search_node

def best_first_search(map_obj, heuristic_fun):
    open = []
    closed = []

    root_node = Search_node(map_obj.get_start_pos())
    goal_node = Search_node(map_obj.get_goal_state())

    root_node.g = 0
    root_node.h = heuristic_fun(map_obj, root_node.state)
    open.append(root_node.get_f())

    while open:
        if len(open) == 0:
            print("Failed")
            return "fail"

        current_node = open.pop()
        closed.append(current_node)

        if current_node == goal_node:
            return current_node, 'succeed'
        
        path = generate_all_successors(current_node)

        for node in path:
            node_state = node_open_closed_check(node, open, closed)

            if node_state not in open and node_state not in closed:
                attach_and_eval(node_state, current_node, map_obj)
                open.append(node_state)
                open.sort(key=lambda node: node.f, reverse=True)
            elif (current_node.g + map_obj.get_cell_value(node_state.position)) > node_state.g:
                attach_and_eval(node_state, current_node, map_obj)
                if node_state in closed:
                    propagate_path_improvements(node_state, map_obj)


def generate_all_successors(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.state)
        current_node = current_node.parent
    
    return path


def node_open_closed_check(node, open, closed):
    for i in open:
        if i.position == node.position:
            return i
    
    for i in closed:
        if i.position == node.position:
            return i
    
    return node


def attach_and_eval(child, parent, map_obj):
    child.parent = parent
    child.g = parent.g + map_obj.get_cell_value(child.position)
    child.h = manhattan_distance(child.position, map_obj.get_end_goal_pos())


# Returns the Manhattan distance between the two nodes
def manhattan_distance(curr_node, goal_node):
    return abs(curr_node[0]-goal_node[0]) + abs(curr_node[1]-goal_node[1])


def arc_cost(child, map_obj):
    return map_obj.get_cell_value(child.position)


def propagate_path_improvements(parent, map_obj):
    for child in parent.children:
        if parent.g + arc_cost(child, map_obj) < child.g:
            child.parent = parent
            child.g = parent.g + arc_cost(child.position)
            child.f = child.g + child.h
            propagate_path_improvements(child, map_obj)
            
