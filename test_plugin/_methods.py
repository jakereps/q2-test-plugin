# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from time import sleep
import sys

import biom


def blocking_test(table: biom.Table, timeout: int) -> biom.Table:
    sleep(timeout)
    return table


def stdio_test(table: biom.Table, number: int) -> biom.Table:
    for i in range(number):
        print('%d: This is a stdout test...' % (i))
        print('%d: This is a stderr test...' % (i), file=sys.stderr)
    return table


def defaults_test(table: biom.Table, timeout: int = 5) -> biom.table:
    return table


def boolean_test(table: biom.Table, it_worked: bool) -> biom.Table:
    print(it_worked)
    return table
