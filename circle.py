import math


def get_points_distance(A, B) -> float:
    A_x, B_x = A[0], B[0]
    A_y, B_y = A[1], B[1]
    return math.sqrt(pow((A_x - B_x), 2) + pow((A_y - B_y), 2))


def get_cot(sin, cos) -> float:
    return cos / sin


class Circle:
    def __init__(self, width, height, radius) -> None:
        self.center = (width / 2, height / 2.5)
        self.radius = radius
        self.angles = []

    def create_angle(self, mouse_pos) -> bool:
        x, y = self.get_xy(mouse_pos)
        angle_radian = self.get_radian(x, y)
        angle_degree = round(math.degrees(angle_radian))

        for angle in self.angles:
            if angle[1] == angle_degree:
                return False

        self.angles.append([(x, y), angle_degree,
                            [math.sin(angle_radian), math.cos(angle_radian), math.tan(angle_radian), get_cot(math.sin(angle_radian), math.cos(angle_radian))]])
        print(self.angles)

        return True

    def get_xy(self, mouse_pos) -> tuple:
        point_dist = get_points_distance(mouse_pos, self.center)
        x = self.center[0] + self.radius * ((mouse_pos[0] - self.center[0]) / point_dist)
        y = self.center[1] + self.radius * ((mouse_pos[1] - self.center[1]) / point_dist)

        return x, y

    def get_radian(self, x, y):
        return math.atan2(self.center[1] - y, x - self.center[0])

    def get_angles(self) -> list:
        return self.angles

    def clear_angles(self) -> None:
        self.angles.clear()
