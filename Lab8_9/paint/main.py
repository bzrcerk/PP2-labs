# Import necessary modules
import math

import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions and create a window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))  # Fill the background with white color

# Define commonly used colors
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorGREEN = (0, 255, 0)
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)

# List of color options and default selected color
colors = [colorRED, colorBLUE, colorGREEN, colorBLACK]
current_color = colorRED

# Create clock for controlling frame rate
clock = pygame.time.Clock()

# Variables for mouse state and drawing
LMBpressed = False  # Left Mouse Button pressed flag
THICKNESS = 5  # Drawing thickness
currX = currY = 0  # Current mouse position
prevX = prevY = 0  # Previous mouse position

# Default drawing tool
# Options: RECT, CIRCLE, ERASER, FREEHAND, SQUARE, TRIANGLE, EQ_TRIANGLE, RHOMBUS
tool = "RECT"


# Helper function to get a rectangle from two diagonal points
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


# Main loop
running = True
while running:
    for event in pygame.event.get():
        # Quit the application
        if event.type == pygame.QUIT:
            running = False

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos  # Store starting point

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos  # Get ending point

        # Handle mouse movement (dragging)
        if event.type == pygame.MOUSEMOTION:
            currX, currY = event.pos
            if LMBpressed:
                if tool == "FREEHAND":
                    pygame.draw.line(
                        screen, current_color, (prevX, prevY), (currX, currY), THICKNESS
                    )
                    prevX, prevY = currX, currY  # Update previous position

                elif tool == "ERASER":
                    pygame.draw.line(
                        screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS
                    )
                    prevX, prevY = currX, currY
                # Draw shapes based on selected tool
                elif tool == "RECT":
                    pygame.draw.rect(
                        screen,
                        current_color,
                        calculate_rect(prevX, prevY, currX, currY),
                        THICKNESS,
                    )

                elif tool == "CIRCLE":
                    radius = int(
                        math.hypot(currX - prevX, currY - prevY)
                    )  # Calculate radius using distance formula
                    pygame.draw.circle(
                        screen, current_color, (prevX, prevY), radius, THICKNESS
                    )

                elif tool == "SQUARE":
                    side = min(
                        abs(currX - prevX), abs(currY - prevY)
                    )  # Calculate equal side length
                    square_rect = pygame.Rect(prevX, prevY, side, side)
                    pygame.draw.rect(screen, current_color, square_rect, THICKNESS)

                elif tool == "TRIANGLE":  # Right triangle
                    pygame.draw.polygon(
                        screen,
                        current_color,
                        [(prevX, prevY), (prevX, currY), (currX, currY)],
                        THICKNESS,
                    )

                elif tool == "EQ_TRIANGLE":  # Equilateral triangle
                    height = int(
                        (3**0.5 / 2) * abs(currX - prevX)
                    )  # Height based on side length
                    top = (prevX + (currX - prevX) // 2, prevY)
                    left = (prevX, prevY + height)
                    right = (currX, prevY + height)
                    pygame.draw.polygon(
                        screen, current_color, [top, left, right], THICKNESS
                    )

                elif tool == "RHOMBUS":
                    # Find center and corners of the rhombus
                    mid_x = (prevX + currX) // 2
                    mid_y = (prevY + currY) // 2
                    dx = abs(currX - prevX) // 2
                    dy = abs(currY - prevY) // 2
                    points = [
                        (mid_x, prevY),
                        (currX, mid_y),
                        (mid_x, currY),
                        (prevX, mid_y),
                    ]
                    pygame.draw.polygon(screen, current_color, points, THICKNESS)

                elif tool == "ERASER":
                    # Erase line by drawing in white
                    pygame.draw.line(
                        screen, colorWHITE, (prevX, prevY), (currX, currY), THICKNESS
                    )

        # Handle key presses to change tools or settings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # Increase thickness
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Decrease thickness, minimum 1

            # Tool selection keys
            elif event.key == pygame.K_r:
                tool = "RECT"
            elif event.key == pygame.K_c:
                tool = "CIRCLE"
            elif event.key == pygame.K_e:
                tool = "ERASER"
            elif event.key == pygame.K_f:
                tool = "FREEHAND"
            elif event.key == pygame.K_s:
                tool = "SQUARE"
            elif event.key == pygame.K_t:
                tool = "TRIANGLE"
            elif event.key == pygame.K_q:
                tool = "EQ_TRIANGLE"
            elif event.key == pygame.K_h:
                tool = "RHOMBUS"

            # Color selection keys
            elif event.key == pygame.K_1:
                current_color = colorRED
            elif event.key == pygame.K_2:
                current_color = colorBLUE
            elif event.key == pygame.K_3:
                current_color = colorGREEN
            elif event.key == pygame.K_4:
                current_color = colorBLACK

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame after loop ends
pygame.quit()
