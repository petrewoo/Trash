#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def readfiles(files):
    for f in files:
        with open(f, 'r') as fo:
            for line in fo:
                yield line


def l_filter(lines):
    return (l for l in lines if len(l) > 40)


def print_lines(lines):
    for l in lines:
        print l


if __name__ == '__main__':
    f_list = ['1.txt', '2.txt']
    re = readfiles(f_list)
    re = l_filter(re)
    print_lines(re)
