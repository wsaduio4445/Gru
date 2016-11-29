import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32) #screen and size 5

image1_filename='img/bg.png'
image2_filename = 'img/bg.png'
bgimage1=pygame.image.load(image1_filename).convert()
bgimage2 = pygame.image.load(image2_filename).convert()
bgimage = [bgimage1,bgimage2] 
x1,y1=0,0#background 7-12

jet1_filename='img/jet.png'#our hero, a jet

running=True



while running:

	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			exit()


	x1-=0.2
	if x1<=-580:
		bgimage = bgimage[1:]+bgimage[:1]
		bgimage1,bgimage2=bgimage
		x1=0
	screen.blit(bgimage1, (x1, y1))
	pygame.display.update() 
