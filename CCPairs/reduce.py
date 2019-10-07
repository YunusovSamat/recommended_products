#!/usr/bin/python3

import sys

last_key, sum_values = None, 0
# Получаем каждую строку.
for line in sys.stdin:
    # Разделяем строку на ключ и значение.
    key, value = line.split('\t')
    # Если ключ не соответствует старому.
    if last_key and last_key != key:
        print(f'{last_key}\t{sum_values}')
        last_key, sum_values = key, int(value)
    else:
        last_key, sum_values = key, sum_values + int(value)

if last_key:
    print(f'{last_key}\t{sum_values}')
