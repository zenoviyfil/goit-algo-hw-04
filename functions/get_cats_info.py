def get_cats_info(path):
    pet_dic = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    pet_code, name, age = line.strip().split(',')
                    pet_dic.append({"id": pet_code, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка в рядку: {line}")
        return pet_dic
    except FileNotFoundError:
        print("Помилка: Файл не знайдено!")
        return None
    except (OSError, ValueError) as error:
        print(f"Помилка при читанні файлу: {error}")
        return None
    
cats_info = get_cats_info("./data/cat_data.txt")
print(cats_info)
