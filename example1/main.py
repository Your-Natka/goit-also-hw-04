from Salary.salary_utils import total_salary

if __name__ == "__main__":
    # Шлях до файлу із зарплатами
    salary_file = "salary_file.txt"
    total, average = total_salary(salary_file)
    
    # Перевірка результатів
    if total is not None and average is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
