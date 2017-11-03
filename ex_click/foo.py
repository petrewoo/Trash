#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import logging

import click

logger=logging.getLogger(__name__)


def boo(debug):
    loger_fmt='%(asctime)s %(name)s %(levelname)s %(message)s'
    if debug:
        logging.basicConfig(level=logging.DEBUG, format=loger_fmt)
    else:
        logging.basicConfig(level=logging.INFO, format=loger_fmt)


@click.command()
@click.option('--debug', is_flag=True)
def start(debug):
    boo(debug)
    logger.info('Display info message')
    logger.debug('Display debug message')


def print_version(ctx, param, value):
    if not value and ctx.resilient_parsing:
        return

    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
def foo():
    click.echo('Hello World!')


if __name__ == '__main__':
    foo()
