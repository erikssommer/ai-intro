from logging import root
import Map
from search_node import Search_node

def generate_all_successors(current_node):
    path = []
    while current_node is not None:
        path.append(current_node.state)
        current_node = current_node.parent
    
    return path

def best_first_search(map_obj, heuristic_fun, cost_fun, tick):
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
            return generate_all_successors(current_node)



