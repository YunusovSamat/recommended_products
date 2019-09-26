#!/usr/bin/python3

import sys

last_key, sum_values = None, 0
for line in sys.stdin:
    key, value = line.split('\t')
    if last_key and last_key != key:
        print(last_key + '\t' + str(sum_values))
        last_key, sum_values = key, int(value)
    else:
        last_key, sum_values = key, sum_values + int(value)

if last_key:
    print(last_key + '\t' + str(sum_values))

# last_key, sum_values = None, 0
# for line in sys.stdin:
#     key, value = line.strip().split('\t')
#     if 'footwear' in key:
#         if last_key and last_key != key:
#             print(last_key + '\t' + str(sum_values))
#             last_key, sum_values = key, int(value)
#         else:
#             last_key, sum_values = key, sum_values + int(value)
# if last_key:
#     print(last_key + '\t' + str(sum_values))
