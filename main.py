class Point:
    def __init__(self):
        self.color = None

    def get_color(self):
        return self.color

    def set_color(self, c):
        if self.color is None:
            self.color = c
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.grid = [[[Point() for _ in range(4)] for _ in range(4)] for _ in range(4)]

    def get_point(self, x, y, z):
        return self.grid[x][y][z]

    def set_point_color(self, x, y, z, color):
        return self.grid[x][y][z].set_color(color)

    def print_board(self):
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    print(f"({x},{y},{z}): {self.grid[x][y][z].get_color()} ", end="")
                print()
            print()


board = Board()
board.set_point_color(0, 0, 0, 'red')
board.set_point_color(1, 0, 0, 'red')
board.set_point_color(2, 0, 0, 'red')
board.set_point_color(3, 0, 0, 'red')
board.print_board()
