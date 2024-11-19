from pathlib import Path
from colorama import Fore

def print_directory_structure(path, indent=0):
    """Рекурсивно виводить структуру директорії."""
    try:
        directory = Path(path)
        if not directory.is_dir():
            print(f"{Fore.RED}Помилка: {path} не є директорією.")
            return

        for item in directory.iterdir():
            if item.is_dir():
                print("  " * indent + Fore.BLUE + f"📂 {item.name}")
                print_directory_structure(item, indent + 1)
            elif item.is_file():
                print("  " * indent + Fore.GREEN + f"📜 {item.name}")
    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {e}")
