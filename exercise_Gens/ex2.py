#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def test():
    for y in [1, 2, 3]:
        y = (yield y)
        print 'in test:{}'.format(y)
        y += 1


x = test()
z = None
z = x.send(z)
z = x.send(z)
x.close()
