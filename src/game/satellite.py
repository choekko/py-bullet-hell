from constants import sprite
import pygame
import math
from constants import setting


class Satellite:
  def __init__(self, start_time):
    super().__init__()
    self.start_time = start_time
    self.image = sprite.SATELLITE
    self.rect = self.image.get_rect()

  def update(self, core_x, core_y):
    current_time = pygame.time.get_ticks()
    current_degree = (self.start_time - current_time) / 200 % 360
    self.rect.center = (core_x + setting.SATELLITE_DISTANCE * math.cos(current_degree), core_y + setting.SATELLITE_DISTANCE * math.sin(current_degree))
    
  def draw(self, screen):
    screen.blit(self.image, self.rect)