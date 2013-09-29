#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def divide(w):
    if w % 2 == 0:
        if w == 2:
            result = 'NO'
        else:
            result = 'YES'
    else:
        result = 'NO'
    return result

if __name__ == "__main__":
    data = sys.stdin.readline().strip()
    result = divide(int(data))
    print result
