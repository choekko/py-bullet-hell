import pygame
from src.game.game import Game
from src.constants import setting

# 초기화
pygame.font.init()
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
pygame.display.set_caption("Space Jam")

title_image_path = "assets/title.png"
end_image_path = "assets/end.png"

game_status = 'LOBBY'
prev_game_status = None
game_score = 0

def handle_game_end():
  global game_status
  game_status = 'END'

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      if game_status == 'LOBBY':
        game_status = 'PROCESSING'
      elif game_status == 'END':
        game_status = 'LOBBY'
      
    is_game_status_updated = prev_game_status != game_status

    if is_game_status_updated:

      if game_status == 'LOBBY':
        screen.fill((0, 0, 0)) 
        title_image = pygame.image.load(title_image_path)
        title_rect = title_image.get_rect()
        title_rect.center = (setting.SCREEN_WIDTH // 2, setting.SCREEN_HEIGHT // 2 - 50)
        text = pygame.font.Font(None, 36).render("press [SPACE] to start", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (setting.SCREEN_WIDTH // 2, setting.SCREEN_HEIGHT // 2 + 50)
        screen.blit(title_image, title_rect)
        screen.blit(text, text_rect)
      
      if game_status == 'PROCESSING':
        game = Game(screen, handle_game_end)

      if game_status == 'END':
        end_image = pygame.image.load(end_image_path)
        end_rect = end_image.get_rect()
        end_rect.center = (setting.SCREEN_WIDTH // 2, setting.SCREEN_HEIGHT // 2 - 70)
        text = pygame.font.Font(None, 36).render("press [SPACE] to go to lobby", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (setting.SCREEN_WIDTH // 2, setting.SCREEN_HEIGHT // 2 + 50)
        screen.blit(end_image, end_rect)
        screen.blit(text, text_rect)
        game_score = 0
      
      prev_game_status = game_status

  if game_status == 'PROCESSING':
    # 게임 업데이트 및 그리기
    game.update()
    game.draw()

  pygame.display.flip()

# 게임 종료
pygame.quit()