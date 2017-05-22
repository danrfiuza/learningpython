# INTIALISATION
import pygame,math,sys # import libraries
from pygame.locals import *
screen = pygame.display.set_mode((800,600)) #start display
character = pygame.image.load('character.png') #load sprite
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
x = y = 200
speed = direction = 10
position = (x,y)
BLACK = (0,0,0)

#main loop
while 1:
	# USER INPUT
	clock.tick(FRAMES_PER_SECOND)
	for event in pygame.event.get():
		if not hasattr(event,'key'):continue
		down = event.type == KEYDOWN
		if   event.key == K_RIGHT:
			x += speed
			print('RIGHT')
		elif event.key == K_LEFT:
			x -= speed
			print('LEFT')
		elif event.key == K_UP:
			y -= speed
			print('UP')
		elif event.key == K_DOWN:
			y += speed
			print('DOWN')
		elif event.key == K_ESCAPE: sys.exit(0) #quit game
	screen.fill(BLACK)
	position = (x , y)

	#RENDERING
	#..rotate the character image for direction
	# rotated = pygame.transform.rotate(character, direction)
	#.. position the character  on screen
	# rect = rotated.get_rect()
	# rect.center = position
	# .. render the character to screen
	screen.blit(character,position)
	pygame.display.flip()
