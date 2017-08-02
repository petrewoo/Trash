#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os


def findfiles(path):
    path = os.path.abspath(path)
    results = os.listdir(path)
    for re in results:
        target = path + '/' + re
        if os.path.isdir(target):
            for sub_re in findfiles(target):
                yield sub_re
        else:
            yield path + '/' + re


def filter(suffix, gen):
    for f in gen:
        _, ext = os.path.splitext(f)
        if suffix == ext:
            yield f


if __name__ == '__main__':
    path = './'

    results = filter('.py', findfiles(path))
    for re in results:
        print re
