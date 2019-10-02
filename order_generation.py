import os
import random


class OrderGeneration:
    def __init__(self):
        self.__products = (
            'footwear', 'trousers', 'a cap', 'jacket', 'T-shirt',
            'coat', 'hoody', 'sweater', 'jeans', 'shorts',
            'sneakers', 'dress', 'a bag', 'belt', 'backpack'
        )
        self.__len_products = len(self.__products)
        self.__orders = list()

    def orders_generation(self) -> None:
        self.__orders.clear()
        for i in range(random.randint(1, 10)):
            line = ';'.join(
                random.sample(self.__products, random.randint(1, 5))
            ) + ';'
            self.__orders.append(line)

    def write_to_file(self, file_path: str) -> None:
        file_dirs, file_name = os.path.split(file_path)
        if os.path.isdir(file_dirs):
            if file_name:
                with open(file_path, 'w') as file:
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
