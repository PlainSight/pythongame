import pygame, sys
from pygame.locals import *

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

clock =pygame.time.Clock()


thing = pygame.image.load('thing.png')

x = 0
y = 0

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
    	pygame.quit()
    	sys.exit()
    if not hasattr(event, 'key'): continue
    if event.key == K_LEFT: x = x - 1
    if event.key == K_RIGHT: x = x + 1
    if event.key == K_UP: y = y - 1
    if event.key == K_DOWN: y = y + 1

  clock.tick(30)
  screen.fill((0,0,0))
  screen.blit(thing, (x, y))
  pygame.display.flip()