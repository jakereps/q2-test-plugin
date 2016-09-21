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

plugin.methods.register_function(
    function=test_plugin.blocking_test,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'timeout': Int},
    outputs=[('rarefied_table', FeatureTable[Frequency])],
    name='Blocking test',
    description='Set a timeout for this script to run, '
                'then try to run more things!'
)

plugin.methods.register_function(
    function=test_plugin.stdio_test,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'number': Int},
    outputs=[('rarefied_table', FeatureTable[Frequency])],
    name='stdout and stderr test',
    description='Given a number n, print to stdout and stderr n times.'
)

plugin.methods.register_function(
    function=test_plugin.defaults_test,
    inputs={'table': FeatureTable[Frequency]},
    parameters={'timeout': Int},
    outputs=[('rarefied_table', FeatureTable[Frequency])],
    name='Defaults Test',
    description='See if the defaults auto-populate where they should.'
)
