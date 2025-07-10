import pygame
import math
from circle import Circle

pygame.init()
pygame.font.init()
pygame.display.set_caption("Trigonometric Circle")

WIDTH, HEIGHT = 900, 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Window:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont("Arial", 18, bold=True)

        self.zero = self.font.render("0", False, BLACK)
        self.one = self.font.render("1", False, BLACK)
        self.minus_one = self.font.render("-1", False, BLACK)

        self.circle = Circle(WIDTH, HEIGHT, 300)
        self.c_angles = self.circle.get_angles()

        self.angle_i = -1
        self.is_placing = False

    def draw_circle(self) -> None:
        pygame.draw.circle(self.window, color=BLACK, center=self.circle.center, width=2, radius=self.circle.radius)
        self.window.blit(self.zero, (self.circle.center[0] + 10, self.circle.center[1] + 10))

        pygame.draw.line(self.window, BLACK, (self.circle.center[0] - 330, self.circle.center[1]), (self.circle.center[0] + 330, self.circle.center[1]), 2)
        self.window.blit(self.one, (self.circle.center[0] + 320, self.circle.center[1] + 10))
        self.window.blit(self.minus_one, (self.circle.center[0] - 330, self.circle.center[1] + 10))

        pygame.draw.line(self.window, BLACK, (self.circle.center[0], self.circle.center[1] - 340), (self.circle.center[0], self.circle.center[1] + 340), 2)
        self.window.blit(self.one, (self.circle.center[0] + 10, self.circle.center[1] - 330))
        self.window.blit(self.minus_one, (self.circle.center[0] + 10, self.circle.center[1] + 320))

    def run(self) -> None:
        while self.running:
            self.clock.tick(60)
            self.window.fill(WHITE)

            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_c:
                        if self.angle_i >= 0:
                            self.is_placing = False
                            self.angle_i = -1
                            self.circle.clear_angles()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.is_placing = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.is_placing:
                        if self.circle.create_angle(mouse_pos):
                            self.angle_i += 1

                        self.is_placing = False

            self.draw_circle()

            for idx, point in enumerate(self.c_angles):
                pygame.draw.circle(self.window, BLACK if idx != self.angle_i else RED, point[0], 4)
                pygame.draw.line(self.window, BLACK if idx != self.angle_i else RED, self.circle.center, point[0], 3)

            if self.is_placing:
                x, y = self.circle.get_xy(mouse_pos)
                pygame.draw.line(self.window, GREEN, self.circle.center, (x, y), 3)
                angle_txt = self.font.render(f"Actual angle: {round(math.degrees(self.circle.get_radian(x, y)))}°", False, BLACK)
            else:
                angle_txt = self.font.render(f"Actual angle: {self.c_angles[self.angle_i][1] if self.angle_i >= 0 else "N/A"}°", False, BLACK)

            self.window.blit(angle_txt, (30, 30))

            if self.angle_i >= 0:
                sin = self.font.render(f"sin {self.c_angles[self.angle_i][1]}° = {self.c_angles[self.angle_i][2][0]}", False, BLACK)
                cos = self.font.render(f"cos {self.c_angles[self.angle_i][1]}° = {self.c_angles[self.angle_i][2][1]}", False, BLACK)
                tan = self.font.render(f"tan {self.c_angles[self.angle_i][1]}° = {self.c_angles[self.angle_i][2][2]}", False, BLACK)
                cot = self.font.render(f"cot {self.c_angles[self.angle_i][1]}° = {self.c_angles[self.angle_i][2][3]}", False, BLACK)

                self.window.blit(sin, (100, HEIGHT - 200))
                self.window.blit(cos, (100, HEIGHT - 100))
                self.window.blit(tan, (WIDTH - 350, HEIGHT - 200))
                self.window.blit(cot, (WIDTH - 350, HEIGHT - 100))

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    window = Window()
    window.run()
