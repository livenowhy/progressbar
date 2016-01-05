#!/usr/bin/python2
# coding:utf-8
"""
@version: 0.0.1
@author: livenowhy
@license: Apache Licence 
@contact: livenowhy@hotmail.com
@file: test.py
@time: 2015/12/29 21:32
"""
from progressbar import ProgressBar
from progressbar import AnimatedProgressBar
import time
import unittest

FILESIZE = 2045824
CHUNK = 1

def testone():
    progress = AnimatedProgressBar(end=FILESIZE, width=50)

    for i in range(0, FILESIZE, CHUNK):
        progress + CHUNK
        progress.show_progress()


def testtwo():
    p = AnimatedProgressBar(end=100, width=80)

    while True:
        p + 5
        p.show_progress()
        time.sleep(0.1)
        if p.progress == 100:
            break


class DefaultsTestCase(unittest.TestCase):
    """
    ProgressBar defaults:
    start = 0
    end = 10
    width = 12
    fill = '='
    blank = '.'
    format = '[%(fill)s>%(blank)s] %(progress)s%%'
    incremental = True
    """
    def setUp(self):
        self.p = ProgressBar()

    def tearDown(self):
        del(self.p)

    def test_initialization(self):
        """
        >>> p = ProgressBar()
        >>> p
        [>............] 0%
        """
        self.assertEqual(str(self.p), '[>............] 0%')

    def test_increment(self):
        """
        >>> p = ProgressBar()
        >>> p + 1
        [=>...........] 10%
        """
        self.p + 1
        self.assertEqual(str(self.p), '[=>...........] 10%')

    def test_reset(self):
        """
        >>> p = ProgressBar()
        >>> p += 8
        >>> p.reset()
        [>............] 0%
        """
        self.p += 8
        self.p.reset()
        self.assertEqual(str(self.p), '[>............] 0%')

    def test_full_progress(self):
        """
        >>> p = ProgressBar()
        >>> p + 10
        [============>] 100%
        """
        self.p + 10
        self.assertEqual(str(self.p), '[============>] 100%')
        self.p + 10
        self.assertEqual(str(self.p), '[============>] 100%')


class CustomizedTestCase(unittest.TestCase):
    """
    ProgressBar custom:
    start = 0
    end = 100
    width = 20
    fill = '#'
    blank = '.'
    format = '%(progress)s%% [%(fill)s%(blank)s]'
    incremental = True
    """
    custom = {
        'end': 100,
        'width': 20,
        'fill': '#',
        'format': '%(progress)s%% [%(fill)s%(blank)s]'
    }
    def setUp(self):
        self.p = ProgressBar(**self.custom)

    def tearDown(self):
        del(self.p)

    def test_initialization(self):
        """
        >>> p = ProgressBar(custom)
        >>> p
        0% [....................]
        """
        self.assertEqual(str(self.p), '0% [....................]')

    def test_increment(self):
        """
        >>> p = ProgressBar(custom)
        >>> p + 1
        1% [....................]
        """
        self.p + 1
        self.assertEqual(str(self.p), '1% [....................]')
        self.p + 4
        self.assertEqual(str(self.p), '5% [#...................]')

    def test_reset(self):
        """
        >>> p = ProgressBar(custom)
        >>> p += 8
        >>> p.reset()
        0% [....................]
        """
        self.p += 8
        self.p.reset()
        self.assertEqual(str(self.p), '0% [....................]')

    def test_full_progress(self):
        """
        >>> p = ProgressBar()
        >>> p + 10
        100% [####################]
        """
        self.p + 100
        self.assertEqual(str(self.p), '100% [####################]')
        self.p + 100
        self.assertEqual(str(self.p), '100% [####################]')


if __name__ == '__main__':
    unittest.main()