#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from itertools import tee


def peep(iterator):
    iter_list = tee(iterator)
    return next(iter_list[0]), iter_list[1]


if __name__ == '__main__':
    it = iter(range(1, 6))
    f_ele, it1 = peep(it)
    print f_ele, list(it1)
