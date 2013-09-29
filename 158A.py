#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def next_round(n, k, lst):
    if lst[k-1] > 0:
        i = k
        while i < n and lst[i] > 0:
            if lst[i] == lst[k-1]:
                i += 1
            else:
                break
    else:
        i = k-1
        while i >= 0:
            if lst[i] > 0:
                break
            else:
                i -= 1
        i += 1
    return i

if __name__ == "__main__":
    data = sys.stdin.readline().strip().split()
    n = int(data[0])
    k = int(data[1])
    lst = sys.stdin.readline().strip().split()
    lst = [int(x) for x in lst]
    result = next_round(n, k, lst)
    print result
