# -*- coding: utf-8 -*-

from pathlib import Path

# Створюємо файл salary_file.txt та записуємо в нього дані
file_path = Path("salary_file.txt")
file_path.write_text("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000", encoding="utf-8")

# Функція для обчислення загальної та середньої зарплати
def total_salary(path):
    try:
        # Перевіряємо, чи існує файл
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")

        total = 0
        count = 0

        # Відкриваємо файл з менеджером контексту для автоматичного закриття
        with open(file_path, mode='r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на ім'я та зарплату
                try:
                    _, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print("Помилка у форматі даних в рядку:", line.strip())

        # Перевірка, чи є дані для обчислення
        if count == 0:
            raise ValueError("Файл не містить коректних даних про зарплати.")

        # Обчислюємо середню зарплату
        average = int(total / count)
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None

# Приклад використання функції
total, average = total_salary("salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
