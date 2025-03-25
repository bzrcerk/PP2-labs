import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

colors = [colorRED, colorBLUE, colorGREEN, colorBLACK]
current_color = colorRED

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = currY = 0
prevX = prevY = 0

tool = "RECT"


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos  # Set the starting point for the shape
            print(f"MOUSEBUTTONDOWN at {prevX}, {prevY}, Tool: {tool}")

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos  # Set the ending point for the shape
            print(f"MOUSEBUTTONUP at {currX}, {currY}, Tool: {tool}")
            if tool == "RECT":
                pygame.draw.rect(
                    screen,
                    current_color,
                    calculate_rect(prevX, prevY, currX, currY),
                    THICKNESS,
                )
            elif tool == "CIRCLE":
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                pygame.draw.circle(
                    screen, current_color, (prevX, prevY), radius, THICKNESS
                )
            elif tool == "ERASER":
                pygame.draw.line(
                    screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS
                )

        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos
            if LMBpressed:
                if tool == "RECT":
                    pygame.draw.rect(
                        screen,
                        current_color,
                        calculate_rect(prevX, prevY, currX, currY),
                        THICKNESS,
                    )
                elif tool == "CIRCLE":
                    radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                    pygame.draw.circle(
                        screen, current_color, (prevX, prevY), radius, THICKNESS
                    )
                    prevX, prevY = currX, currY
                elif tool == "ERASER":
                    pygame.draw.line(
                        screen,
                        colorWHITE,
                        (prevX, prevY),
                        (currX, currY),
                        THICKNESS,
                    )
                    prevX, prevY = currX, currY
                elif tool == "FREEHAND":
                    pygame.draw.line(
                        screen,
                        current_color,
                        (prevX, prevY),
                        (currX, currY),
                        THICKNESS,
                    )
                    prevX, prevY = currX, currY

        if event.type == pygame.KEYDOWN:
            print(f"Key pressed: {event.key}")
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)
            elif event.key == pygame.K_r:
                tool = "RECT"
            elif event.key == pygame.K_c:
                tool = "CIRCLE"
            elif event.key == pygame.K_e:
                tool = "ERASER"
            elif event.key == pygame.K_f:
                tool = "FREEHAND"
            elif event.key == pygame.K_1:
                current_color = colorRED
            elif event.key == pygame.K_2:
                current_color = colorBLUE
            elif event.key == pygame.K_3:
                current_color = colorGREEN
            elif event.key == pygame.K_4:
                current_color = colorBLACK

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
