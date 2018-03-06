#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import argparse
import os


def get_args():
    """This is function which get command line input parameters"""

    parser = argparse.ArgumentParser("split a file into pieces")
    parser.add_argument('file',
                        help='Input file name',
                        type=str)
    parser.add_argument('num',
                        help='Put num lines per output file',
                        type=int)
    return vars(parser.parse_args())


def gofn(file, num):
    """Generate output file name"""

    root, _ = os.path.splitext(file)

    def wrapper(i):
        return root + '_' + str(i / num - 1) + '.txt'
    return wrapper


def split(file, num):

    if not os.path.isfile(file):
        raise(TypeError, "Not regular file")

    bucket = ''
    get_fname = gofn(file, num)

    with open(file, 'r') as fi:
        for i, l in enumerate(fi, 1):
            bucket += l
            if i % num == 0:
                with open(get_fname(i), 'w') as fo:
                    fo.write(bucket)
                bucket = ''
        else:
            if not i % num == 0:
                offset = (i % num + 1) * num
                with open(get_fname(offset), 'w') as fo:
                    fo.write(bucket)
                bucket = ''


if __name__ == '__main__':
    split(**get_args())
