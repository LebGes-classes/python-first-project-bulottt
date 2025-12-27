from menu import Menu
from game import Game

if __name__ == "__main__":
    menu = Menu()
    game = Game()

    while True:
        choice = menu.show().strip()

        if choice == "1":
            game.play()
        elif choice == "2":
            menu.rules()
        elif choice == "3":
            break
