import os
import random


# Класс для генерации и записи заказов.
class OrderGeneration:
    __slots__ = ('__products', '__len_products', '__orders')

    def __init__(self):
        # Список всех товаров.
        self.__products = (
            'footwear', 'trousers', 'a cap', 'jacket', 'T-shirt',
            'coat', 'hoody', 'sweater', 'jeans', 'shorts',
            'sneakers', 'dress', 'a bag', 'belt', 'backpack'
        )
        # Количество всех товаров.
        self.__len_products = len(self.__products)
        # Список заказов.
        self.__orders = list()

    # Генерируем список заказов.
    def orders_generation(self) -> None:
        # Очищаем список заказов.
        self.__orders.clear()
        # Генерируем случайное количество строк от 1 до 10.
        for i in range(random.randint(1, 10)):
            # Выбираем случайные товары от 1 до 5
            # добавляем между ними и в конце разделители.
            line = ';'.join(
                random.sample(self.__products, random.randint(1, 5))
            ) + ';'
            self.__orders.append(line)

    # Записываем списко заказов в файл.
    def write_to_file(self, file_path: str) -> None:
        # Разделяем путь на каталоги и имя файла.
        file_dirs, file_name = os.path.split(file_path)
        # Если каталоги существуют.
        if os.path.isdir(file_dirs):
            # Если имя файла есть.
            if file_name:
                # Открываем файл на запись.
                with open(file_path, 'w') as file:
                    # Записываем в файл список заказов с новой строки.
                    file.write('\n'.join(self.__orders))
                print("Record to file")
            else:
                print("Error: object is a directory")
        else:
            print("Error: No such file or directory")


if __name__ == '__main__':
    gen = OrderGeneration()
    gen.orders_generation()
    gen.write_to_file(r'/home/samat/PycharmProjects/TaskPackage/'
                      r'recommended_products/orders01.txt')
