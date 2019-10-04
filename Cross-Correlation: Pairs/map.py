#!/usr/bin/python3

import sys

# Получаем каждую строку.
for line in sys.stdin:
    products = [elem for elem in line.split(';') if elem not in ('', '\n')]
    for i in range(len(products)-1):
        for j in range(i+1, len(products)):
            # Выводим ключ - товары, значение - 1.
            if products[i] < products[j]:
                print(f'{products[i]} & {products[j]}\t1')
            elif products[j] < products[i]:
                print(f'{products[j]} & {products[i]}\t1')
