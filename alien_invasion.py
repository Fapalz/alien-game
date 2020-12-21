import os
import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Отображение последнего прорисованного экрана.
            self.screen.fill(self.setting.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    print('yes')
    ai = AlienInvasion()
    ai.run_game()
