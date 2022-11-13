import pickle
import sys
from definitions import DungeonMap, DungeonRoom


def print_exits(map, x, y):
    room = map.rows[y][x]
    upward_room = map.rows[y - 1][x]
    left_room = map.rows[y][x - 1]
    if room.entry:
        print("you are at the entrance")
    if room.exit:
        print("you are at the exit, you won!!!!!!!!!")
    if not room.east_wall:
        print("there  is a passage to the east")
    if not room.south_wall:
        print("there is a passage to the south")
    if not upward_room.south_wall:
        print("there is a passage to the north")
    if not left_room.east_wall:
        print("there is a passage to the west")


def ask_for_dir():
    while True:
        go = input("Where do you want to go? (N, E, S, W) : ")
        if go == 'n':
            print("NNNNNN")
        elif go == "e":
            print('EEEEEEE')
        elif go == "s":
            print('SSSSS')
        elif go == "w":
            print('WWWWWWW')
        else
            print("Invalid syntax, please make sure you answer is one of the given options and in lowercase")


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(f'maps\\{filename}.map', 'rb')
    my_map = pickle.load(file)
    my_map.print()
    print_exits(map=my_map, x=1, y=1)
