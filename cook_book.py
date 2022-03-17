# Функции

def open_cook_book(file_name):
    """Функция для октрытия и чтения файла для формированием словаря рецептов
    """
    with open(file_name, encoding='utf-8') as cook_book:
        number_of_dishes = 1
        read_file = True
        cook_book_dict = {}
        ingredients_info_dict = {}
        count = 0
        while read_file == True:
            dish = cook_book.readline().strip()
            n = cook_book.readline()
            # Я честно так и не понял, как реализовать последующий вывод ингредиентов через их количество (n)
            # Строчку с readline() оставил, чтоб далее уже пошел цикл с информацией об ингредиентах
            # Буду рад, если подскажите и поясните этот момент :)
            list_of_ingredients = []
            for line in cook_book:
                if line == '\n':
                    number_of_dishes += 1
                    break
                element_of_line = line.split(' | ')
                ingredients_info_dict['ingredient_name'] = element_of_line[0]
                ingredients_info_dict['quantity'] = element_of_line[1]
                ingredients_info_dict['measure'] = element_of_line[2].strip()
                list_of_ingredients.append(ingredients_info_dict)
                ingredients_info_dict = {}
            cook_book_dict[dish] = list_of_ingredients
            count += 1
            if count == number_of_dishes:
                read_file = False
        return cook_book_dict

def show_cook_book(file_name):
    """Функция для вывода словаря рецептов
    """
    print('COOK BOOK:\n')
    for key, value in open_cook_book(file_name).items():
        print(f"{key}:")
        for v in value:
            print(f"\t\t{v['ingredient_name']} - {v['quantity']} {v['measure']}")
        print()


# Основной код

show_cook_book('recipes.txt')