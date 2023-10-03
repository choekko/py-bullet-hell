import pygame
import math
from constants import direction

def handle_arrow_key_pressed(up=lambda:None, down=lambda:None, left=lambda:None, right=lambda:None, other=lambda: None):
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
      left()
  elif keys[pygame.K_RIGHT]:
      right()
  elif keys[pygame.K_UP]:
      up()
  elif keys[pygame.K_DOWN]:
      down()
  else:
    other()

def get_reversed_direction(_direction):
  return direction.Direction(-_direction.x, -_direction.y)

def calculate_angle(direction):
  # atan2 함수를 사용하여 각도 계산 (라디안 단위)
  angle_radians = math.atan2(-direction.y, direction.x)
  
  # 라디안에서 도(degree)로 변환
  angle_degrees = math.degrees(angle_radians)
  
  return angle_degrees


def is_collided(rect1, rect2):
  distance = math.sqrt((rect1.center[0] - rect2.center[0])**2 + (rect1.center[1] - rect2.center[1]) ** 2)
  return distance < 10
