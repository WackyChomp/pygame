import sys
import pygame


pygame.init()

pygame.display.set_caption('Silencer')

screen = pygame.display.set_mode((640, 480))    # set_mode function creates window

clock = pygame.time.Clock() # forces game to run at specific frame rate


# Game screen runs in continuous loop with changing data
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:   # registers pressing x button to close screen
      pygame.quit()
      sys.exit()

  pygame.display.update()
  clock.tick(60)    # dynamic sleep to maintain 60fps