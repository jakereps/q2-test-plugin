# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import test_plugin

setup(
    name='test-plugin',
    version=test_plugin.__version__,
    packages=find_packages(),
    install_requires=['scikit-bio >= 0.4.2',
                      'qiime >= 2.0.0', 'q2-types'],
    pacakge_data={'test_plugin': ['workflows/*md']},
    author='Jorden Kreps',
    author_email='jordenkreps@gmail.com',
    description='Various workflow tests for qiime-studio.',
    license='BSD',
    url='http://www.qiime.org',
    entry_points={
        'qiime.plugins': ['test-plugin=test_plugin.plugin_setup:plugin']
    }
)
