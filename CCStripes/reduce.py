#!/usr/bin/python3

import sys
last_key = None
d = dict()
for line in sys.stdin:
    key, value = line.split('\t')
    if last_key and last_key != key:
        for d_key in d:
            print(f'{last_key} & {d_key}\t{d[d_key]}')
        last_key = key
        d.clear()
        for param in value.split('&'):
            param_key, param_val = param.split(':', 1)
            d[param_key] = int(param_val)
    else:
        last_key = key
        for param in value.split('&'):
            param_key, param_val = param.split(':', 1)
            d[param_key] = int(d.get(param_key, 0)) + int(param_val)

if last_key:
    for d_key in d:
        print(f'{last_key} & {d_key}\t{d[d_key]}')
