import pygame
import os

pygame.init()
pygame.mixer.init()

# CONSTANTS
BG_COLOR = (0,0,0)
W, H = 800, 800
screen = pygame.display.set_mode((W, H))


# MUSIC DIR
MUSIC_DIR = 'music'
playlist = [t for t in os.listdir(MUSIC_DIR) if t.endswith('.mp3')]
curr_t = 0

# FUNC TO LOAD AND PLAY
def pl():
	pygame.mixer.music.load(os.path.join(MUSIC_DIR, playlist[curr_t]))
	pygame.mixer.music.play()
	print(f'Playing: {playlist[curr_t]}')

if playlist:
	pl()
else:
	print('No availible music in folder')

running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				if not pygame.mixer.music.get_busy():
					pl()
			elif event.key == pygame.K_s:
				pygame.mixer.music.pause()
				print('Music on pause')
			elif event.key == pygame.K_n:
				curr_t = (curr_t+1) % len(playlist)
				pl()
			elif event.key == pygame.K_b:
				curr_t = (curr_t-1) % len(playlist)
				pl()



pygame.quit()
