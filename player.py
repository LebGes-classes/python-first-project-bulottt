class Player:
    """Класс игрока, хранит позицию игрока и количество сделанных шагов."""

    def __init__(self, x, y) -> None:
        """Создаёт игрока в стартовой позиции."""

        self.x = x
        self.y = y
        self.steps = 0

    def move(self, dx, dy, maze) -> None:
        """Пытается переместить игрока. Если ход невозможен (стена или выход за границы),игрок остаётся на месте."""

        nx = self.x + dx
        ny = self.y + dy

        if not maze.in_bounds(nx, ny):
            return

        if maze.is_wall(nx, ny):
            return

        self.x = nx
        self.y = ny
        self.steps += 1