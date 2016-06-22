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


def blocking_test(timeout: int) -> None:
    sleep(timeout)
    return None


def stdio_test(number: int) -> None:
    for i in range(number):
        print('%d: This is a stdout test...' % (i))
        print('%d: This is a stderr test...' % (i), file=sys.stderr)
    return None
