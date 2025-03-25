# Import necessary libraries
import random
import time

import pygame

from color_palette import *  # Import custom color definitions

# Initialize pygame
pygame.init()

# Screen dimensions and settings
WIDTH = 600
HEIGHT = 600
CELL = 30  # Size of each grid cell

# Create the game window
screen = pygame.display.set_mode((HEIGHT, WIDTH))

# Fonts and game over text
font1 = pygame.font.SysFont("Verdana", 60)
image_game_over = font1.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))


# Function to draw a simple grid
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)


# Function to draw a chessboard-like grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(
                screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL)
            )


# Class representing a point on the grid
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"


# Class representing the snake
class Snake:
    def __init__(self):
        # Initialize the snake's body, direction, score, and level
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1  # Horizontal movement direction
        self.dy = 0  # Vertical movement direction
        self.score = 0
        self.level = 1

    # Move the snake by updating its body positions
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    # Draw the snake on the screen
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(
                screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL)
            )

    # Check if the snake's head collides with the food
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))  # Grow the snake
            self.score += 1

            # Increase level every 3 points
            if self.score % 3 == 0:
                self.level += 1
                return "LEVEL_UP"
            return "ATE"
        return None


# Class representing the food
class Food:
    def __init__(self):
        # Initialize food position and value
        self.pos = Point(9, 9)
        self.value = random.randint(1, 10)

    # Draw the food on the screen
    def draw(self):
        pygame.draw.rect(
            screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        )

    # Generate a random position for the food, avoiding the snake's body
    def generate_rand(self, snake_body):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            conflict = False
            for segment in snake_body:
                if segment.x == x and segment.y == y:
                    conflict = True
                    break
            if not conflict:
                self.pos = Point(x, y)
                break


# Game settings
FPS = 5  # Frames per second
clock = pygame.time.Clock()

# Initialize game objects
food = Food()
snake = Snake()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit the game
            running = False
        if event.type == pygame.KEYDOWN:  # Handle key presses
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    # Draw the chessboard grid
    draw_grid_chess()

    # Move the snake and check for collisions
    snake.move()
    result = snake.check_collision(food)

    # Handle food collision
    if result == "ATE" or result == "LEVEL_UP":
        food.generate_rand(snake.body)
        if result == "LEVEL_UP":
            FPS += 2  # Increase game speed

    # Check if the snake hits the wall
    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Snake hit the wall!")
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False

    # Draw the snake and food
    snake.draw()
    food.draw()

    # Display score and level
    font_info = pygame.font.SysFont("Verdana", 20)
    score_text = font_info.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font_info.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    # Update the display and control the frame rate
    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
