import sys
from parser import parse_input
from commands import execute_command


def main(directory=None):
    """
    Основна функція, яка приймає шлях до директорії (опціонально)
    та реалізує цикл взаємодії з користувачем.
    """
    if directory:
        print(f"Welcome to the assistant bot! Working directory: {directory}")
    else:
        print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            print(execute_command(command, args))


if __name__ == "__main__":
    # Якщо аргумент командного рядка передано, використовуємо його
    directory_path = sys.argv[1] if len(sys.argv) > 1 else None

    # Передаємо шлях до функції main
    main(directory_path)

