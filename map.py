import random

"""
m = map.Map(1, 1, 55, 200) # good params to start
"""


class Map:
    def __init__(self, player_height, player_width, screen_height, screen_width):
        self._player_height = player_height
        self._player_width = player_width
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._map = []
        self._bitmap = []

    def generate(self):
        previous_top = 0
        previous_bottom = self._screen_height

        new_map = []

        for row in range(self._screen_width):
            cave_top, cave_bot = self._generate_row(previous_top, previous_bottom)
            new_map.append([cave_top, cave_bot])
            previous_top = cave_top
            previous_bottom = cave_bot

        self._map = new_map
        self.save_to_file()
        return self._bitmap

    def _generate_row(self, prev_top, prev_bottom):
        """" return left/right map row """
        seed = random.randint(prev_top + Cave.MIN_PASS_SIZE, prev_bottom - Cave.MIN_PASS_SIZE)
        cave_height = random.randint(Cave.MIN_HEIGHT, Cave.MAX_HEIGHT)
        cave_top = (seed - cave_height//2) if (seed - cave_height//2) > 0 else 0
        cave_bottom = (seed + cave_height//2) if (seed + cave_height//2) < self._screen_height else self._screen_height
        return cave_top, cave_bottom

    def save_to_file(self, file_name="map.txt"):
        with open("map.txt", 'w+') as f:
            for column in self._map:
                bitmap = [c in range(column[0], column[1]) for c in range(self._screen_height)]
                self._bitmap.append(bitmap)

            for i in range(self._screen_height):
                for column in self._bitmap:
                    if column[i]:
                        f.write(' ')
                    else:
                        f.write('0')
                f.write('\n')


class Cell:
    def __init__(self):
        self.empty = False


class Cave:
    MIN_PASS_SIZE = 5
    MIN_HEIGHT = 17
    MAX_HEIGHT = 20
    MIN_WIDTH = 100
    MAX_WIDTH = 500
