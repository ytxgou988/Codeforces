#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def abbreviation(lst):
    result = []
    for word in lst:
        if len(word) > 10:
            result.append(word[0] + str(len(word)-2) + word[-1])
        else:
            result.append(word)
    return result

if __name__ == "__main__":
    lst = []
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        lst.append(sys.stdin.readline().strip())
    lst = abbreviation(lst)
    for word in lst:
        print word
