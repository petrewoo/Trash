#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class reverse_iter:

    def __init__(self, l):
        self._l = l

    def __iter__(self):
        return self

    def next(self):
        if len(self._l):
            return self._l.pop()
        else:
            raise StopIteration


if __name__ == '__main__':
    """Test case"""
    test_list = [1, 2, 3, 4, 7, 5]
    x = reverse_iter(test_list)
    while 1:
        print next(x)
