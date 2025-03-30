import random
import time

import pygame

# Initialize all pygame modules
pygame.init()

# Window dimensions
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
image_background = pygame.image.load("resources/AnimatedStreet.png")
image_player = pygame.image.load("resources/Player.png")
image_enemy = pygame.image.load("resources/Enemy.png")
image_coin = pygame.image.load("resources/coin.png")
pygame.transform.scale_by(image_coin, 0.5)  # Scale the coin image

# Load background music and play in loop
pygame.mixer.music.load("resources/background.wav")
pygame.mixer.music.play(-1)  # -1 means infinite loop

# Load crash sound
sound_crash = pygame.mixer.Sound("resources/crash.wav")

# Game Over screen setup
font1 = pygame.font.SysFont("Verdana", 60)
image_game_over = font1.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Font for score display
font2 = pygame.font.SysFont("Verdana", 50)


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5
        self.score = 0  # Player's coin score

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        # Keep player inside screen borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# Enemy car class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10

    def generate_random_rect(self):
        # Randomly position the enemy at the top
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        # Reset enemy if it moves off screen
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 10)  # Random coin value
        self.speed = 10

    def generate_random_rect(self):
        # Randomly position the coin at the top
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        # Respawn coin if it moves off screen
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# Main game loop control
running = True
clock = pygame.time.Clock()
FPS = 60

# Create instances
player = Player()
enemy = Enemy()
coin = Coin()

# Sprite groups for updates and collisions
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

# Add sprites to appropriate groups
all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update score display
    image_coin_score = font2.render(f"{player.score}", True, "black")
    image_coin_score_rect = image_coin_score.get_rect()

    # Move player
    player.move()

    # Draw background
    screen.blit(image_background, (0, 0))

    # Move and draw all game objects
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Check collision with enemy
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)

    # Check collision with coin
    if pygame.sprite.spritecollide(player, coin_sprites, False):
        player.score += coin.value  # Increase score by coin value
        enemy.speed += coin.value / 24  # Slightly increase enemy speed
        pygame.display.flip()
        coin.kill()  # Remove old coin

        # Spawn a new coin
        new_coin = Coin()
        new_coin.generate_random_rect()
        coin = new_coin
        coin_sprites.add(coin)
        all_sprites.add(coin)

    # Show current score
    screen.blit(image_coin_score, (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

# Exit game
pygame.quit()
