import sys
from colorama import Fore

def get_directory_path_from_args():
    """Перевіряє наявність аргументу командного рядка та повертає шлях."""
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Необхідно вказати шлях до директорії.")
        sys.exit(1)
    return sys.argv[1]
