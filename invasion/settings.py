class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (167, 122, 145)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullets_speed = 1
        self.bullets_width = 3
        self.bullets_height = 15
        self.bullets_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.12
        self.fleet_drop_speed = 50
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.2
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullets_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)