import pygame

pygame.init()

W,H = 800, 800
BG_COLOR = (0, 0, 0)
MOVE_SP = 20
circle_x = H//2
circle_y = W//2

screen = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()
FPS = 60

running = True

up_pressed = False
down_pressed = False
right_pressed = False
left_pressed = False

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pressed_keys = pygame.key.get_pressed()       
	if pressed_keys[pygame.K_UP] and circle_y - 25 > 0:
		circle_y -= MOVE_SP
	if pressed_keys[pygame.K_DOWN] and circle_y + 25 < H:
		circle_y += MOVE_SP
	if pressed_keys[pygame.K_RIGHT] and circle_x + 25 < W:
		circle_x += MOVE_SP
	if pressed_keys[pygame.K_LEFT] and circle_x - 25 > 0:
		circle_x -= MOVE_SP

	screen.fill(BG_COLOR)
	pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 25)

	pygame.display.flip()
	clock.tick(FPS)
		