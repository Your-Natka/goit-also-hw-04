from file_handler import read_binary_file
from cat_utils import parse_cats_data

if __name__ == "__main__":
    file_path = "cats_file.bin"
    
    try:
        # Зчитуємо бінарний файл
        decoded_content = read_binary_file(file_path)
        # Парсимо дані котів
        cats_info = parse_cats_data(decoded_content)
        # Виводимо результат
        print("Інформація про котів:")
        for cat in cats_info:
            print(f"ID: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']} років")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Сталася помилка: {e}")