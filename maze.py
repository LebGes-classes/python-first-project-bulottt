import random

class Maze:
    """
    Класс лабиринта.

    Хранит двумерный список клеток:
    '██' — стена
    ' ' — проход
    'XX' — выход

    Лабиринт генерируется с помощью рекурсивного обхода.
    """

    def __init__(self, size) -> None:
        """
        Создаёт лабиринт заданного размера.

        Если размер чётный, он увеличивается на 1,
        чтобы генерация работала корректно.
        """

        if size % 2 == 0:
            size += 1

        self.size = size
        self.grid = []

        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append("██")
            self.grid.append(row)

        self.start_x = 1
        self.start_y = 1
        self.exit_x = self.size - 2
        self.exit_y = self.size - 2

    def generate(self) -> None:
        """Запускает генерацию лабиринта и ставит выход."""

        self._dig(self.start_x, self.start_y)
        self.grid[self.exit_y][self.exit_x] = "XX"

    def _dig(self, x, y) -> None:
        """Рекурсивно делает проходы в лабиринте, начиная с клетки (x, y)."""

        self.grid[y][x] = " "

        directions = [
            (2, 0),
            (-2, 0),
            (0, 2),
            (0, -2)
        ]

        random.shuffle(directions)

        for d in directions:
            dx = d[0]
            dy = d[1]

            nx = x + dx
            ny = y + dy

            if nx > 0 and nx < self.size - 1 and ny > 0 and ny < self.size - 1:
                if self.grid[ny][nx] == "██":
                    wall_x = x + dx // 2
                    wall_y = y + dy // 2
                    self.grid[wall_y][wall_x] = " "
                    self._dig(nx, ny)

    def in_bounds(self, x, y) -> bool:
        """Проверяет, находятся ли координаты внутри лабиринта."""

        if x < 0:
            return False
        if y < 0:
            return False
        if x >= self.size:
            return False
        if y >= self.size:
            return False
        return True

    def is_wall(self, x, y) -> bool:
        """Проверяет, является ли клетка стеной."""

        return self.grid[y][x] == "██"

    def is_exit(self, x, y) -> bool:
        """Проверяет, является ли клетка выходом."""

        return self.grid[y][x] == "XX"