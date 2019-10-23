#!/usr/bin/python3

import sys

for line in sys.stdin:
    products = [elem for elem in line.split(';') if elem not in ('', '\n')]
    products.sort()
    for i in range(len(products)-1):
        d = dict.fromkeys(products[i+1:], 0)
        for product in products[i+1:]:
            d[product] += 1
        d_format = '&'.join([f'{key}:{d[key]}' for key in d])
        print(f'{products[i]}\t{d_format}')
