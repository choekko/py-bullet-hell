import pygame
import os

# 현재 스크립트 파일의 디렉토리
_player_image_path = "assets/player/ship.png"
_enemy_image_path = "assets/enemy/ship.png"
_frame_width = 32
_frame_height = 32

PLAYER_FLOATING_SPRITE_SHEET = pygame.image.load(_player_image_path);
PLAYER_FLOATING_FRAMES = [
  pygame.Rect(0, 0, _frame_width, _frame_height),
  pygame.Rect(_frame_width, 0, _frame_width, _frame_height),
  pygame.Rect(_frame_width * 2, 0, _frame_width, _frame_height),
  pygame.Rect(_frame_width * 3, 0, _frame_width, _frame_height),
]
PLAYER_FRAME_SPEED = 1

ENEMY_FLOATING_1 = pygame.image.load(_enemy_image_path).subsurface(pygame.Rect(0, 0, _frame_width, _frame_height))
SATELLITE = pygame.image.load(_player_image_path).subsurface(pygame.Rect(_frame_width * 1, _frame_height * 3, _frame_width, _frame_height))