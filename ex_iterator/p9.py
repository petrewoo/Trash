#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from itertools import izip, count


def my_enumerate(iterator):
    return izip(count(), iterator)


if __name__ == '__main__':
    t = iter(range(10, 1, -1))
    for ele in my_enumerate(t):
        print ele
