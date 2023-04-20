from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtOpenGL import QGLWidget
from OpenGL.GL import *


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


class GUI:
    def __init__(self, board):
        self.board = board


class OpenGLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(OpenGLWidget, self).__init__(parent)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, 0.0)
        glEnd()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        self.setLayout(grid)

        opengl = OpenGLWidget()
        grid.addWidget(opengl, 0, 0, 1, 2)

        label = QLabel('3D GUI')
        grid.addWidget(label, 1, 0)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('3D GUI')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()

myBoard = Board()
myBoard.set_point_color(0, 0, 0, 'red')
myBoard.set_point_color(0, 0, 1, 'red')
myBoard.set_point_color(0, 0, 2, 'red')
myBoard.set_point_color(0, 0, 3, 'red')
