from dataclasses import dataclass
from typing import List
from random import random


@dataclass
class DungeonRoom:
    south_wall: bool = False
    east_wall: bool = False
    entry: bool = False
    exit: bool = False
    flooded: bool = False


@dataclass
class DungeonMap:
    rows: List[List[DungeonRoom]]
    width: int
    height: int
    density: float
    entry: DungeonRoom

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
            F = '='
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
                    line1 = line1 + ('' if first_room else (F if room.flooded else E)) + W
                else:
                    line1 = line1 + ('' if first_room else (F if room.flooded else E)) + E

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
        self.rows[-1][-1].exit = True
        self.rows[1][1].entry = True
        self.entry = self.rows[1][1]
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

    def flood_rooms(self):
        for g in range(self.width * self.height):
            self.entry.flooded = True
            for i in range(1, self.height):
                row = self.rows[i]
                for j in range(1, self.width):
                    room = row[j]
                    if room.flooded:
                        if not room.east_wall:
                            row[j+1].flooded = True
                        if not room.south_wall:
                            self.rows[i + 1][j].flooded = True
                        if not row[j-1].east_wall:
                            row[j-1].flooded = True
                        if not self.rows[i-1][j].south_wall:
                            self.rows[i-1][j].flooded = True


if __name__ == '__main__':
    my_map = DungeonMap(width=9, height=5, density=0.5)
    my_map.make_borders()
    my_map.make_exits()
    my_map.make_random_walls()
    my_map.flood_rooms()

    my_map.print()

