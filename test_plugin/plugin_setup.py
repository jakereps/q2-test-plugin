# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime.plugin import Plugin, Int

import test_plugin
from q2_types import FeatureTable, Frequency, RelativeFrequency

plugin = Plugin(
    name='test-plugin',
    version=test_plugin.__version__,
    website='http://github.com/jakereps/q2-test-plugin',
    package='test_plugin'
)

plugin.register_function(
    function=test_plugin.blocking_test,
    inputs={},
    parameters={'timeout': Int},
    outputs=[],
    name='Blocking test',
    doc='Set a timeout for this script to run, then try to run more things!'
)

plugin.register_function(
    function=test_plugin.stdio_test,
    inputs={},
    parameters={'number': Int},
    outputs=[],
    name='stdout and stderr test',
    doc='Given a number n, print to stdout and stderr n times.'
)
