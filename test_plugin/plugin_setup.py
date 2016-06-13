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
    function=test_plugin.blocking_test_function,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'timeout': Int},
    outputs=[('relative_frequency_table', FeatureTable[RelativeFrequency])],
    name='Blocking test',
    doc='Set a timeout for this script to run, then try to run more things!'
)
