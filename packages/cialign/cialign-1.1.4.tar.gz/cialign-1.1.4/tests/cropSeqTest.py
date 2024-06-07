#! /usr/bin/env python

import unittest
from unittest import mock
from parameterized import parameterized
import logging
import numpy as np

import CIAlign.cropSeq as cropSeq

class CropSeqsTests(unittest.TestCase):


    @parameterized.expand([
        [0.1, 0.1, '--UC----UCUCUCUCGCGUGUGUGAAAAAAAAAAAAAAAA----AAAUUUU------------A', 8, 52],
        [0.1, 0.1, '--UC--AAA-----UCUCUCUCGCGUGUGUGAAAAAAAAAAA----AAAUUUU------------A', 3, 53],
        [0.05, 0.1, '--UC--AAA-----UCUCUCUCAAAAAAAAAAAAAAAAAAAA----AAAUUUU-----------A', 6, 53],
        [0.05, 0.3, '--UC--AAA-----UCUCUCUCGCGUGUGUAAAAAAAAAAAA----AAAUUUU------------A', 14, 42]
        ])
    def testDetermineStartEnd(self, mingap_perc, redefine_perc, input, expected_start, expected_end):
        seq = []
        seq.append([s for s in input])
        input = np.array(seq[0])
        logger = logging.getLogger('path.to.module.under.test')
        with mock.patch.object(logger, 'debug') as mock_debug:
            start, end = cropSeq.determineStartEnd(input, "test_name", logger, mingap_perc, redefine_perc)

        self.assertEqual(start, expected_start)
        self.assertEqual(end, expected_end)

    @parameterized.expand([[0.05, 0.1, '--UC----UCUCUCUCGCGUGUGUGAAAAAAAAAAAAAAAAAAAAAA----AAAUUUU------------A', 8, 13],
                           [0.05, 0.1, '--UC--AA-----UCUCUCUCGCGUGUGUGAAAAAAAAAAAAAAAAA----AAAUUUU------------A', 13, 13],
                           [0.05, 0.2, '--UC--AA-----UCUCUCUCGCGUGUGUGAAAAAAAAAAAAAAAAA----AAAUUUU------------A', 13, 24],
                           [0.02, 0.2, '--UC--AA-----UCUCUCUCGGGAGAGGCGUAUAAAUCGAUCGAUCGAUCGUACGAUCGUACGAUGCUCGUGUGUGAAAAAAAAAAAAAAAAAAAAAAAAAAAA----AAAUUUU------------A', 13, 24],
                           [0.02, 0.3, '--UC--AA-----UCUCUCUCGCGUGUGUGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA----AAAUUUU------------A', 13, 24],
                           ])
    def testFindValue(self, mingap_perc, redefine_perc, input, expected_value, expected_reverse_value):
        seq = []
        seq.append([s for s in input])
        input = np.array(seq[0])
        reverse = input[::-1]
        value = cropSeq.findValue(input, mingap_perc, redefine_perc)
        reverseValue = cropSeq.findValue(reverse, mingap_perc, redefine_perc)

        self.assertEqual(value, expected_value)
        self.assertEqual(reverseValue, expected_reverse_value)

    @parameterized.expand([
            ['UCUCUCUCUCGCGUGUGUGAAAAAAAAAUUUUA', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'],
            ['UCUC--UCUCUCGCG---UGUGUGAAAAAAAAAUUUUA---', '0,0,0,0,2,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5'],
            ['--UC----UCUCUCUCGCGUGUGUGAAAAAA----AAAUUUU------------A', '2,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,10,10,10,10,10,10,10,22'],
    ])
    def testCountGaps(self, input, expected_gaps):
        seq = []
        seq.append([s for s in input])
        input = np.array(seq[0])

        gap_list = expected_gaps.split(",")
        expected = [int(s) for s in gap_list]

        gaps = cropSeq.countGaps(input)

        self.assertTrue(gaps == expected)
