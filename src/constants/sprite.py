import pygame
import os

# 현재 스크립트 파일의 디렉토리
_current_dir = os.path.dirname(__file__)
_player_image_path = os.path.join(_current_dir, "..", "..", "assets/player/ship.png")
_enemy_image_path = os.path.join(_current_dir, "..", "..", "assets/enemy/ship.png")

PLAYER_FLOATING_1 = pygame.image.load(_player_image_path).subsurface(pygame.Rect(0, 0, 30, 30))

ENEMY_FLOATING_1 = pygame.image.load(_enemy_image_path).subsurface(pygame.Rect(5, 5, 20, 20))