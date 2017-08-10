#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def eoho(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            try:
                value = (yield value)
            except GeneratorExit:
                raise TypeError
            except Exception, e:
                print 'hoho'
                value = e
    finally:
        print "Don't forget to clean up when 'close()' is called."
