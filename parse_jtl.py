#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import csv
import logging

from collections import namedtuple
from collections import defaultdict

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO, filename='1.txt')

SLOT_NUM = 60

result_member = ('total_count', 'total_error_count', 'error_msg', 'error_code',
                 'count', 'error', 'rt', 'min_rt', 'max_rt')

parse_member = ('count', 'error', 'rt', 'min_rt', 'max_rt')


class Bucket(object):

    def __init__(self, label):
        self._count = [0] * 60
        self._err = [0] * 60
        self._res_time = [0] * 60
        self._min_res_time = [-1] * 60
        self._max_res_time = [0] * 60
        self._label = label
        self._total = 0
        self._total_err = 0
        self._err_msg = defaultdict(int)
        self._err_code = defaultdict(int)

    @property
    def label(self):
        return self._label

    @property
    def total_count(self):
        return self._total

    @property
    def total_error_count(self):
        return self._total_err

    @property
    def error_msg(self):
        return self._err_msg

    @property
    def error_code(self):
        return self._err_code

    @property
    def count(self):
        return self._count

    @property
    def error(self):
        return self._err

    @property
    def rt(self):
        return self._res_time

    @property
    def min_rt(self):
        return self._min_res_time

    @property
    def max_rt(self):
        return self._max_res_time

    def _update_total(self):
        self._total += 1

    def _update_total_err(self):
        self._total_err += 1

    def _update_err_msg(self, err_msg):
        self._err_msg[err_msg] += 1

    def _update_err_code(self, err_code):
        self._err_code[err_code] += 1

    def _update_count(self, index):
        self._count[index] += 1

    def _update_err(self, index):
        self._err[index] += 1

    def _update_res_time(self, index, res_time):
        self._res_time[index] += res_time

    def _update_min_res_time(self, index, res_time):
        if self._min_res_time[index] == -1:
            self._min_res_time[index] = res_time
        else:
            self._min_res_time[index] = min(
                self._min_res_time[index], res_time)

    def _update_max_res_time(self, index, res_time):
        self._max_res_time[index] = max(self._max_res_time[index], res_time)

    def __call__(self, index, res_time, err, err_msg, err_code):
        if err:
            self._update_total_err()
            self._update_err_msg(err_msg)
            self._update_err_code(err_code)
            self._update_err(index)

        self._update_total()
        self._update_count(index)
        self._update_res_time(index, res_time)
        self._update_min_res_time(index, res_time)
        self._update_max_res_time(index, res_time)


class FileSuffixInvalid(Exception):
    """File suffix is not jtl."""


class Aggregator(object):

    _jtl_format = ['time_stamp', 'res_time', 'label',
                   'err_code', 'err_msg', 'null',
                   'null', 'err', 'null', 'null',
                   'null', 'null', 'null']

    def __init__(self, start_time, end_time, filename):
        self._start_time = start_time
        self._end_time = end_time
        self._fn = filename
        self._bucket = {}
        self._pretreatment()

    def _pretreatment(self):
        self._suffix = self._fn.split('.')[-1]
        if not self._suffix == 'jtl':
            raise FileSuffixInvalid

        self._duration = self._end_time + 1 - self._start_time
        logger.info('duration: {}'.format(self._duration))

    def _get_index(self, ctime):
        return (ctime - self._start_time) * SLOT_NUM / self._duration

    def process(self):
        Result = namedtuple('Result', self._jtl_format, rename=True)

        for re in map(Result._make, csv.reader(open(self._fn, 'rb'))):
            time_stamp = int(re.time_stamp)
            res_time = int(re.res_time)
            err = True if re.err.lower() == 'false' else False
            index = self._get_index(time_stamp)
            bucket = self._bucket.setdefault(re.label, Bucket(re.label))
            bucket(index, res_time, err, re.err_msg, re.err_code)

    def display(self):
        for key, value in self._bucket.items():
            logger.info('{}'.format(key))
            for sub_key in result_member:
                if sub_key in parse_member:
                    for i in getattr(value, sub_key):
                        logger.info('\t{}: {}'.format(sub_key, i))
                else:
                    logger.info(
                        '\t{}: {}'.format(sub_key, getattr(value, sub_key)))


if __name__ == '__main__':
    test = Aggregator(
        1490771130141,
        1490771333214,
        './Downloads/booking_payment_batch_800.jtl')
    test.process()
    test.display()
