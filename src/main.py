import pygame
from game.game import Game
from constants import setting

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((setting.SCREEN_WIDTH, setting.SCREEN_HEIGHT))
pygame.display.set_caption("Space Jam")

# 게임 인스턴스 생성
game = Game(screen)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 업데이트 및 그리기
    game.update()
    game.draw()

    pygame.display.flip()

# 게임 종료
pygame.quit()