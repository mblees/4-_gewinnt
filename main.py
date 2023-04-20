import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


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
    vertices = (
        (2, 2, 0),
        (-2, -2, 0),
        (-2, 2, 0),
        (2, -2, 0)
    )

    edges = (
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3)
    )

    def __init__(self):
        pass

    def rectangle(self):
        glColor3f(0.5, 0.5, 1.0)
        glBegin(GL_QUADS)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

    def sphere(self, radius, subdivisions, center):
        glColor3f(1, 1, 1)
        vertex_array = []
        normal_array = []
        for i in range(subdivisions):
            phi = math.pi * (i + 0.5) / subdivisions
            for j in range(subdivisions):
                theta = 2 * math.pi * j / subdivisions
                x = radius * math.sin(phi) * math.cos(theta) + center[0]
                y = radius * math.sin(phi) * math.sin(theta) + center[1]
                z = radius * math.cos(phi) + center[2]
                vertex_array.append([x, y, z])
                normal_array.append([x - center[0], y - center[1], z - center[2]])

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glBegin(GL_TRIANGLES)
        for i in range(subdivisions):
            for j in range(subdivisions):
                v1 = i * subdivisions + j
                v2 = v1 + 1
                v3 = (i + 1) * subdivisions + j
                if v1 < len(vertex_array) and v2 < len(vertex_array) and v3 < len(vertex_array):
                    glNormal3fv(normal_array[v1])
                    glVertex3fv(vertex_array[v1])
                    glNormal3fv(normal_array[v2])
                    glVertex3fv(vertex_array[v2])
                    glNormal3fv(normal_array[v3])
                    glVertex3fv(vertex_array[v3])

                    v1 = (i + 1) * subdivisions + j
                    v2 = v1 + 1
                    v3 = i * subdivisions + j + 1
                    if v1 < len(vertex_array) and v2 < len(vertex_array) and v3 < len(vertex_array):
                        glNormal3fv(normal_array[v1])
                        glVertex3fv(vertex_array[v1])
                        glNormal3fv(normal_array[v2])
                        glVertex3fv(vertex_array[v2])
                        glNormal3fv(normal_array[v3])
                        glVertex3fv(vertex_array[v3])
        glEnd()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    def init_window(self):
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)
        gluLookAt(5, 5, 5, 0, 0, 0, 0, 0, 1)

    def start_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.rectangle()
            self.sphere(0.4, 15, [1.5, 1.5, 0.5])
            self.sphere(0.4, 15, [0.5, 1.5, 0.5])
            self.sphere(0.4, 15, [-0.5, 1.5, 0.5])
            self.sphere(0.4, 15, [-1.5, 1.5, 0.5])
            pygame.display.flip()
            pygame.time.wait(10)


myGui = GUI()
myGui.init_window()
myGui.start_game_loop()
