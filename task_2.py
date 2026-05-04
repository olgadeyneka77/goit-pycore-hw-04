def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, name, age = line.split(',')
                    cats_list.append({"id": cat_id, "name": name, "age": age})
                except ValueError:
                    print(f"Помилка: Рядок має неправильний формат: '{line}'")
                    continue
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    return cats_list
cats_info = get_cats_info("cats_info.txt")

# Гарне виведення кожного кота окремо
for cat in cats_info:
    print(f"ID: {cat['id']} | Ім'я: {cat['name']} | Вік: {cat['age']}")


