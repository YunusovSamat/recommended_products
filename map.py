#!/usr/bin/python3

import sys

MY_PRODUCT = 'footwear'

for line in sys.stdin:
    if MY_PRODUCT in line:
        # list_products = [elem for elem in line.split(';')
        #                  if elem not in ('\n', '', 'footwear')]
        for elem in line.split(';'):
            if elem not in ('', '\n', MY_PRODUCT):
                print(elem + '\t1')

        # for i in range(len(products)-1):
        #     for j in range(i+1, len(products)):
        #         if products[i] < products[j]:
        #             print((products[i], products[j]), '\t', 1, sep='')
        #         elif products[i] > products[j]:
        #             print((products[j], products[i]), '\t', 1, sep='')
