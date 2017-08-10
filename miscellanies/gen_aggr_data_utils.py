#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import __builtin__
import random
from itertools import repeat, chain, imap


def random_subset(fd):
    re = next(fd)

    for n, line in enumerate(fd):
        if random.randrange(n + 2):
            continue
        re = line

    return re


def rand_line(fn):
    def _():
        with open(fn, 'r') as f:
            return random_subset(f)
    return _


def new_next(*args, **kwargs):
    return __builtin__.next(*args, **kwargs).strip('\n')


class ZipExhausted(Exception):
    pass


def izip_longest(*args, **kwds):

    func_list = kwds.get('func_list')

    counter = [1] * len(args)

    def sentinel(i):
        counter[i] -= 1
        if all(v == 0 for v in counter):
            raise ZipExhausted
        yield func_list[i]()

    iterators = \
        [chain(it, sentinel(n), repeat(func_list[n]()))
         for n, it in enumerate(args)]
    try:
        while iterators:
            yield tuple(map(new_next, iterators))
    except ZipExhausted:
        pass


class MFiles(object):

    def __init__(self, files, func_list):
        if isinstance(files, basestring):
            files = (files, )
        else:
            if files:
                files = tuple(files)
            else:
                raise TypeError('Empty file list input')

        self._fd_list = []
        self._files = files
        self._func_list = func_list

    def _open(self, files):
        self._fd_list = [open(f) for f in files]
        return self._izip_longest()

    def __enter__(self):
        return self._open(self._files)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            pass
        finally:
            for fd in self._fd_list:
                fd.close()

    def _izip_longest(self):
        counter = [1] * len(self._fd_list)

        def sentinel(i):
            counter[i] -= 1
            if all(v == 0 for v in counter):
                raise ZipExhausted
            yield self._func_list[i]()

        iterators = \
            [chain(it, sentinel(n), repeat(self._func_list[n]()))
             for n, it in enumerate(self._fd_list)]
        try:
            while iterators:
                yield tuple(map(new_next, iterators))
        except ZipExhausted:
            pass


if __name__ == '__main__':
    f_list = ['1.txt', '2.txt', '3.txt']
    func_list = [f for f in imap(rand_line, f_list)]
    with MFiles(f_list, func_list) as fi:
        for i in fi:
            print i
