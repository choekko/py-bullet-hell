import pygame
from constants import sprite, direction
from game.utils import handle_arrow_key_pressed

class Player(pygame.sprite.Sprite):
    def __init__(self, start_time):
        super().__init__()
        self.clock = pygame.time.Clock()
        self.current_frame = 0
        self.sprite_timer = 0
        self.prev_time = start_time
        self._update_frame()
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.direction = direction.UP
        self.rotated_image = self.image
        self.speed = 0
        self.already_reset = False

    def _update_frame(self, reset_flag=False):
      self.image = sprite.PLAYER_FLOATING_SPRITE_SHEET.subsurface(sprite.PLAYER_FLOATING_FRAMES[self.current_frame])
      if not reset_flag:
        self.already_reset = False
        current_time = pygame.time.get_ticks()
        self.sprite_timer += (current_time - self.prev_time) / 1000

        if self.sprite_timer >= sprite.PLAYER_FRAME_SPEED:
          self.sprite_timer = 0  # 타이머 초기화
          self.prev_time = current_time
          self.current_frame += 1
          if self.current_frame > 3:
            self.current_frame %= 4
  
    def _reset_frame(self):
      if not self.already_reset: 
        self.current_frame = 0
        self._update_frame(True)
        self.already_reset = True

    def _handle_arrow_key_pressed(self, type):
      self.direction = direction.DIRECTION.get(type)
      self.rotated_image = pygame.transform.rotate(self.image, self.direction.angle)
      self.speed = 1.5

    def _stop(self):
      self.speed = 0

    def update(self):
      if self.speed:
        self._update_frame()
      else:
        self._reset_frame()

      handle_arrow_key_pressed(
        right=lambda:self._handle_arrow_key_pressed('RIGHT'),
        left=lambda:self._handle_arrow_key_pressed('LEFT'),
        down=lambda:self._handle_arrow_key_pressed('DOWN'),
        up=lambda:self._handle_arrow_key_pressed('UP'),
        other=lambda:self._stop()
      )

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)