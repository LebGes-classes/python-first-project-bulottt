from os_user import clear
from renderer import Renderer
from maze import Maze
from player import Player

class Game:
    """Управляет игровым процессом."""

    def __init__(self) -> None:
        self.renderer = Renderer()

    def play(self) -> None:
        maze = Maze(15)
        maze.generate()
        player = Player(maze.start_x, maze.start_y)

        while True:
            self.renderer.draw(maze, player)

            key = input(">>> ").lower()

            if key == "q":
                return

            if key == "w":
                player.move(0, -1, maze)
            elif key == "s":
                player.move(0, 1, maze)
            elif key == "a":
                player.move(-1, 0, maze)
            elif key == "d":
                player.move(1, 0, maze)

            if maze.is_exit(player.x, player.y):
                self.show_win(player.steps)
                return


    def show_win(self, steps) -> None:
        clear()
        print("=" * 60)
        print(" " * 18 + "УРОВЕНЬ ПРОЙДЕН")
        print("=" * 60)
        print("Шагов сделано:", steps)
        print("=" * 60)
        input("Enter — в меню")