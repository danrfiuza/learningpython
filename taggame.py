# INTIALISATION
import pygame,math,sys # import libraries
from pygame.locals import *
HEIGHT = 320
WIDTH  = 240
screen = pygame.display.set_mode((HEIGHT,WIDTH)) #start display
character = pygame.image.load('character.png') #load sprite
enemy     = pygame.image.load('character.png')
clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
x = y = 200
speed = direction = 10
position = (x,y)
BLACK = (0,0,0) # background color


#CHARACTER CLASS
class CharacterSprite(pygame.sprite.Sprite):
	def  __init__(self,image,x,y,speed):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.x = x
		self.y = y
		self.speed = speed

	def update(self,x,y):
		self.x = x
		self.y = y
		screen.blit(self.src_image,(x,y))

	def get_x():
		return self.x

	def get_y():
		return self.y

#ENEMY CLASS
class EnemySprite(pygame.sprite.Sprite):
	def  __init__(self,image,x,y,speed):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.x = x
		self.y = y
		self.speed = speed

	def draw(self,x,y):
		screen.blit(self.src_image,(self.x,self.y))

	def pursuit(self,CharacterSprite):
		if CharacterSprite.x > self.x : self.x += self.speed
		if CharacterSprite.x < self.x : self.x -= self.speed
		if CharacterSprite.y > self.y : self.y += self.speed
		if CharacterSprite.y < self.y : self.y -= self.speed


character = CharacterSprite('character.png',200,200,10)
enemy = EnemySprite('character.png',100,100,10)
#main loop
while 1:
	# USER INPUT
	clock.tick(FRAMES_PER_SECOND)
	for event in pygame.event.get():
		if not hasattr(event,'key'):continue
		down = event.type == KEYDOWN
		if   event.key == K_RIGHT:
			x += speed
			enemy.pursuit(character)
			print('RIGHT')
		elif event.key == K_LEFT:
			x -= speed
			enemy.pursuit(character)
			print('LEFT')
		elif event.key == K_UP:
			y -= speed
			enemy.pursuit(character)
			print('UP')
		elif event.key == K_DOWN:
			y += speed
			enemy.pursuit(character)
			print('DOWN')
		elif event.key == K_ESCAPE: sys.exit(0) #quit game
	screen.fill(BLACK)
	position = (x,y)
	print(position)
	#RENDER AND DRAW
	character.update(x,y)
	enemy.draw(100,100)
	#RENDERING
	pygame.display.flip()
