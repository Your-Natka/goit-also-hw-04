import sys
from parser import parse_input
from commands import execute_command


def main(directory):
    """
    Основна функція, яка приймає шлях до директорії та реалізує цикл взаємодії з користувачем.
    """
    print(f"Welcome to the assistant bot! Working directory: {directory}")
    
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
    # Перевірка аргументів командного рядка
    if len(sys.argv) != 2:
        print("Використання: python main.py <шлях до директорії>")
        sys.exit(1)

    # Зчитуємо шлях до директорії
    directory_path = sys.argv[1]

    # Передаємо шлях до функції main
    main(directory_path)
