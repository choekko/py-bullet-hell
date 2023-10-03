import pygame
import os

# 현재 스크립트 파일의 디렉토리
_current_dir = os.path.dirname(__file__)
_player_image_path = os.path.join(_current_dir, "..", "..", "assets/player/ship.png")
_enemy_image_path = os.path.join(_current_dir, "..", "..", "assets/enemy/ship.png")
_player_frame_width = 32
_player_frame_height = 32

PLAYER_FLOATING_SPRITE_SHEET = pygame.image.load(_player_image_path);
PLAYER_FLOATING_FRAMES = [
  pygame.Rect(0, 0, _player_frame_width, _player_frame_height),
  pygame.Rect(_player_frame_width, 0, _player_frame_width, _player_frame_height),
  pygame.Rect(_player_frame_width * 2, 0, _player_frame_width, _player_frame_height),
  pygame.Rect(_player_frame_width * 3, 0, _player_frame_width, _player_frame_height),
]
PLAYER_FRAME_SPEED = 1

ENEMY_FLOATING_1 = pygame.image.load(_enemy_image_path).subsurface(pygame.Rect(5, 5, 20, 20))