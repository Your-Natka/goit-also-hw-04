def parse_cats_data(decoded_content):
    """
    Парсить текстові дані котів, отримані з файлу, і повертає список словників.
    """
    cats_info = []
    for line in decoded_content.splitlines():
        try:
            cat_id, name, age = line.strip().split(',')
            cats_info.append({"id": cat_id, "name": name, "age": int(age)})
        except ValueError:
            print(f"Помилка у форматі даних в рядку: {line.strip()}")
    return cats_info