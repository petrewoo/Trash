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


if __name__ == '__main__':
    path = '/Users/wushenzhe/Documents'

    results = findfiles(path)
    for re in results:
        print re
