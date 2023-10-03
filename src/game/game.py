import pygame
import random
from game.utils import get_reversed_direction, is_collided
from game.player import Player
from game.enemy import Enemy
from game.score import Score
from constants import direction, setting



class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks();

        # 게임 초기화 및 리소스 로드
        self.player = Player(self.start_time)
        self.enemies = []
        self.background_speed = 0
        self.background_direction = direction.UP
        self.score = Score(self.start_time)
            

    def update(self):
        # 게임 로직 업데이트
        self.player.update()
        self.score.update()
        self.background_direction = get_reversed_direction(self.player.direction)
        self.background_speed = self.player.speed

        for enemy in self.enemies:
            enemy.update(self.background_speed, self.background_direction)

        # 무작위로 적 생성
        if random.randint(1, 100) < 3:
            self.enemies.append(Enemy())

        # 충돌 검사
        for enemy in self.enemies:
            if is_collided(self.player.rect, enemy.rect):
                pygame.quit()
                quit()

    def draw(self):
        # 게임 객체 그리기
        self.screen.fill((0, 0, 0))  # 배경을 검정색으로 지우기

        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

        self.score.draw(self.screen)





