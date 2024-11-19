from pathlib import Path

def read_binary_file(path):
    """
    Зчитує вміст бінарного файлу та повертає його у вигляді рядка.
    """
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Файл за шляхом {path} не знайдено.")
    
    with open(file_path, mode='rb') as file:
        return file.read().decode('utf-8')