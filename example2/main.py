from file_handler import get_cats_info

if __name__ == "__main__":
    # Задаємо шлях до файлу з даними
    file_path = "cats_file.txt"
    
    # Отримуємо список інформації про котів
    cats_info = get_cats_info(file_path)
    
    # Виводимо результат
    print(cats_info)