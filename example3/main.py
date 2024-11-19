import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama для коректного кольорового виводу
init(autoreset=True)

def display_directory_structure(path: Path, indent: int = 0):
    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не існує!")
        return

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: '{path}' не є директорією!")
        return

    for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
        if item.is_dir():
            print(f"{' ' * indent}{Fore.BLUE}{item.name}/")
            display_directory_structure(item, indent + 4)  # Рекурсія для піддиректорій
        else:
            print(f"{' ' * indent}{Fore.GREEN}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python main.py <шлях до директорії>")
    else:
        directory_path = Path(sys.argv[1])
        display_directory_structure(directory_path)
