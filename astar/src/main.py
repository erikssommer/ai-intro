import map
import astar
import sys
from node import Node


def find_path(node, map_obj):
    current_node = node
    goalNode = Node(map_obj.get_goal_pos())

    while current_node.parent is not None:
        if current_node.state != goalNode.state:
            map_obj.set_cell_value(current_node.state, 5)

        current_node = current_node.parent

    map_obj.show_map()


def main(task_number):
    map_obj = map.Map_Obj(task=task_number)
    run = astar.best_first_search(map_obj)

    find_path(run, map_obj)


try:
    input = sys.argv[1]

    try:
        input = int(input)
    except:
        print("You have to pass a variable containing task number, try again!")

    if input <= 0 or input > 5:
        print("Task number must be between 1 and 5")
    else:
        try:
            main(input)
        except:
            print("Could not find path")

except Exception as e:
    print(e)
