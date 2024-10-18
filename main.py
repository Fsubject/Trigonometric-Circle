import pygame
import math

WIDTH, HEIGHT = 900, 900

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def get_points_distance(A, B):
    A_x, B_x = A[0], B[0]
    A_y, B_y = A[1], B[1]
    return math.sqrt(pow((A_x - B_x), 2) + pow((A_y - B_y), 2))


def get_cot(sin, cos):
    return cos / sin


def main():
    pygame.init()
    pygame.font.init()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption("Trigonometric Circle")

    font = pygame.font.SysFont("Arial", 18, bold=True)

    center = (WIDTH / 2, HEIGHT / 2.5)
    radius = 300
    user_points = []
    angle_i = -1

    while running:
        clock.tick(60)
        window.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                point_dist = get_points_distance(mouse_pos, center)
                x = center[0] + radius * ((mouse_pos[0] - center[0]) / point_dist)
                y = center[1] + radius * ((mouse_pos[1] - center[1]) / point_dist)

                angle_radians = math.atan2(center[1] - y, x - center[0])
                angle = round(angle_radians * (180 / math.pi))

                user_points.append([(x, y), angle + 360 if angle < 0 else angle, [math.sin(angle), math.cos(angle), math.tan(angle), get_cot(math.sin(angle), math.cos(angle))]])
                angle_i += 1

        pygame.draw.circle(window, color=BLACK, center=center, width=2, radius=radius)
        pygame.draw.line(window, BLACK, (center[0] - 340, center[1]),
                         (center[0] + 340, center[1]), 2)
        pygame.draw.line(window, BLACK, (center[0], center[1] - 340),
                         (center[0], center[1] + 340), 2)

        for point in user_points:
            pygame.draw.circle(window, BLACK, point[0], 4)
            pygame.draw.line(window, BLACK, center, point[0], 3)

        angle_txt = font.render(f"Actual angle: {user_points[angle_i][1] if angle_i >= 0 else "N/A"}°", False, BLACK)
        window.blit(angle_txt, (30, 30))
        if angle_i >= 0:
            sin = font.render(f"sin {user_points[angle_i][1]}° = {user_points[angle_i][2][0]}", False, BLACK)
            cos = font.render(f"cos {user_points[angle_i][1]}° = {user_points[angle_i][2][1]}", False, BLACK)
            tan = font.render(f"tan {user_points[angle_i][1]}° = {user_points[angle_i][2][2]}", False, BLACK)
            cot = font.render(f"cot {user_points[angle_i][1]}° = {user_points[angle_i][2][3]}", False, BLACK)

            window.blit(sin, (100, HEIGHT - 200))
            window.blit(cos, (100, HEIGHT - 100))
            window.blit(tan, (WIDTH - 350, HEIGHT - 200))
            window.blit(cot, (WIDTH - 350, HEIGHT - 100))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
