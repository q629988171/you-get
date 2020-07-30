#!/usr/bin/env python

import unittest

from you_get.extractors import (
    iqiyi,
)


class YouGetTests(unittest.TestCase):
    def iqiyi_test(self):
        iqiyi.download(
            'https://www.iqiyi.com/v_19rrk5grlg.html', info_only=True)


if __name__ == '__main__':
    unittest.main()
