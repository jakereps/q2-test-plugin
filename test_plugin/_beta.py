# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from time import sleep

import biom


def blocking_test_function(table: biom.Table, timeout: int,
                           axis: str='sample') -> biom.Table:
    sleep(timeout)
    return table.norm(axis=axis, inplace=False)
