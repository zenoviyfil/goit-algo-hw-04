def total_salary(path):
    total_salary = 0
    total_employee = 0
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            total_employee = len(lines)

            for line in lines:
                try:
                    _, salary = line.strip().split(",")
                    total_salary += float(salary)
                except ValueError:
                    print(f"Помилка в рядку: {line}")

            average_salary = total_salary / total_employee if total_employee > 0 else 0

        return total_salary, average_salary
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
        return None
    except (OSError, ValueError) as error:
        print(f"Помилка при читанні файлу: {error}")
        return None
    
total, average = total_salary("./data/salary_data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

