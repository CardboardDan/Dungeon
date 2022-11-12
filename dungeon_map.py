from dataclasses import dataclass
from typing import List
from random import random


@dataclass
class DungeonRoom:
    south_wall: bool = False
    east_wall: bool = False


@dataclass
class DungeonMap:
    rows: List[List[DungeonRoom]]
    width: int
    height: int
    density: float

    def __init__(self, width, height, density):
        self.width = width + 1
        self.height = height + 1
        self.density = density

        self.rows = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                room = DungeonRoom()
                row.append(room)
            self.rows.append(row)

    def print(self):
        started = False
        r = 0
        for row_index in range(len(self.rows)):
            row = self.rows[row_index]

            W = '#'
            E = ' '
            line1 = f'R{r}'
            line2 = f'R{r}'
            n = 0
            first_room = True
            for room_index in range(len(row)):
                room = row[room_index]

                bottom_right_corner = room.east_wall or \
                                      room.south_wall or \
                                      self.next_room_has_south_wall(row_index, room_index) or \
                                      self.room_below_has_east_wall(row_index, room_index)

                if room.east_wall:
                    line1 = line1 + ('' if first_room else str(n)) + W
                else:
                    line1 = line1 + ('' if first_room else str(n)) + E

                if room.south_wall:
                    line2 = line2 + ('' if first_room else W) + W
                else:
                    line2 = line2 + ('' if first_room else E) + (W if bottom_right_corner else E)
                n += 1
                first_room = False
            if started:
                print(line1)
            else:
                started = True
            print(line2)
            r += 1

    def make_borders(self):
        for room in self.rows[0]:
            room.south_wall = True
        for room in self.rows[-1]:
            room.south_wall = True
        for row in self.rows:
            row[0].east_wall = True
            row[-1].east_wall = True

    def make_exits(self):
        self.rows[-1][-1].south_wall = False
        self.rows[0][1].south_wall = False
        self.rows[1][1].east_wall = True

    def next_room_has_south_wall(self, row_index, room_index):
        if room_index == len(self.rows[0]) - 1:
            return False

        return self.rows[row_index][room_index + 1].south_wall

    def room_below_has_east_wall(self, row_index, room_index):
        if row_index == len(self.rows) - 1:
            return False
        return self.rows[row_index + 1][room_index].east_wall

    def make_random_walls(self):
        for row in self.rows:
            for room in row:
                if random() < self.density:
                    room.south_wall = True
                if random() < self.density:
                    room.east_wall = True


if __name__ == '__main__':
    my_map = DungeonMap(width=9, height=5, density=1.0)
    my_map.make_borders()
    my_map.make_exits()
    my_map.make_random_walls()
    my_map.print()
