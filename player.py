import pickle
import sys
from definitions import DungeonMap, DungeonRoom

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(f'maps\\{filename}.map', 'rb')
    my_map = pickle.load(file)
    my_map.print()