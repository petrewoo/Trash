#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def izip(*iterables):
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))


if __name__ == '__main__':
    i1 = iter(range(10))
    i2 = iter(range(20))

    iterators = izip(i1, i2)
    for i in iterators:
        print i
