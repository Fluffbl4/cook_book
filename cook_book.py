import os
import os.path

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients
#print(f'cook_book = {cook_book}')

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += int(consist['quantity']) * int(person_count)
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': int(consist['quantity']) * int(person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def count_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for line in f if line.strip())


def rewrite_files(file_for_writing: str, base_path, location):
    # Перебираем все файлы в подпапке и считаем количество строк в каждом
    files = [(count_lines(os.path.join(base_path, location, filename)), os.path.join(base_path, location, filename),
              filename) \
             for filename in os.listdir(os.path.join(base_path, location))]

    # Сортируем файлы по количеству строк
    sorted_files = sorted(files, key=lambda x: x[0])

    # Открываем итоговый файл для записи
    with open(file_for_writing, 'w', encoding='utf-8') as result_file:
        for _, path, filename in sorted_files:
            # Записываем служебную информацию
            result_file.write(f'{filename}\n{count_lines(path)}\n')

            # Читайте и записывайте содержимое файла построчно
            with open(path, 'r', encoding='utf-8') as input_file:
                result_file.write(input_file.read())
                result_file.write('\n')

# Определяем пути
file_for_writing = os.path.abspath('\\Users\\prajs\\Desktop\\cook_book\\1.txt')
base_path = os.getcwd()
location = os.path.abspath('\\Users\\prajs\\Desktop\\cook_book\\files_to_task_3')

# Вызываем функцию для объединения файлов
rewrite_files(file_for_writing, base_path, location)
