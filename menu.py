from os_user import clear

class Menu:
    """Отвечает за меню и правила."""

    def show(self) -> str:
        clear()
        print("=" * 60)
        print(" " * 24 + "MAZE GAME")
        print("=" * 60)
        print("1. Новая игра")
        print("2. Правила")
        print("3. Выход")
        print("=" * 60)
        return input("Выберите (1-3): ")

    def rules(self) -> None:
        clear()
        print("ПРАВИЛА")
        print()
        print("Дойти от @@ до XX")
        print("W A S D — движение")
        print("Q — выход")
        input("\nEnter...")