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
                    color = self.grid[x][y][z].get_color()
                    if color is not None:
                        print(f"{color}|", end="")
                    else:
                        print("_|", end="")
                print(" ", end="")
            print()

    def check_color_win(self, color):
        # Check rows
        for x in range(4):
            for y in range(4):
                for z in range(1):  # Only need to check first layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x][y][z + 1].get_color() == color and
                            self.grid[x][y][z + 2].get_color() == color and
                            self.grid[x][y][z + 3].get_color() == color):
                        return True

        # Check columns
        for x in range(4):
            for y in range(1):  # Only need to check first layer of height
                for z in range(4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x][y + 1][z].get_color() == color and
                            self.grid[x][y + 2][z].get_color() == color and
                            self.grid[x][y + 3][z].get_color() == color):
                        return True

        # Check depth
        for x in range(1):  # Only need to check first layer of width
            for y in range(4):
                for z in range(4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x + 1][y][z].get_color() == color and
                            self.grid[x + 2][y][z].get_color() == color and
                            self.grid[x + 3][y][z].get_color() == color):
                        return True

        # Check diagonals
        for x in range(1):  # Only need to check first layer of width
            for y in range(1):  # Only need to check first layer of height
                for z in range(4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x + 1][y + 1][z].get_color() == color and
                            self.grid[x + 2][y + 2][z].get_color() == color and
                            self.grid[x + 3][y + 3][z].get_color() == color):
                        return True

        for x in range(1):  # Only need to check first layer of width
            for y in range(3, 4):
                for z in range(4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x + 1][y - 1][z].get_color() == color and
                            self.grid[x + 2][y - 2][z].get_color() == color and
                            self.grid[x + 3][y - 3][z].get_color() == color):
                        return True

        for x in range(4):
            for y in range(1):  # Only need to check first layer of height
                for z in range(1):  # Only need to check first layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x - 1][y + 1][z + 1].get_color() == color and
                            self.grid[x - 2][y + 2][z + 2].get_color() == color and
                            self.grid[x - 3][y + 3][z + 3].get_color() == color):
                        return True

        for x in range(4):
            for y in range(1):  # Only need to check first layer of height
                for z in range(3, 4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x - 1][y + 1][z - 1].get_color() == color and
                            self.grid[x - 2][y + 2][z - 2].get_color() == color and
                            self.grid[x - 3][y + 3][z - 3].get_color() == color):
                        return True

        for x in range(4):
            for y in range(4):
                for z in range(1):  # Only need to check first layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x - 1][y][z + 1].get_color() == color and
                            self.grid[x - 2][y][z + 2].get_color() == color and
                            self.grid[x - 3][y][z + 3].get_color() == color):
                        return True

        for x in range(1):  # Only need to check first layer of width
            for y in range(1):  # Only need to check first layer of height
                for z in range(1):  # Only need to check first layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x + 1][y + 1][z].get_color() == color and
                            self.grid[x + 2][y + 2][z].get_color() == color and
                            self.grid[x + 3][y + 3][z].get_color() == color):
                        return True

        for x in range(3, 4):  # Only need to check last layer of width
            for y in range(1):  # Only need to check first layer of height
                for z in range(1):  # Only need to check first layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x - 1][y + 1][z].get_color() == color and
                            self.grid[x - 2][y + 2][z].get_color() == color and
                            self.grid[x - 3][y + 3][z].get_color() == color):
                        return True

        for x in range(1):  # Only need to check first layer of width
            for y in range(1):  # Only need to check first layer of height
                for z in range(4):
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x + 1][y + 1][z + 1].get_color() == color and
                            self.grid[x + 2][y + 2][z + 2].get_color() == color and
                            self.grid[x + 3][y + 3][z + 3].get_color() == color):
                        return True

        for x in range(3, 4):  # Only need to check last layer of width
            for y in range(1):  # Only need to check first layer of height
                for z in range(3, 4):  # Only need to check last layer of depth
                    if (self.grid[x][y][z].get_color() == color and
                            self.grid[x - 1][y + 1][z - 1].get_color() == color and
                            self.grid[x - 2][y + 2][z - 2].get_color() == color and
                            self.grid[x - 3][y + 3][z - 3].get_color() == color):
                        return True
        return False


board = Board()
board.set_point_color(0, 0, 0, 'x')
board.set_point_color(1, 1, 1, 'x')
board.set_point_color(2, 2, 2, 'x')
board.set_point_color(3, 3, 3, 'x')
board.print_board()
if board.check_color_win('x'):
    print('x has won')
