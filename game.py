import pygame, sys
from pygame.locals import *
import pickle

WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

clock = pygame.time.Clock()

thing = pygame.image.load('thing.png')

class Minion:
  def __init__(self):
    self.x = 50
    self.y = 50
    self.vx = 0
    self.vy = 0
    self.sprite = thing

  def setPos(pos):
    self.x = pos.x
    self.y = pos.y

  def update(self):
    self.x += self.vx
    self.y += self.vy

  def render(self):
    screen.blit(self.sprite, (self.x, self.y))

cc = Minion()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
    	pygame.quit()
    	sys.exit()
    if not hasattr(event, 'key'): continue
    if event.type == KEYDOWN:
      if event.key == K_LEFT: cc.vx = -10
      if event.key == K_RIGHT: cc.vx = 10
      if event.key == K_UP: cc.vy = -10
      if event.key == K_DOWN: cc.vy = 10
    if event.type == KEYUP:
      if event.key == K_LEFT: cc.vx = 0
      if event.key == K_RIGHT: cc.vx = 0
      if event.key == K_UP: cc.vy = 0
      if event.key == K_DOWN: cc.vy = 0

  pickle.dumps()

  payload = pickle.loads()

  clock.tick(60)
  screen.fill((255,255,255))
  cc.update()
  cc.render()

  pygame.display.flip()

