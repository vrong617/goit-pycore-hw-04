def get_cats_info(path):
    cats_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # перевірка на пусту строку
                    cat_id, name, age_str = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age_str
                    }
                    cats_list.append(cat_info)

        return cats_list

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {str(e)}")
        return []

print(get_cats_info("text.txt"))