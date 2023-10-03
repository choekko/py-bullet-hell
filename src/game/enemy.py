import pygame
import random
import math
from game.utils import calculate_angle
from constants import sprite, direction, setting


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite.ENEMY_FLOATING_1
        self.rotated_image = self.image
        self._init_status()

    def _init_status(self):
      initial_positions = [
        (-20, random.randint(0, setting.SCREEN_HEIGHT)),  # 왼쪽에서 오른쪽
        (setting.SCREEN_WIDTH + 20, random.randint(0, setting.SCREEN_HEIGHT)),  # 오른쪽에서 왼쪽
        (random.randint(0, setting.SCREEN_WIDTH), -20),  # 위에서 아래로
        (random.randint(0, setting.SCREEN_WIDTH), setting.SCREEN_HEIGHT + 20),  # 아래에서 위로
      ]

      initial_x, initial_y = random.choice(initial_positions)

      target_x = setting.SCREEN_WIDTH // 2 + random.randint(-50, 50)
      target_y = setting.SCREEN_HEIGHT // 2 + random.randint(-50, 50)
      direction_x = target_x - initial_x
      direction_y = target_y - initial_y
      length = math.sqrt(direction_x ** 2 + direction_y ** 2)
      _direction = direction.Direction(direction_x / length, direction_y / length)

      self.rect = self.image.get_rect()
      self.rect.center = (initial_x, initial_y)
      self.x = self.rect.x
      self.y = self.rect.y
      self.direction = _direction
      self.speed = setting.ENEMY_SPEED
      self.rotated_image = pygame.transform.rotate(self.image, 90 + calculate_angle(_direction))

    def update(self, background_speed=0, background_direction=direction.UP):
        self.x += self.speed * self.direction.x + background_speed * background_direction.x
        self.y += self.speed * self.direction.y + background_speed * background_direction.y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)