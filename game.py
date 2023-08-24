import sys
import pygame

from scripts.entities import PhysicsEntity

class Game:
  def __init__(self):

    pygame.init()
    pygame.display.set_caption('Silencer')
    self.screen = pygame.display.set_mode((640, 480))    # set_mode function creates window

    self.clock = pygame.time.Clock() # forces game to run at specific frame rate

    self.img = pygame.image.load('data/images/clouds/cloud_1.png')
    self.img.set_colorkey((0,0,0))      # makes color become transparent if same color

    self.img_pos = [160, 260]
    self.movement = [False, False]

    self.collision_area = pygame.Rect(50, 50, 300, 50)

    self.player = PhysicsEntity(self, 'player', (50,50), (8,15))

  def run(self):
    # Game screen runs in continuous loop with changing data
    while True:
      self.screen.fill('crimson')      # colors as rgb,text,hex / covers trailing images after movement

      # rectangle collision
      img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
      if img_r.colliderect(self.collision_area):
        pygame.draw.rect(self.screen, 'green', self.collision_area)
      else:
        pygame.draw.rect(self.screen, 'grey', self.collision_area)

      # cloud movement
      self.img_pos[1] += (self.movement[1] - self.movement[0]) * 3    # method of adding boolean / multiplication affects speed
      self.screen.blit(self.img, self.img_pos)

      # player
      self.player.update((self.movement[1] - self.movement[0], 0))    # (x,y)
      self.player.render(self.screen)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:   # registers pressing x button to close screen
          pygame.quit()
          sys.exit()
        if event.type == pygame.KEYDOWN:    # key pressed
          if event.key == pygame.K_UP:
            self.movement[0] = True
          if event.key == pygame.K_DOWN:
            self.movement[1] = True
          if event.key == pygame.K_LEFT:
            self.movement[0] = True
          if event.key == pygame.K_RIGHT:
            self.movement[1] = True
        if event.type == pygame.KEYUP:      # key release
          if event.key == pygame.K_UP:
            self.movement[0] = False
          if event.key == pygame.K_DOWN:
            self.movement[1] = False
          if event.key == pygame.K_LEFT:
            self.movement[0] = False
          if event.key == pygame.K_RIGHT:
            self.movement[1] = False


      pygame.display.update()
      self.clock.tick(60)    # dynamic sleep to maintain 60fps

Game().run()    # initialize game to run