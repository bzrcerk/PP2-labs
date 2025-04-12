import random
import time

import psycopg2
import pygame

from color_palette import *

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="123456789",
    port="5432",
)


def create_table_if_not_exists():
    with conn.cursor() as cursor:
        cursor.execute(
            """
						CREATE TABLE IF NOT EXISTS users (
								id SERIAL PRIMARY KEY,
								username VARCHAR(50) UNIQUE NOT NULL
						);
						"""
        )
        cursor.execute(
            """
						CREATE TABLE IF NOT EXISTS user_score (
								id SERIAL PRIMARY KEY,
								user_id INTEGER REFERENCES users(id),
								score INTEGER NOT NULL,
								level INTEGER NOT NULL,
								created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
						);
						"""
        )
        conn.commit()


# Get or create user and load state
def get_or_create_user():
    username = input("Enter your username: ").strip()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user:
            user_id = user[0]
            cursor.execute(
                "SELECT score, level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1",
                (user_id,),
            )
            state = cursor.fetchone()
            if state:
                print(
                    f"Welcome back, {username}! Your level: {state[1]}, score: {state[0]}"
                )
                return user_id, state[1], state[0]
            else:
                return user_id, 1, 0
        else:
            cursor.execute(
                "INSERT INTO users (username) VALUES (%s) RETURNING id", (username,)
            )
            user_id = cursor.fetchone()[0]
            conn.commit()
            print(f"New user created: {username}")
            return user_id, 1, 0


# Initialize pygame
pygame.init()
WIDTH, HEIGHT, CELL = 600, 600, 30
screen = pygame.display.set_mode((HEIGHT, WIDTH))
font1 = pygame.font.SysFont("Verdana", 60)
image_game_over = font1.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

create_table_if_not_exists()


# Draw grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(
                screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL)
            )


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score, self.level = 0, 1

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(
                screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL)
            )

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            self.score += food.value
            if self.score % 3 == 0:
                self.level += 1
                return "LEVEL_UP"
            return "ATE"
        return None


class Food:
    def __init__(self):
        self.generate_new()

    def generate_new(self):
        self.pos = Point(
            random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)
        )
        self.value = random.randint(1, 5)
        self.timer_start = time.time()

    def draw(self):
        pygame.draw.rect(
            screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)
        )
        font = pygame.font.SysFont("Verdana", 15)
        screen.blit(
            font.render(str(self.value), True, colorBLACK),
            (self.pos.x * CELL + 5, self.pos.y * CELL + 5),
        )

    def generate_rand(self, snake_body):
        while True:
            x, y = (
                random.randint(0, WIDTH // CELL - 1),
                random.randint(0, HEIGHT // CELL - 1),
            )
            if not any(segment.x == x and segment.y == y for segment in snake_body):
                self.pos = Point(x, y)
                self.value = random.randint(1, 5)
                self.timer_start = time.time()
                break

    def is_expired(self):
        return time.time() - self.timer_start > 5


# Main Game Start
user_id, start_level, start_score = get_or_create_user()
snake = Snake()
snake.level = start_level
snake.score = start_score
food = Food()

FPS = 5 + 2 * (snake.level - 1)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP:
                snake.dx, snake.dy = 0, -1
            elif event.key == pygame.K_p:
                paused = True
                print("Paused. Press P to resume or S to save.")
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.QUIT:
                            running = False
                            paused = False
                        elif pause_event.type == pygame.KEYDOWN:
                            if pause_event.key == pygame.K_p:
                                paused = False
                            elif pause_event.key == pygame.K_s:
                                with conn.cursor() as cursor:
                                    cursor.execute(
                                        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                                        (user_id, snake.score, snake.level),
                                    )
                                    conn.commit()
                                    print("Game saved.")
                                    print(f"Level: {snake.level}, Score: {snake.score}")

    draw_grid_chess()
    snake.move()
    result = snake.check_collision(food)

    if result in ["ATE", "LEVEL_UP"]:
        food.generate_rand(snake.body)
        if result == "LEVEL_UP":
            FPS += 2

    if food.is_expired():
        food.generate_rand(snake.body)

    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)
        running = False

    snake.draw()
    food.draw()
    font_info = pygame.font.SysFont("Verdana", 20)
    screen.blit(font_info.render(f"Score: {snake.score}", True, colorBLACK), (10, 10))
    screen.blit(font_info.render(f"Level: {snake.level}", True, colorBLACK), (10, 40))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
