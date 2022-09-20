import Map
import astar

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

main(1)