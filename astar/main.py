import Map
import astar
import sys

from search_node import Search_node


def find_path(node, map_obj):
    current_node = node
    goalNode = Search_node(map_obj.get_goal_pos())

    while current_node.parent is not None:
        if current_node.state != goalNode.state:
            map_obj.set_cell_value(current_node.state, 5)

        current_node = current_node.parent

    map_obj.show_map()


def main(task_number):
    map_obj = Map.Map_Obj(task=task_number)
    run = astar.best_first_search(map_obj)

    find_path(run, map_obj)


try:
    input = sys.argv[1]

    try:
        input = int(input)
    except:
        print("You have to pass a variable containing task number, try again!")

    if input <= 0 or input > 4:
        print("Task number must be between 1 and 4")
    else:
        try:
            main(input)
        except:
            print("Could not find path")

except Exception as e:
    print(e)
