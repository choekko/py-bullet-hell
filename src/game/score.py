import pygame
from constants import setting

class Score:
  def __init__(self, start_time):
    self.start_time = start_time
    self.score = 0

  def update(self):
    self.score = (pygame.time.get_ticks() - self.start_time) // 1000

  def draw(self, screen):
    # 점수 렌더링
    text = pygame.font.Font(None, 36).render("Score: " + str(self.score), True, (255, 255, 255))

    # 텍스트 위치 설정
    text_rect = text.get_rect()
    text_rect.x = 10
    text_rect.y = setting.SCREEN_HEIGHT - 30
    screen.blit(text, text_rect)