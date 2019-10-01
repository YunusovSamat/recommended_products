import random


class OrderGeneration:
    def __init__(self):
        self._products = [
            'footwear', 'trousers', 'a cap', 'jacket', 'T-shirt',
            'coat', 'hoody', 'sweater', 'jeans', 'shorts',
            'sneakers', 'dress', 'a bag', 'belt', 'backpack'
        ]
        self._len_products = len(self._products)
        self._orders = list()

    def orders_generation(self) -> None:
        self._orders.clear()
        for i in range(random.randint(1, 10)):
            row_orders = ';'.join(
                random.sample(self._products, random.randint(1, 5))
            ) + ';'
            self._orders.append(row_orders)

    def write_orders_to_file(self, file_path: str) -> None:
        with open(file_path, 'w') as file:
            file.write('\n'.join(self._orders))


if __name__ == '__main__':
    gen = OrderGeneration()
    gen.orders_generation()
    gen.write_orders_to_file(r'/home/samat/PycharmProjects/TaskPackage/'
                             r'recommended_products/orders02')
