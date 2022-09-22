import Map
import astar
import sys

def find_path(node, map_obj):
    current_node = node

    while current_node.parent is not None:
        if current_node != map_obj.get_goal_pos():
            map_obj.set_cell_value(current_node.position, 5)

        current_node = current_node.parent
    
    map_obj.show_map()


def main(task_number):
    map_obj = Map.Map_Obj(task=task_number)
    run = astar.best_first_search(map_obj)

    try:
        find_path(run, map_obj)
    except AttributeError:
        print("An error accoured while finding path")

try:
    input = sys.argv[1]

    try:
        input = int(input)
    except:
        print("You have to pass a variable containing task number, try again!")

    if input <= 0 or input > 3:
        print("Task number must be between 1 and 3")
    else:
        main(input)
except Exception as e:
    print(e)