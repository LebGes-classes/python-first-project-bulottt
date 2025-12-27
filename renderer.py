from os_user import clear

class Renderer:
    """Отвечает только за отображение игры в консоли."""

    def draw(self, maze, player) -> None:
        clear()
        print("=" * 60)
        print(" " * 22 + "ЛАБИРИНТ")
        print("=" * 60)
        print("Шаги:", player.steps)
        print()

        for y in range(maze.size):
            line = ""
            for x in range(maze.size):
                if x == player.x and y == player.y:
                    line += "@@"
                else:
                    if maze.grid[y][x] == "██":
                        line += "██"
                    elif maze.grid[y][x] == "XX":
                        line += "XX"
                    else:
                        line += "  "
            print("  " + line)

        print()
        print("W A S D — движение | Q — выход")