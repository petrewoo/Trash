#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import re


def findfiles(path):
    path = os.path.abspath(path)
    results = os.listdir(path)
    for r in results:
        target = path + '/' + r
        if os.path.isdir(target):
            for sub_re in findfiles(target):
                yield sub_re
        else:
            yield path + '/' + r


def filter(suffix, gen):
    for f in gen:
        _, ext = os.path.splitext(f)
        if suffix == ext:
            yield f


def count(results):
    s = 0
    for r in results:
        with open(r, 'r') as f:
            s += sum(1 for _ in f if not re.match('^(\s)*$|^#', _))
    return s


if __name__ == '__main__':
    path = './'
    results = filter('.py', findfiles(path))
    print count(results)
