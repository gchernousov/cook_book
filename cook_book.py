# Функции

def get_info_cook_book(file_name):
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
                ingredients_info_dict['quantity'] = int(element_of_line[1])
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
    for key, value in get_info_cook_book(file_name).items():
        print(f"{key}:")
        for v in value:
            print(f"\t\t{v['ingredient_name']} - {v['quantity']} {v['measure']}")
        print()

# def generate_ingredients_data(dish_name, person_count):
#     if dish_name in get_info_cook_book('recipes.txt').keys():
#         result_dict = {} # потом убрать
#         for ingredient_info in get_info_cook_book('recipes.txt')[dish_name]:
#             result_dict[ingredient_info['ingredient_name']] = {'measure': ingredient_info['measure'],
#                                                                'quantity': ingredient_info['quantity'] * person_count}
#         print(f'\nДля приготовления {dish_name} на {person_count} персон(ы) Вам потребуется:\n')
#         for key, value in result_dict.items():
#             print(f'{key}: {value["quantity"]} {value["measure"]}')
#     else:
#         print(f'\nИзвините, но в книге нет рецепта для {dish_name}')

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = {}
    current_q = 0
    if type(dishes) == list or type(dishes) == tuple:
        for dish_name in dishes:
            if dish_name in get_info_cook_book('recipes.txt').keys():
                for ingredient_info in get_info_cook_book('recipes.txt')[dish_name]:
                    if ingredient_info['ingredient_name'] in result_dict.keys():
                        current_q = result_dict[ingredient_info['ingredient_name']]['quantity']
                    result_dict[ingredient_info['ingredient_name']] = {'measure': ingredient_info['measure'],
                                                                       'quantity': ingredient_info['quantity'] + current_q}
            else:
                print(f'\nИзвините, но в книге нет рецепта для {dish_name}')
        print(f'\nДля приготовления указанных блюд на {person_count} персон(ы) Вам потребуется:\n')
        for key, value in result_dict.items():
            print(f'{key}: {value["quantity"] * person_count} {value["measure"]}')
    elif type(dishes) == str:
        if dishes in get_info_cook_book('recipes.txt').keys():
            for ingredient_info in get_info_cook_book('recipes.txt')[dishes]:
                result_dict[ingredient_info['ingredient_name']] = {'measure': ingredient_info['measure'],
                                                                   'quantity': ingredient_info['quantity']}
            print(f'\nДля приготовления указанных блюд на {person_count} персон(ы) Вам потребуется:\n')
            for key, value in result_dict.items():
                print(f'{key}: {value["quantity"] * person_count} {value["measure"]}')
    else:
        print('НЕПРАВИЛЬНЫЙ ВВОД')


# Основной код

# Вывод содержимого книги рецептов:
show_cook_book('recipes.txt')

# Вывод необходимых ингредиентов и их количества:
print('\n>>> Заказ одного блюда:')
get_shop_list_by_dishes('Утка по-пекински', 2)

print('\n>>> Заказ списка блюд:') # Также реализована возможность заказа кортежа блюд
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print('\n>>> Заказ списка блюд, среди которых есть те, которых нет в книге рецептов:')
get_shop_list_by_dishes(['Борщ', 'Омлет', 'Цезарь'], 4)

print('\n>>> Заказ двух одинаковых блюд:')
get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)

print('\n>>> Заказ блюд с одинаковыми ингредиентами:')
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

print('\n>>> Заказ блюд с одинаковыми блюдами и ингредиентами:')
# Решил отработать и такой вариант и он внезапно вызвал у меня сложность, но, вроде, разобрался
get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Омлет'], 2)