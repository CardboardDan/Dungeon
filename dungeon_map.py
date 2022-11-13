import pickle
import sys

from definitions import DungeonMap

if __name__ == '__main__':
    my_map = DungeonMap(width=9, height=12, density=0.9)
    my_map.make_borders()
    my_map.make_exits()
    my_map.make_random_walls()
    my_map.flood_rooms()
    my_map.flood_check()

    my_map.print()
    filename = 'example'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    file = open(f'maps\\{filename}.map', 'wb')
    pickle.dump(my_map, file)