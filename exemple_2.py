# -*- coding: utf-8 -*-
from pathlib import Path

# Створення бінарного файлу з даними про котів
file_path = Path("cats_file.bin")
cats_file = b"60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5"
file_path.write_bytes(cats_file)


def get_cats_info(path):
    cats_info = []  # Список для збереження інформації про котів
    try:
        # Перевірка існування файлу
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")

        # Читання бінарних даних і перетворення їх у текст
        with open(file_path, mode='rb') as file:
            content = file.read()
            # Перетворюємо байти в рядок, використовуючи кодування
            decoded_content = content.decode('utf-8')

        # Обробка рядків
        for line in decoded_content.splitlines():
            try:
                # Розділяємо кожен рядок на частини: id, name, age
                cat_id, name, age = line.strip().split(',')
                # Додаємо інформацію про кота до списку як словник
                cats_info.append({"id": cat_id, "name": name, "age": age})
            except ValueError:
                print(f"Помилка у форматі даних в рядку: {line.strip()}")

        return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


# Приклад використання функції
cats_info = get_cats_info("cats_file.bin")
print(cats_info)
