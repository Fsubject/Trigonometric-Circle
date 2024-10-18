import math
import pygame


def get_points_distance(A, B) -> float:
    A_x, B_x = A[0], B[0]
    A_y, B_y = A[1], B[1]
    return math.sqrt(pow((A_x - B_x), 2) + pow((A_y - B_y), 2))


def get_cot(sin, cos) -> float:
    return cos / sin


class Circle:
    def __init__(self, width, height, radius):
        self.center = (width / 2, height / 2.5)
        self.radius = radius
        self.angles = []

    def create_angle(self, mouse_pos) -> None:
        point_dist = get_points_distance(mouse_pos, self.center)
        x = self.center[0] + self.radius * ((mouse_pos[0] - self.center[0]) / point_dist)
        y = self.center[1] + self.radius * ((mouse_pos[1] - self.center[1]) / point_dist)

        angle_radians = math.atan2(self.center[1] - y, x - self.center[0])
        angle = round(angle_radians * (180 / math.pi))

        self.angles.append([(x, y), angle + 360 if angle < 0 else angle, [math.sin(angle), math.cos(angle), math.tan(angle), get_cot(math.sin(angle), math.cos(angle))]])

    def get_center(self) -> tuple:
        return self.center

    def get_radius(self) -> int:
        return self.radius

    def get_angles(self) -> list:
        return self.angles
