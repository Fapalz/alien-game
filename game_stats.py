class GameStats:
    """Отслеживание статистики игры."""

    def __init__(self, ai_game):
        """Инициализация статистики"""
        self.settings = ai_game.settings
        self.ships_left = 1
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False
        self.score = 0

        # Рекорд не должен сбрасываться.
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1