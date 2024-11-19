from pathlib import Path

def total_salary(path):
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")

        total = 0
        count = 0

        with open(file_path, mode='r', encoding='utf-8') as file:
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print("Помилка у форматі даних в рядку:", line.strip())

        if count == 0:
            raise ValueError("Файл не містить коректних даних про зарплати.")

        average = int(total / count)
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None
