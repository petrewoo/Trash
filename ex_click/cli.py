#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

import click

logger=logging.getLogger(__name__)


@click.command()
def cli():
    print 'Hello World'


@click.command()
@click.option('--debug', is_flag=True, help='Debug mode')
def foo(debug):
    logger_fmt='%(asctime)s %(name)s %(levelname)s %(message)s'
    if debug:
        logging.basicConfig(level=logging.DEBUG, format=logger_fmt)
    else:
        logging.basicConfig(level=logging.INFO, format=logger_fmt)

    logger.info('Display info message')
    logger.debug('Display debug message')
