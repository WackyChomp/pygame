import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
      self.game = game
      self.type = e_type          # entity type
      self.pos = list(pos)        # each entity having their own list for its position
      self.size = size
      self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
      frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])      

      self.pos[0] += frame_movement[0]      # x position
      self.pos[1] += frame_movement[1]      # y position

    def render(self, surf):
      surf.blit(self.game.assets['player'], self.pos)