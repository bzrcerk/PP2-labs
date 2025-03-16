import pygame
import time

pygame.init()

#CONSTANTS
W, H = 800, 600
CENTER = (W//2, H//2)
BG_COLOR = (0, 0, 0)

#MAIN PARAMS
screen = pygame.display.set_mode((W, H))
running = True

#IMPORTS OF IMAGES
clock_img = pygame.image.load('clock.png')
min_img = pygame.image.load('min_hand.png')
sec_img = pygame.image.load('sec_hand.png')

# FUNC OF ROTATING
def rotating(surface, image, angle, pos):
	rotated = pygame.transform.rotate(image, angle)
	new_rect = rotated.get_rect(center=pos)
	surface.blit(rotated, new_rect.topleft)


#MAIN LOOP
while running:
	
	screen.fill(BG_COLOR)	# COLOR OF BG
	screen.blit(clock_img, (0,0)) # PASTE IMG MICKEY

	# GET TIME
	current_time = time.localtime()
	mins = current_time.tm_min
	secs = current_time.tm_sec

	# ANGLES
	min_ang = -(mins*6)
	sec_ang = -(secs*6)

	rotating(screen, min_img, min_ang, CENTER)
	rotating(screen, sec_img, sec_ang, CENTER)

	pygame.display.flip()
	pygame.time.delay(1000)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False



pygame.quit()