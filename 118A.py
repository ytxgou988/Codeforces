#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def petya(str):
    result = []
    for elem in str:
        if elem in ["A", "O", "Y", "E", "U", "I", "a", "o", "y", "e", "u", "i"]:
            pass
        else:
            result.append('.')
            if elem.isupper():
                result.append(elem.lower())
            else:
                result.append(elem)
    return ''.join(result)

if __name__ == "__main__":
    str = sys.stdin.readline().strip()
    result = petya(str)
    print result

