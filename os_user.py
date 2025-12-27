import os
import random


def clear() -> None:
    """Очищает консоль в зависимости от ОС."""

    os.system("cls" if os.name == "nt" else "clear")
