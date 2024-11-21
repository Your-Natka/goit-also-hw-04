from cat_utils import parse_cats_data

def get_cats_info(file_path):
    """
    Читає файл із даними про котів і повертає список словників.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return parse_cats_data(content)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []