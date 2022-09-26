import map
import astar
import sys
from node import Node
from map import Map_Obj
from solution import Solution


def find_path(node: Node, map_obj: Map_Obj) -> Node:
    """
    Drawing map by backpropagating from resultnode
    """
    current_node = node
    goal_node = Node(map_obj.get_goal_pos())

    # Backpropagation - tracing back to initial node and marking each visited cell
    while current_node.parent is not None:
        if current_node.state != goal_node.state:
            cell_value = map_obj.get_cell_value(current_node.state)
            map_obj.set_cell_value(current_node.state, cell_value)

        current_node = current_node.parent
    # Showing map
    map_obj.show_map()


def main(task_number: int) -> None:
    """
    Method for running a star algorithm for given task
    """
    map_obj = map.Map_Obj(task=task_number)
    status, node = astar.best_first_search(map_obj, task_number)

    if status == Solution.SUCCESS:
        find_path(node, map_obj)
    else:
        print("Failed to find path")


try:
    # Retrieving task number from shell variable
    input = sys.argv[1]

    try:
        input = int(input)
    except:
        print("You have to pass a variable containing task number, try again!")

    # Task number has to be between 1 and 5
    if input <= 0 or input > 5:
        print("Task number must be between 1 and 5")
    else:
        try:
            # Input is valid and astar algorithm is initiated
            main(input)
        except:
            print("Could not find path")

except Exception as e:
    print(e)
