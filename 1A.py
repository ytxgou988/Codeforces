#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def get_num(n, m, a):
    if n % a == 0:
        x = n/a
    else:
        x = n/a+1
    if m % a == 0:
        y = m/a
    else:
        y = m/a+1
    return x*y

if __name__ == "__main__":
    str = sys.stdin.readline().strip().split()
    n = int(str[0])
    m = int(str[1])
    a = int(str[2])
    num = get_num(n, m, a)
    print num

