import sys
import pygame


class Game:
  def __init__(self):

    pygame.init()
    pygame.display.set_caption('Silencer')
    self.screen = pygame.display.set_mode((640, 480))    # set_mode function creates window

    self.clock = pygame.time.Clock() # forces game to run at specific frame rate

  def run(self):
    # Game screen runs in continuous loop with changing data
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:   # registers pressing x button to close screen
          pygame.quit()
          sys.exit()

      pygame.display.update()
      self.clock.tick(60)    # dynamic sleep to maintain 60fps

Game().run()    # initialize game to run