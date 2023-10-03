import pygame
from constants import sprite, direction
from game.utils import handle_arrow_key_pressed

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite.PLAYER_FLOATING_1
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.direction = direction.UP
        self.rotated_image = self.image
        self.speed = 0

    def _handle_arrow_key_pressed(self, type):
      self.direction = direction.DIRECTION.get(type)
      self.rotated_image = pygame.transform.rotate(self.image, self.direction.angle)
      self.speed = 1.5

    def _stop(self):
      self.speed = 0

    def update(self):
      handle_arrow_key_pressed(
        right=lambda:self._handle_arrow_key_pressed('RIGHT'),
        left=lambda:self._handle_arrow_key_pressed('LEFT'),
        down=lambda:self._handle_arrow_key_pressed('DOWN'),
        up=lambda:self._handle_arrow_key_pressed('UP'),
        other=lambda:self._stop()
      )

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)