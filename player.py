import pickle
import sys
from dataclasses import dataclass
from turtledemo.minimal_hanoi import play

from definitions import DungeonMap, DungeonRoom


def print_exits(player_map, my_player):
    x = my_player.x
    y = my_player.y
    exits = {}
    room = player_map.rows[y][x]
    upward_room = player_map.rows[y - 1][x]
    left_room = player_map.rows[y][x - 1]
    if not room.east_wall:
        print("there is a passage to the east")
        exits["e"] = True
    if not room.south_wall:
        print("there is a passage to the south")
        exits["s"] = True
    if not upward_room.south_wall:
        print("there is a passage to the north")
        exits["n"] = True
    if not left_room.east_wall:
        print("there is a passage to the west")
        exits["w"] = True
    return exits


def ask_for_dir(player_map, x, y):
    while True:
        go = input("Where do you want to go? (N, E, S, W) : ")
        go = go.lower()
        if go == 'n':
            print("NNNNNN")
        elif go == "e":
            print('EEEEEEE')
        elif go == "s":
            print('SSSSS')
        elif go == "w":
            print('WWWWWWW')
        else:
            print("Invalid syntax, please make sure you answer is one of the given options and in lowercase")


@dataclass
class Player:
    x: int
    y: int


def describe_room(player_map, my_player):
    x = my_player.x
    y = my_player.y
    room = player_map.rows[y][x]
    print(x, y)
    if room.entry:
        print("you are at the entrance")
    elif room.exit:
        print("you are at the exit, you won!!!!!!!!!")
    else:
        print("you are in an empty room.")


def ask_for_action():
    action = input("What do you want to do? : ")
    action = action.lower()
    return action


def print_message(message):
    print("*" * len(message))
    print(message)
    print("*" * len(message))
    print()

def validate_action(action, my_map, my_player, exits):
    if action in ['n', 's', 'w', 'e']:
        if exits.get(action, False):
            return True
        else:
            print_message("there is a wall there")
            return False
    else:
        print_message("Invalid syntax")
        return False


def execute_action(action, my_map, my_player):
    if action == "n":
        my_player.y -= 1
    elif action == "e":
        my_player.x += 1
    elif action == "s":
        my_player.y += 1
    elif action == "w":
        my_player.x -= 1



def enter_room(map, player):
    describe_room(map, player)
    exits = print_exits(map, player)
    action = ask_for_action()
    if validate_action(action, map, player, exits):
        execute_action(action, map, player)
    return


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(f'maps\\{filename}.map', 'rb')
    my_map = pickle.load(file)
    my_map.print()
    player = Player(x=1, y=1)
    while True:
        enter_room(my_map, player)
